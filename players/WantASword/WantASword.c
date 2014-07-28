#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void output(char p){
    putchar(p);
    exit(0);
}

int main(int argc, char **argv){
    srand(time(NULL) + 100);
    if(argc == 1) output('S');
    // get sharpness of self+opponent
    int my_sharp = 0, opp_sharp = 0;
    char *p = argv[1];
    while(*p != ','){
        if(*p == 'S') ++my_sharp;
        else if(*p == 'P') --my_sharp;
        ++p;
    }
    ++p;
    while(*p != 0){
        if(*p == 'S') ++opp_sharp;
        else if(*p == 'P') --opp_sharp;
        ++p;
    }
    if(opp_sharp == 0){
        if(my_sharp == 0) output('S');
        else if(rand() % 3) output('S');
        else output('P');
    }else if(opp_sharp < 5){
        if(my_sharp == 0){
            if(rand() % 2) output('S');
            else output('B');
        }else{
            if(rand() % 2) output('S');
            else if(rand() % 2) output('B');
            else output('P');
        }
    }else{
        if(my_sharp == 0) output('S');
        else output('P');
    }
    return 0xDEAD;
}