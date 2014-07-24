#!/bin/bash

ENTRYCOUNT=17

cat out.txt | sed "s/^[0-9]\+ //" > out2.txt

for (( i=0; i<$((ENTRYCOUNT)); i++ ))
do
  grep -c "\b$i\b" out2.txt >> scores.txt
done

paste scores.txt playerlist.txt

rm out2.txt
rm scores.txt
