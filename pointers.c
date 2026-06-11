#include <stdio.h>
int main() {
    int x = 10;
    int *p = &x;
    printf("Value of x: %d\n", x);
    printf("Address of x: %p\n", p);
    printf("Value through pointer: %d\n", *p);

    *p = 99;
    printf("x is now: %d/n", x);

    return 0;
}
