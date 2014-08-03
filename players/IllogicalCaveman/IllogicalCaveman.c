#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void output(char p){
    putchar(p);
    exit(0);
}

int main(int argc, char **argv){
    srand(time(NULL) + 0xF00D);
    if(argc == 1) output('S');
    // get sharpness of self+opponent
    int my_sharp = 0, opp_sharp = 0;
    char *p = argv[1], *q;
    while(*p != ','){
        if(*p == 'S') ++my_sharp;
        else if(*p == 'P') --my_sharp;
        ++p;
    }
    q = p++;
    while(*p != 0){
        if(*p == 'S') ++opp_sharp;
        else if(*p == 'P') --opp_sharp;
        ++p;
    }
    if(opp_sharp == 0){
        if(my_sharp == 0) output('S');
        else if(rand() % 10 < 6) output('P');
        else output('S');
    }else if(my_sharp == 0){
        if(rand() % 10 < 6) output('S');
        else output('B');
    }else{
        if(rand() % 10 < 6){
            switch((-1)[q]){
                case 'B': output('P');
                case 'P': output('S');
                case 'S': output('B');
            }
        }else{
            if((-1)[p] == (-2)[p]){
                switch((-1)[p]){
                    case 'S': output('P');
                    case 'B': output('S');
                    case 'P': output('B');
                }
            }else if(rand() % 10 < 6){
                output('P');
            }else output('B');
        }
    }
    return 0xDEAD;
}