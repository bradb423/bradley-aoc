#include <stdio.h>

int main(void){
    long x = 1;
    long y = 2;
    long z = 3;
    long result = 2;
    long const LIMIT = 4000000;

    while (z < LIMIT){
        z = x+y;
        x = y;
        y = z;
        if (z%2 == 0){
            result += z;
        }
    }
    printf("The result is: %u", result);
}