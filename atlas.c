#include <stdio.h>
#include <math.h>
float evaluate(float x) {
    return 2 * x * x + 3 * x - 5;
}

float derivative_approx(float x) {
    float h = 0.0001;
    return (evaluate(x + h) - evaluate(x)) / h;
}
int main() {
    float x;
    printf("Project Atlas v0.1\n");
    printf("Discipline. Execution. No excuses.\n\n");
    printf("Enter x: ");
    scanf("%f",&x);
    printf("f(%.2f) = %.4f\n", x, evaluate(x));
    printf("f'(%.2f) = %.4f\n", x, derivative_approx(x));
    return 0;
}
