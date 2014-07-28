/* vi: ts=2
 * The Semi-Patient Swordsmith.
 * Caveman poke
 * Input: SPS,SBB (me,opp)
 */

#include <stdio.h>
#include <string.h>

#define ROUNDS 100
#define SWORD 5

unsigned statusof(char **ptr, unsigned *ctr)
{
    unsigned c = 0;
    *ctr = 0;
    while (**ptr && **ptr != ',')
            switch (*(*ptr)++) {
                    case 'S': c += 1; *ctr = 0; break;
                    case 'P': if (c) c -= 1; *ctr = 0; break;
                    case 'B': *ctr += 1; break;
            }
    return c;
}

int main(int argc, char **argv)
{
    unsigned me, opp;
    unsigned mbc, obc;
    unsigned rds;
    char act;
    if (!argv[0]) return 3;
    if (!argv[1] || !*argv[1]) argv[1] = ",";
    rds = strlen(argv[1]) >> 1;
    me = statusof(&argv[1], &mbc);
    ++argv[1];
    opp = statusof(&argv[1], &obc);

    if (me > ROUNDS - rds || me >= SWORD || opp >= SWORD)
            act = 'P';
    else if (!opp)
            if (rds % 5 > me)
                    act = 'P';
            else
                    act = 'S';
    else if (opp > 2 && SWORD - opp > rds % 5)
            act = 'P';
    else if (mbc > me + 1)
            act = 'S';
    else
            act = 'B';

    if (!me && act == 'P') act = 'S';
    if (rds == ROUNDS && act == 'S') act = 'B';
    putc(act, stdout);
    putc('\n', stdout);
}