height = float(input("Your height in m: "))
weight = float(input("Your weight in kg: "))

bmi = round((weight / height**2), 1)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif 18.5 < bmi < 24.9:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25.0 < bmi < 29.9:
    print(f"Your BMI is {bmi}, you are overweight.")
else:
    print(f"Your BMI is {bmi}, you are obese.")
