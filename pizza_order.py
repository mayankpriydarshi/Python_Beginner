print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
isSmall = False
if size in ["s", "S"]:
    bill += 15
    isSmall = True
elif size in ["m", "M"]:
    bill += 20
elif size in ["l", "L"]:
    bill += 25
if add_pepperoni in ["y", "Y"]:
    if isSmall:
        bill += 2
    else:
        bill += 3
if extra_cheese in ["y", "Y"]:
    bill += 1
print(f"Your final bill is: ${bill}.")
