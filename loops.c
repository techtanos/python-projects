#include <stdio.h>
int main() {
    for(int i = 1; i<= 5; i++) {
        printf("Flight %d\n", i);
    }
    int battery = 100;
    while(battery > 0) {
        printf("Battery: %d%%\n", battery);
        battery = battery - 20;
    }
    printf("Battery dead!\n");
    return 0;
}
