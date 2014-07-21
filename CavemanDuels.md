# Caveman Duels (or: Me poke you with sharp stick)

Caveman mad. Other caveman take stick but stick was for me. Caveman fight!

---

## Description

Caveman need sharp stick to stab other caveman. Other caveman also try to stab with sharp stick. Caveman can sharpen stick, poke with stick, or block poky sticks.

If caveman poke other caveman with sharp stick, other caveman run away and me victory. But if other caveman smartly blocking when me poking, nothing happen except my stick become blunt and me need to sharpen again.

Caveman lazy. Also, caveman dumb. Caveman no know what to do, so caveman need fancy techno computer program to tell caveman what to do.

## Input

Caveman need to know what happened to know what to do next. Computer no have eyes, but caveman have eyes, so caveman tell program what happen and program tell caveman what to do.

Caveman will give program history of what happen, where `S` stand for sharpen, `P` stand for poke, and `B` stand for block. Caveman give program history of both sides, so history of caveman and history of caveman enemy will be separated by comma (`,`). Example:

    SPB,SBB
    
This mean me sharpen, then poke, then block, and other caveman sharpen, then block, then block again.

## Output

When program tell caveman what to do, output very similar to input (because caveman not very smart). Program says `S` if want caveman to sharpen, `P` for poke, and `B` for block.

- **`S`: sharpen**

    When caveman sharpen, stick sharpness go up by 1 and stick gets 1 extra poke. Each poke reduce stick sharpness by 1, and if stick sharpness is 0 stick is too dull to poke. Stick sharpness starts at 0. If stick sharpness gets to 5, stick become sword! (See below.)
    
    If other caveman poke while sharpening, other caveman win! So be cave-ful. (Careful; caveman like making ban pun.)
    
- **`P`: poke**

    When caveman poke, stick sharpness go down by 1 and caveman poke enemy! If enemy sharpening, caveman win! If enemy poking, stick hits enemy stick and they both get duller by 1. If enemy blocking, nothing happen.
    
    If caveman poke when sharpness is 5, stick become sword and caveman *always* win! (Unless other caveman also have sword, then they both become duller.)
    
- **`B`: block**

    When caveman block, nothing happen when other caveman poke. If other caveman not poking, block does nothing.
    
    Block does not protect against sword!
    
## Rules and constraints

Other things caveman must do:

- Program can read and write file in its *own* folder (no stealing!) if want to save data, but can't access anything outside of it (and caveman no have internet connection out in wilderness).
- Caveman is fair: One program can not have code specific for other program, and 2 program can not help each other. (You can have many program, but program can't interact with other program in any way.)
- Caveman judge not patient. If caveman take more than 100 turn each to stab other caveman, judge get bored and both caveman lose.

If program break rule or no follow specification, program disqualified, removed from `playerlist.txt`, and all duels restart from beginning. If your program disqualified, caveman leader (me!) will comment on your program's post and explain why. If no break any rule, your program be added to leaderboard. (If your program not on leaderboard, no explainy comment on your post, and you posted your program before "Last updated" time below, tell caveman leader! Maybe he forgot it.)

In your post, please include:

- A name.
- A shell command to run your program (example: `java MyBot.java`, `ruby MyBot.rb`, `python3 MyBot.py`, etc.).
 - Note: input will be put after this as command line argument.
 - Caveman's computer has Ubuntu 14.04, so make sure code works (freely) on it.
- A version number, if code works different on different version of language.
- Your code (obviously).
- How to compile code, if necessary.

## Controller code / testing, example bot

Caveman leader wrote control code in C++, and [put it on Github repo](https://github.com/KeyboardFire/caveman-duels). You can run and test program there.

Very very very simple program (1 line!) is also posted in answers below.

## Scoring and leaderboard

Score is easy. Whichever caveman win get point. Caveman with most point after 10 duel against each other caveman become new caveman leader! 

*4 submissions are required before a real leaderboard will appear.*

    +--------------------------+--------+--------------------+
    | Name                     | Points | Last Updated (UTC) |
    +--------------------------+--------+--------------------+
    | Foo                      | 1337   | Jan 01 12:00 PM    |
    | Bar                      | 42     | Apr 01 01:23 AM    |
    | Baz                      | 10     | Dec 15 00:00 AM    |
    | Qux                      | 1      | Feb 29 10:00 AM    |
    +--------------------------+--------+--------------------+
    
Last updated: N/A.
