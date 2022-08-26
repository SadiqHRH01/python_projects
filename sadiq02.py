
age = input("what is your current age? ")

age = int(age)

years_left = 90 - age
days_left = years_left * 365
weeks_left = years_left * 52
month_left = years_left * 12

total = f"You have {days_left}, {weeks_left} weeks, months {month_left}"
print(total)
