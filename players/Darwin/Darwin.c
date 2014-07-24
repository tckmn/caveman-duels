#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

/* magic numbers */
#define SWORD_SHARPNESS 5
#define PROGRAM_DIM 4 /* polynomial order + 1 */
#define DEFAULT_FILENAME "players/Darwin/program"

typedef double real;
typedef real program[PROGRAM_DIM][PROGRAM_DIM];
typedef program caveman_brain[3];

typedef char action; /* S, B or P */
/* encodes a pair of actions */
#define ACTION_PAIR(a1, a2) (((int)(a1) << (sizeof(action) * 8)) | (a2))

real eval_program(const program p, double x, double y) {
    real v = 0;
    int i, j;

    for (i = 0; i < PROGRAM_DIM; ++i) {
        real w = 0;
        for (j = 0; j < PROGRAM_DIM; ++j)
            w = x * w + p[i][j];
        v = y * v + w;
    }

    return fmax(v, 0.0);
}
void read_program(FILE* f, program p) {
    int i, j;
    for (i = 0; i < PROGRAM_DIM; ++i) {
        for (j = 0; j < PROGRAM_DIM; ++j) {
            double v;
            fscanf(f, "%lg", &v);
            p[i][j] = v;
        }
    }
}

int blunt(int* s) {
    int temp = *s;
    if (temp)
        --*s;
    return temp;
}
void sharpen(int* s) { ++*s; }
/* takes two sharpness/action pairs and updates the sharpness accordingly.
 * returns negative value if first caveman wins, positive value if second
 * caveman wins and 0 otherwise. */
int act(int* s1, action a1, int* s2, action a2) {
    switch (ACTION_PAIR(a1, a2)) {
        case ACTION_PAIR('B', 'B'): return 0;
        case ACTION_PAIR('B', 'S'): sharpen(s2); return 0;
        case ACTION_PAIR('B', 'P'): return blunt(s2) >= SWORD_SHARPNESS ? 1 :
                                                                          0;
        case ACTION_PAIR('S', 'B'): sharpen(s1); return 0;
        case ACTION_PAIR('S', 'S'): sharpen(s1); sharpen(s2); return 0;
        case ACTION_PAIR('S', 'P'): sharpen(s1); return *s2 > 0 ? 1 : 0;
        case ACTION_PAIR('P', 'B'): return blunt(s1) >= SWORD_SHARPNESS ? -1 :
                                                                          0;
        case ACTION_PAIR('P', 'S'): sharpen(s2); return *s1 > 0 ? -1 : 0;
        case ACTION_PAIR('P', 'P'): {
            int t1 = blunt(s1), t2 = blunt(s2);
            if (t1 >= SWORD_SHARPNESS && t2 < SWORD_SHARPNESS)
                return -1;
            else if (t2 >= SWORD_SHARPNESS && t1 < SWORD_SHARPNESS)
                return 1;
            else
                return 0;
        }
    }
}
/* processes a pair of strings of actions */
int str_act(int* s1, const char* a1, int* s2, const char* a2) {
    for (; *a1 && *a2; ++a1, ++a2) {
        int winner = act(s1, *a1, s2, *a2);
        if (winner)
            return winner;
    }
    return 0;
}

double frandom() { return (double)rand() / RAND_MAX; }

/* chooses an action based on self and opponent's sharpness */
action choose_action(const caveman_brain b, int s1, int s2) {
    double v[3];
    double sum = 0;
    double r;
    int i;
    for (i = 0; i < 3; ++i) {
        v[i] = eval_program(b[i], s1, s2);
        sum += v[i];
    }
    r = frandom() * sum;
    if (r <= v[0])
        return 'B';
    else if (r <= v[0] + v[1])
        return 'S';
    else
        return 'P';
}

/* portable tick-count for random seed */
#ifdef _WIN32
#include <Windows.h>
unsigned int tick_count() { return GetTickCount(); }
#else
#include <sys/time.h>
unsigned int tick_count() {
    struct timeval t;
    gettimeofday(&t, NULL);
    return 1000 * t.tv_sec + t.tv_usec / 1000;
}
#endif

int main(int argc, const char* argv[]) {
    const char* filename = DEFAULT_FILENAME;
    const char *a1, *a2;
    FILE* f;
    caveman_brain b;
    int s1 = 0, s2 = 0;
    int i;

    srand(tick_count()); rand();

    a1 = argc > 1 ? argv[1] : "";
    if (*a1) {
        a2 = strchr(a1, ',');
        if (a2 == NULL) {
            printf("invalid input!\n");
            return 1;
        }
        ++a2;
    } else
        a2 = a1;

    if (argc > 2)
        filename = argv[2];

    f = fopen(filename, "r");
    if (f == NULL) {
        printf("failed to open `%s'\n", filename);
        return 1;
    }
    for (i = 0; i < 3; ++i)
        read_program(f, b[i]);
    fclose(f);

    str_act(&s1, a1, &s2, a2);
    printf("%c\n", choose_action(b, s1, s2));

    return 0;
}