# Testing a bot

For this purposes of this example, the bot you want to test will be called `BottyBot`.

1. Download the ZIP file for this Github repository (found at the bottom of the right sidebar) Unzip it and put it somewhere. Call it whatever you want (for this example, it will be called CavemanDuels).

2. Create a directory called `BottyBot` inside `CavemanDuels/players`. Place the files containing the code you wrote in this directory. Compile them, if necessary.
 - For scripting languages like Ruby, Python, or Perl, you would use `BottyBot.rb`, `BottyBot.py`, or `BottyBot.pl` respectively.
 - For compiled languages like Java, you would save your code as `BottyBot.java` and compile it with `javac *.java`.
 
3. Open the `CavemanDuels/playerlist.txt` file. Append the shell command used to run your program to that file (if you're confused as to how, just find one that also uses your language, copy it, and change its name).
 - If you want to test your bot against a specific other bot, remove every other line except your bot and the bot you want to test against.
 - If you want to test your bot against all other bots (i.e. run a full simulation), keep all of the commands there; you don't need to do anything else.

4. Compile the controller program. This will look something like this (on a Linux OS, assuming you start in the `CavemanDuels` directory):

        g++ -std=c++11 src/*.cpp src/*.hpp -o CavemanDuels -pthread

    Then, run the controller program (the executable called `CavemanDuels`). If you're testing against all submissions, this may take a while; be patient!

5. If you're running a UNIX-based / Linux system (or, although untested, probably OS X), you can execute `buildscores.sh`, which will give you a user-friendly easy-to-read chart of how all the bots performed (the same chart that is used for the leaderboard on the PPCG post).

    If you want to examine the raw data, open `out.txt`. Each line will have 4 numbers. The first is the battle ID. The second, third, and fourth are the player IDs of the winners of all three trials of the battle. A player's ID will be its line number in `playerlist.txt`, starting from zero (ex. the first player listed in `playerlist.txt` will have an ID of `0`). The battle ID is calculated with `playerId1 << 8 | playerId2`, where `<<` is a bit shift and `|` is bitwise OR.
