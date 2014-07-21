# Caveman Duels (or: Me poke you with sharp stick)

Caveman mad. Other caveman take stick but stick was for me. Caveman fight!

---

## Description

Caveman need sharp stick to stab other caveman. Other caveman also try to stab with sharp stick. Caveman can sharpen stick, poke with stick, or block poky sticks.

If caveman poke other caveman with sharp stick, other caveman run away and me victory. But if other caveman smartly blocking when me poking, nothing happen except my stick become blunt and me need to sharpen again.

Caveman lazy. Also, caveman dumb. Caveman no know what to do, so caveman need fancy techno computer program to tell caveman what to do.

## Input

Your program's input will be a history of the events that have happened, where `S` stands for sharpen (i.e. the caveman sharpened his stick), `P` stands for poke, and `B` stands for block. The input will be a history of both sides (you and the opponent), so your and the opponenent's moves will be separated with a comma (`,`).

Example input:

    SPB,SBB
    
This means that the player sharpened his/her stick, then poked, then blocked, and the opponenet sharpened, then blocked, then blocked again.

## Output

The output is very similar to the input (because the caveman is not very smart). Your program should output `S` to sharpen, `P` for poke, and `B` for block. Only the first character of output will be taken into account, and any other input will be treated as a no-op (i.e. pass).

- **`S`: sharpen**

    When sharpening, the caveman's stick's sharpness goes up by 1 and the stick gets 1 extra poke. Each poke reduces the stick's sharpness by 1, and if the stick's sharpness is 0, it's too dull to poke with. Sharpness starts at 0. If sharpness gets to 5, the stick becomes a sword! (See below.)
    
    If the opponenet pokes while you are sharpening, the opponent wins! So be cave-ful. (Careful; caveman like making ban puns.)
    
- **`P`: poke**

    When poking, the caveman's stick's sharpness goes down by 1 and you poke your opponent! If your opponent is sharpening, you win! If the opponent is poking, your stick hits your opponent's stick and they both get duller (by 1 "sharpness unit"). If the opponent is blocking, nothing happens.
    
    If you poke when your stick's sharpness is 5, your stick becomes a sword and you *always* win! (Unless your opponent also has a sword; in that case, they both become duller.)
    
- **`B`: block**

    When you block, nothing happens when your opponent pokes. If your opponent is not poking, block does nothing.
    
    Block does not protect against sword!
    
## Rules and constraints

Additional rules are:

- Your program can read and write files in its *own* folder (no stealing!) if you want to save data, but you can't access anything outside of it (and cavemen don't have internet connection out in the wilderness).
- Cavemen are fair: One program can not have code specific for another program, and programs can not help each other. (You may have multiple programs, but they can't interact with each other in any way.)
- The caveman judge is not patient. If the cavemen take more than 100 turns each to decide a winner, the judge gets bored and both cavemen lose.

If your program breaks a rule or doesn't follow the specification, the program is disqualified, removed from `playerlist.txt`, and all duels restart from the beginning. If your program is disqualified, the caveman leader (me!) will comment on your program's post and explain why. If you aren't breaking any rules, your program will be added to the leaderboard. (If your program is not on the leaderboard, there is no explanatory comment on your post, and you posted your program before the "Last updated" time below, tell the caveman leader! Maybe he forgot it.)

In your post, please include:

- A name.
- A shell command to run your program (ex. `java MyBot.java`, `ruby MyBot.rb`, `python3 MyBot.py`, etc.).
 - Note: input will be appended to this as a command line argument.
 - The cavemen use Ubuntu 14.04, so make sure your code works (freely) on it.
- A version number, if your code works differently on different versions of your chosen language.
- Your code (obviously).
- How to compile the code, if necessary.

## Controller code / testing, example bot

The caveman leader wrote the control code in C++, and [posted it on a Github repo](https://github.com/KeyboardFire/caveman-duels). You can run and test your program there.

A very, *very* simple program (1 line!) is also posted in the answers below.

## Scoring and leaderboard

Scoring is easy. Whichever caveman wins gets a point. The caveman with the most points after 10 duels against every other caveman becomes the new caveman leader!

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
