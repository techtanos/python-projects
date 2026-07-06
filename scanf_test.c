#include <stdio.h>

int main() {
    char name[50];
    int age;
    
    printf("Enter your name: ");
    scanf("%s", name);
    
    printf("Enter your age: ");
    scanf("%d", &age);
    
    int days = age * 365;
    
    printf("Hello %s!\n", name);
    printf("You are %d years old.\n", age);
    printf("You have been alive for approximately %d days.\n", days);
    printf("Use them well.\n");
    
    return 0;
}
