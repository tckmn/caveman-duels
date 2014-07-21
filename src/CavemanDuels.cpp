#define THREAD_COUNT 4
#define ID_SHIFT_AMOUNT 8

#include <iostream>
#include <sstream>
#include <fstream>

#include <string>
#include <vector>
#include <set>

#include <thread>
#include <mutex>

void playNextGame(std::vector<int>& duels, std::mutex& duelsMtx);
std::vector<int> getDuels(int numEntries, const std::string CACHE_FILE);

bool _finished = false;

int main() {
	// retrieve list of players
	std::ifstream playerlistFile("playerlist.txt");
	std::string line;
	std::vector<std::string> commands;
	while (std::getline(playerlistFile, line)) {
		commands.push_back(line);
	}

	// start playing!
	std::string OUT_FILE = "out.txt";
	std::ofstream out(OUT_FILE, std::ios::out | std::ios::app);
	std::vector<int> duels = getDuels(commands.size(), OUT_FILE);
	std::mutex duelsMtx;

	// initialize and start threads
	std::thread threads[THREAD_COUNT];
	for (unsigned int i = 0; i < THREAD_COUNT; ++i) {
		threads[i] = std::thread(playNextGame, duels, duelsMtx);
	}

	out.close();
	return 0;
}

void playNextGame(std::vector<int>& duels, std::mutex& duelsMtx) {
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
