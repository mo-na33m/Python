input("Welcome to the computer quiz. ")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("GOODBYE! ")
    quit()
else:
    print("Okay please answer the following 5 questions. GOOD LUCK :) ")
score = 0

answer = input("Question 1 - What 5 * 5? ")
if answer.lower() == "25":
    print("Correct")
    score += 1
else:
    input("Incorrect")

answer = input("Question 2 - What 5 * 1? ")
if answer.lower() == "5":
    print("Correct")
    score += 1
else:
    input("Incorrect")

answer = input("Question 3 - What 4 * 0? ")
if answer.lower() == "0":
    print("Correct")
    score += 1
else:
    input("Incorrect")

answer = input("Question 4 - What 3 * 3? ")
if answer.lower() == "9":
    print("Correct")
    score += 1
else:
    input("Incorrect")

answer = input("Question 5 - What 10 * 7? ")
if answer.lower() == "70":
    print("Correct")
    score += 1
else:
    input("Incorrect")

print("You got " + str(score) + " out of 5 questions correct! ")
print("You got " + str((score/5) * 100) + "%.")
print("Thanks for playing. GOODBYE! ")
input('Press ENTER to exit')









