#include <stdio.h>
float calculate_energy(float payload, float speed, float time) {
   return payload * 5 + speed * 0.8 + time * 1.2;
}
int main() {
    float energy1 = calculate_energy(2.5, 10, 20);
    float energy2 = calculate_energy(0.5, 5, 15);
    float energy3 = calculate_energy(4.0, 12, 25);

    printf("Flight 1: %.1f wh\n", energy1);
    printf("Flight 2: %.1f wh\n", energy2);
    printf("Flight 3: %.1f wh\n", energy3);
    return 0;
}
