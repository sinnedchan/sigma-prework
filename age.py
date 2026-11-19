from datetime import date

#Get today's date
today = date.today()
present_day = today.day
present_month = today.month
present_year = today.year

#print(present_day, present_month, present_year)

#Ask for a date and split them into parts so that they can be compared to today's date
user_input = input("Enter your date of birth including dashes (DD-MM-YY): ")
parts = user_input.split("-")

#print(parts)

birth_day = int(parts[0])
birth_month = int(parts[1])
birth_year = int(parts[2])

#Compare each part of the dates to determine whether the user has had their birthday so far this year
age = present_year - birth_year

if present_month < birth_month:
    age = age - 1
elif present_month == birth_month and present_day < birth_day:
    age = age - 1

print("Age:", age)