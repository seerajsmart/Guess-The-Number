import random

winNum = random.randint(0, 20)

print("I'm thinking of a number in between 0 and 20, what is it?")

playing = True

while playing:
    guess = int(input())
    if guess > winNum:
        print("Too high! Guess lower")
    elif guess < winNum:
        print("Too low! Guess higher!")
    elif guess == winNum:
        print("GG You won!")