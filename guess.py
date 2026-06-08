import random

top_secret = random.randint(1, 20)
tries = 0
max_tries = 5
won = False

while tries < max_tries:
    guess = int(input("Guess the number (1-20): "))
    tries = tries + 1

    if guess < top_secret:
        print("Too low, try again.")
    elif guess > top_secret:
        print("Too high, try again.")
    else:
        print("You got it in", tries, "tries!")
        won = True
        break

if not won:
    print("You lost. The number was", top_secret)
