#define THREAD_COUNT 4
#define ID_SHIFT_AMOUNT 8
#define ID_SHIFT_MASK 0xFF
#define OUT_FILE "out.txt"

#include <iostream>
#include <sstream>
#include <fstream>

#include <string>
#include <vector>
#include <set>

#include <thread>
#include <mutex>
#include <chrono>
#include <csignal>

#include "Caveman.hpp"

int playGame(std::vector<std::string> commands, int contestants);
void playNextGame(std::vector<std::string> commands, std::vector<int>& duels, std::mutex& duelsMtx, std::ofstream& out, std::mutex& outMtx);
std::vector<int> getDuels(int numEntries, const std::string CACHE_FILE);

void onSIGINT(int _);
bool _finished = false;

int main() {
	// retrieve list of players
	std::ifstream playerlistFile("playerlist.txt");
	std::string line;
	std::vector<std::string> commands;
	while (std::getline(playerlistFile, line)) {
		commands.push_back(line);
	}

	// initialize and start threads
	std::vector<int> duels = getDuels(commands.size(), OUT_FILE);
	std::ofstream out(OUT_FILE, std::ios::out | std::ios::app);

	std::mutex duelsMtx, outMtx;
	std::thread threads[THREAD_COUNT];

	for (unsigned int i = 0; i < THREAD_COUNT; ++i) {
		threads[i] = std::thread(playNextGame, commands, std::ref(duels), std::ref(duelsMtx), std::ref(out), std::ref(outMtx));
	}

	// handle ctrl+c for lots of data
	struct sigaction handleSIGINT;
	handleSIGINT.sa_handler = onSIGINT;
	sigemptyset(&handleSIGINT.sa_mask);
	handleSIGINT.sa_flags = 0;
	sigaction(SIGINT, &handleSIGINT, NULL);

	// have main thread wait until other threads finished
	while (!_finished) {
		// do something just to avoid eating CPU
		std::this_thread::sleep_for(std::chrono::milliseconds(1000));
	}

	// completely finish other threads
	for (unsigned int i = 0; i < THREAD_COUNT; ++i) {
		threads[i].join();
	}

	out.close();
	return 0;
}

int playGame(std::vector<std::string> commands, int contestants) {
	int n1 = (contestants >> ID_SHIFT_AMOUNT) & ID_SHIFT_MASK,
		n2 = contestants & ID_SHIFT_MASK;
	Caveman c1(commands[n1]), c2(commands[n2]);

	for (int turnCount = 0; turnCount < 100; turnCount++) {
		int provokeResult = c1.provoke(c2);
		if (provokeResult == -1) return n2;
		if (provokeResult == 1) return n1;
	}

	return -1;
}

void playNextGame(std::vector<std::string> commands, std::vector<int>& duels, std::mutex& duelsMtx,
	std::ofstream& out, std::mutex& outMtx) {

	for (;;) {
		duelsMtx.lock();
		if (duels.empty()) {
			_finished = true;
			duelsMtx.unlock();
			return;
		}
		int duel = duels.back();
		duels.pop_back();
		duelsMtx.unlock();

		std::ostringstream winners("");
		for (int i = 0; i < 10; ++i) {
			winners << playGame(commands, duel) << " ";
		}
		std::string winnersStr = winners.str();
		winnersStr.pop_back();

		outMtx.lock();
		out << duel << " " << winnersStr << std::endl;
		outMtx.unlock();
	}
}

std::vector<int> getDuels(int numEntries, std::string CACHE_FILE) {
	// open file and grab data
	std::ifstream cache(CACHE_FILE);
	std::string line;
	std::set<int> cacheData;
	while (std::getline(cache, line)) {
		std::istringstream lineStream(line);
		int i;
		lineStream >> i;
		cacheData.insert(i);
	}

	// create duels, excluding already-done ones
	std::vector<int> duels;
	for (int p1 = 0; p1 < numEntries - 1; ++p1) {
		for (int p2 = p1 + 1; p2 < numEntries; ++p2) {
			int duel = p1 << ID_SHIFT_AMOUNT | p2;
			if (cacheData.find(duel) == cacheData.end()) {
				duels.push_back(duel);
			}
		}
	}

	return duels;
}

void onSIGINT(int _) {
	_finished = true;
}
