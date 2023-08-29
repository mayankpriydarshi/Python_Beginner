print("Welcome the tip calculator")
bill = float(input("What is the total bil?₹ "))
tip = int(input("How much tip would you like to give? "))
people = int(input("How many people to split bill? "))
tip_as_percent = tip / 100
total_tip_amount = tip_as_percent * bill
total_bill = total_tip_amount + bill
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay ₹{final_amount}")
