n1 = "YK"
height_n1 = 2
weight_kg1 = 90

n2 = "YK's sister"
height_n2 = 1.8
weight_kg2 = 70

n3 = "YK's brother"
height_n3 = 2.5
weight_kg3 = 160


def bmi(name, height, weight):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return name + " is Underweight"
    elif 18.5 < bmi < 24.9:
        return name + " is Normal weight"
    elif 25 < bmi < 29.9:
        return name + " is Overweight"
    elif bmi > 30:
        return name + " is Obesity"

result1 = bmi(n1, height_n1, weight_kg1)
result2 = bmi(n2, height_n2, weight_kg2)
result3 = bmi(n3, height_n3, weight_kg3)

print(result1)
print(result2)
print(result3)