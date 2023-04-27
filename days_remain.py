# 🚨 Don't change the code below 👇
age = input("What is your current age?\nType your current age: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

current_age = int(age)

days_remain = ((90 * 365) - (current_age * 365))
weeks_remain = ((90 * 52) - (current_age * 52))
months_remain = ((90 * 12) - (current_age * 12))

message = f"You have {days_remain} days, {weeks_remain} weeks, and {months_remain} months left. "

print(message)