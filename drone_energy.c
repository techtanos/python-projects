#include <stdio.h>

int main() {
    float payload = 7;
    float flight_time = 7;
    float speed = 7;
    
    float energy = payload * 5 + flight_time * 1.2 + speed * 0.8;
    
    printf("Energy consumed: %.1f Wh\n", energy);
    
    return 0;
}
