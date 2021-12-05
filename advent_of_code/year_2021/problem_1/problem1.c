#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE *fp = fopen("input.txt", "r");
    int count = 0; /* Want to count the number of times the depth of the water increases */
    int current_num;
    int previous_num;
    if (fp == NULL)
    {
        printf("Error opening file");
        exit(1);
    }

    while (fscanf(fp, "%d", &current_num) == 1)
    {
        if (current_num > previous_num){
            count += 1;
        }
        previous_num = current_num;
    }
    printf("Number of increases in depth is: %d", count);
}