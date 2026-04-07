#guess game



import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number (1-100): "))

    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print("Correct! You guessed it.")
        break