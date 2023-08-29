age = input("What is your current age? ")
age_int = int(age)
remaining_year = 90 - age_int
day = remaining_year * 365
week = remaining_year * 52
month = remaining_year * 12
print(f"You have {day} days, {week} weeks, and {month} months left.")
