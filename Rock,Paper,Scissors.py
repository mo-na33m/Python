import random

user_wins = 0
comp_user = 0
draw = 0

options = ["rock", "paper", "scissors"]

print("Welcome to Rock Paper Scissors. You will go against the computer. ENJOY! ")

while True:
    user_input = input("Type in rock/paper/scissors or Q to Quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    r_number = random.randint(0, 2)
    # rock = 0 paper = 1 scissors = 2
    comp_pick = options[r_number]
    print("Computer Picked", comp_pick)

    if user_input == "rock" and comp_pick == "scissors":
        print("You Won!")
        user_wins += 1

    elif user_input == "paper" and comp_pick == "rock":
        print("You Won!")
        user_wins += 1

    elif user_input == "scissors" and comp_pick == "paper":
        print("You Won!")
        user_wins += 1

    elif user_input == "scissors" and comp_pick == "scissors":
        print("A Draw")
        draw += 1

    elif user_input == "paper" and comp_pick == "paper":
        print("A Draw")
        draw += 1

    elif user_input == "rock" and comp_pick == "rock":
        print("A Draw")
        draw += 1

    else:
        print("You Lost!")
        comp_user += 1

print("You Won", user_wins, "times. ")
print("The Computer Won", comp_user, "times. ")
print("Games Drawn", draw, "times. ")
print("Thanks for playing. GOODBYE!")


