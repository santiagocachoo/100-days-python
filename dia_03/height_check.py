print("Welcome to the ride")
height = int(input("Enter your height in cm: "))
bill = 0

if height > 120:
    age = int(input("Enter your age: "))
    if age < 12:
        print("Child ticket is $5 dollars")
        bill = 5
    elif age < 18:
        print("Youth ticket is $7 dollars")
        bill = 7
    else:
        print("Adult ticket is $12 dollars")
        bill = 12

    wants_photos = input("Do you want pictures for the ride? Type y for yes and n for no ")
    if wants_photos == "y":
        bill += 3

    print(f"Your total price is ${bill}")
        
else:
    print("Sorry, you must be above 120 cm to enter this ride")