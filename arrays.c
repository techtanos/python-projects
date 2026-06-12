#include <stdio.h>
int main() {
    float drone_mass[5] = {1.5, 2.0, 3.0, 4.5, 2.8};
    for(int i = 0; i < 5; i++){
        float force = drone_mass[i] * 9.8;
        printf("Drone %d: %.1f Newtons\n", i+1, force);
    }
    return 0;
}
