.PHONY: clean

test:
	./CavemanDuels
	./buildscores.sh

CavemanDuels: src/*.cpp src/*.hpp
	g++ -std=c++11 src/*.cpp src/*.hpp -o CavemanDuels -pthread

clean:
	-rm CavemanDuels out.txt
