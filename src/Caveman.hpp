#ifndef CAVEMAN_HPP
#define CAVEMAN_HPP

#include <string>

#include <cstdio>

class Caveman {
public:
	Caveman(std::string cmd);
	int provoke(Caveman& otherCaveman); // returns -1 for lose, 1 for win, 0 for N/A

private:
	std::string cmd;
	void getAction(std::string input);

	void maybeSharpen();
	void maybePoke(Caveman otherCaveman);

	char lastAction;
	std::string actionHistory;

	int sharpness;
	bool dead;
};

#endif
