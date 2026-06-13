#include <stdio.h>
#include <string.h>

struct Drone {
    char name[20];
    float mass;
    float speed;
    float altitude;
};

int main() {
    struct Drone d1, d2, d3;
    
    strcpy(d1.name, "Eagle-1");
    d1.mass = 2.5;
    d1.speed = 10;
    d1.altitude = 100;
    
    strcpy(d2.name, "Eagle-2");
    d2.mass = 3.7;
    d2.speed = 15;
    d2.altitude = 200;
    
    strcpy(d3.name, "Eagle-3");
    d3.mass = 9.9;
    d3.speed = 20;
    d3.altitude = 50;
    
    printf("%s: mass=%.1fkg, force=%.1fN\n", d1.name, d1.mass, d1.mass*9.8);
    printf("%s: mass=%.1fkg, force=%.1fN\n", d2.name, d2.mass, d2.mass*9.8);
    printf("%s: mass=%.1fkg, force=%.1fN\n", d3.name, d3.mass, d3.mass*9.8);
    
    return 0;
}
