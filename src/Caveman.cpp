#include "Caveman.hpp"
#include <iostream>

Caveman::Caveman(std::string cmd): cmd(cmd), lastAction('X'), actionHistory(""), sharpness(0), dead(false) {
	// nothing to do here
}

// returns -1 for lose, 1 for win, 0 for N/A
int Caveman::provoke(Caveman& otherCaveman) {
	getAction(actionHistory.length() ? (actionHistory + "," + otherCaveman.actionHistory) : "");
	otherCaveman.getAction(actionHistory.length() ? (otherCaveman.actionHistory + "," + actionHistory) : "");
	actionHistory += lastAction == '^' ? 'P' : lastAction;
	otherCaveman.actionHistory += otherCaveman.lastAction == '^' ? 'P' : otherCaveman.lastAction;

	maybeSharpen();
	otherCaveman.maybeSharpen();

	maybePoke(otherCaveman);
	otherCaveman.maybePoke(*this);

	if (dead) return -1;
	if (otherCaveman.dead) return 1;
	return 0;
}

void Caveman::getAction(std::string input) {
	char DEFAULT = 'B';

	FILE* pipe = popen((cmd + (input.length() ? (" " + input) : "")).c_str(), "r");
	if (!pipe) {
		lastAction = DEFAULT;
	} else {
		lastAction = fgetc(pipe);
		if (lastAction != 'S' && lastAction != 'P' && lastAction != 'B') lastAction = DEFAULT;
		// blunt
		if (lastAction == 'P' && sharpness == 0) lastAction = DEFAULT;
		// sword
		if (lastAction == 'P' && sharpness >= 5) lastAction = '^';

		pclose(pipe);
	}
}

void Caveman::maybeSharpen() {
	if (lastAction == 'S') {
		++sharpness;
	}
}

void Caveman::maybePoke(Caveman& otherCaveman) {
	if (lastAction == 'P') {
		if (otherCaveman.lastAction == 'B' || otherCaveman.lastAction == 'P' || otherCaveman.lastAction == '^') {
			--sharpness;
		} else {
			otherCaveman.dead = true;
		}
	} else if (lastAction == '^') {
		if (otherCaveman.lastAction == '^') {
			--sharpness;
		} else {
			otherCaveman.dead = true;
		}
	}
}
