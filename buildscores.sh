#!/bin/bash

set -- `wc -l playerlist.txt`
ENTRYCOUNT=$1

cut -d ' ' -f 2,3,4 out.txt > out2.txt

for (( i=0; i<$((ENTRYCOUNT)); i++ ))
do
  cat out2.txt | tr ' ' $'\n' | grep -c "^$i$" >> scores.txt
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
