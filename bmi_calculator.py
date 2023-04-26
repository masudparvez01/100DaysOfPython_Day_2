# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

height1 = float(height)
weight1 = float(weight)
bmi_formula = int(weight1/(height1*height1))

bmi_result = str(bmi_formula)

print("Your BMI result is: " + bmi_result)

print("Thank You!!!")