.PHONY: clean

test:
	./CavemanDuels
	./buildscores.sh

CavemanDuels: src/*.cpp
	g++ -std=c++11 src/*.cpp -pthread -o CavemanDuels

clean:
	-rm CavemanDuels out.txt
