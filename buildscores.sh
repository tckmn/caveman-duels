#!/bin/bash

ENTRYCOUNT=17

cat out.txt | sed "s/^[0-9]\+ //" > out2.txt

for (( i=0; i<$((ENTRYCOUNT)); i++ ))
do
  grep -c "\b$i\b" out2.txt >> scores.txt
done

echo "Score   Player"
paste scores.txt playerlist.txt      \
  | expand                           \
  | sed "s/^\([0-9]* *\).*[\/ ]/\1/" \
  | sed "s/\.[^.]*$//"               \
  | sort -nr
echo "*(this leaderboard was auto-magically generated)*"

rm out2.txt
rm scores.txt
