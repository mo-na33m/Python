import random

print("Welcome to the Guess The Random Number Game! ")
tr = input("Type a number: ")

if tr.isdigit():
    tr = int(tr)
    if tr <= 0:
        print("Please type a number larger than 0 next time. Thanks for playing! ")
        quit()
else:
    print("Please type a number next time. Thanks for playing! ")
    quit()

rn = random.randint(0, tr)
guesses = 0

while True:
    guesses += 1
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please type a number next time. Thanks for playing! ")
        continue

    if guess == rn:
        print("You got it ")
        break
    elif guess > rn:
        print("You were above the number! ")
    else:
        print("You were below the number! ")

print("Bravo you did it in", guesses, "guesses. Thanks for playing! ")
input('Press ENTER to exit')

