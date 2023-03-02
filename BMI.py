# BMI Calculator
# Formula: mass (kg) / height2 (m)


name = input("Hi what is your name: ")
persons_weight = float(input("Please enter your weight (Kg): "))
persons_height = float(input("Please enter you height (M): "))

bmi = persons_weight / (persons_height * persons_height)

if bmi > 0:
    if bmi < 16:
        print("Hi" + name + " you are Severe Thinness")
    elif bmi < 17:
        print("Hi" + name + " you are Moderate Thinness")
    elif bmi < 18.5:
        print("Hi" + name + " you are Mild Thinness")
    elif bmi < 25:
        print("Hi" + name + " you are Normal")
    elif bmi < 30:
        print("Hi" + name + " you are Overweight")
    elif bmi < 35:
        print("Hi" + name + " you are Obese Class 1")
    elif bmi < 40:
        print("Hi" + name + " you are Obese Class 2")
    elif bmi > 40:
        print("Hi" + name + " you are Obese Class 3")
    else:
        print("Invalid")


print(bmi)
input('Press ENTER to exit')


