#BMI calculate function
def bmi(name, height, weight):
    bmi = weight / (height ** 2)
    print("BMI: ", bmi)
    if bmi < 18.5:
        print(name + " is Underweight")
    elif 18.5 < bmi < 24.9:
        print(name + " is Normal weight")
    elif 25 < bmi < 29.9:
        print(name + " is Overweight")
    elif bmi > 30:
        print(name + " is Obesity")

#input
n = input("Enter your name: ")
w = float(input("Enter your weight: "))
h = float(input("Enter your height: "))
#output
bmi(n, h, w)

