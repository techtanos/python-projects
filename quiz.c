#include <stdio.h>
float calculate(float a, float b) {
    return a * b;
}
int main() {
    float result = calculate(3.0, 4.0);
    printf("Result: %.1f\n", result);
    for(int i = 0; i < 5; i++) {
        printf("i = %d\n", i);
}
    return 0;
}
