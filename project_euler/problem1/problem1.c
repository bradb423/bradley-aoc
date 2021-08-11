#include <stdio.h>

int main(void) {
    unsigned int total = 0;

    for (unsigned int i = 3; i < 1000; i += 1){
        if ((i%3 == 0) || (i%5==0)){
            total += i;
        }
    }

    printf("The solution is %u", total);
}