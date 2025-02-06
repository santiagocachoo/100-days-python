MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
    
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(menu_choice):
    if MENU[menu_choice]["ingredients"]["water"] > resources["water"]:
        print(f"Sorry, there is not enough water")
    elif MENU[menu_choice]["ingredients"]["milk"] > resources["milk"]:
        print(f"Sorry, there is not enough milk")
    elif MENU[menu_choice]["ingredients"]["coffee"] > resources["coffee"]:
        print(f"Sorry, there is not enough coffee")
    else:
        return True

def ask_coins():
    print("Please, insert some coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

    

money = 0

machine_on = True

while machine_on:
    # user choice
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # command to break code
    if user_choice == "off":
        break

    if user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${money}")

    # check if there is enough resources
    if user_choice in MENU:
        enough = check_resources(user_choice)
        if enough:
            user_money = ask_coins()
            if user_money < MENU[user_choice]["cost"]:
                print("Sorry, that's not enough money")
            else:
                if user_money > MENU[user_choice]["cost"]:
                    change = round(user_money - MENU[user_choice]["cost"], 2)
                    print(f"Here is ${change} in change")
                money += MENU[user_choice]["cost"]

                resources["water"] -= MENU[user_choice]["ingredients"]["water"]
                resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]
                resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]

                print(f"Enjoy your {user_choice}")
    else:
        pass
        


