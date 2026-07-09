#include <stdio.h>

int main() {
    float mass, accel, time;
    
    // Get inputs from user
    printf("Enter mass (kg): ");
    scanf("%f", &mass);
    
    printf("Enter desired acceleration (m/s2): ");
    scanf("%f", &accel);
    
    printf("Enter time (seconds): ");
    scanf("%f", &time);
    
    // Calculate results
    float force = mass * (9.8 + accel);
    float velocity = accel * time;
    float distance = 0.5 * accel * time * time;
    
    // Print results
    printf("Force needed: %.2f N\n", force);
    printf("Final velocity: %.2f m/s\n", velocity);
    printf("Distance covered: %.2f m\n", distance);
    
    return 0;
}
