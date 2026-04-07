#Number guessing


import random

low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))

number = random.randint(low, high)

while True:
    guess = int(input(f"Guess a number between {low} and {high}: "))

    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print("🎉 Correct! You guessed it.")
        break