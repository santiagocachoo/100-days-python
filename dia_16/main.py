from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

machine_on = True

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        break

    elif user_choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
        
    else:
        coffee_object = my_menu.find_drink(user_choice)

        it_can_be_done = my_coffee_maker.is_resource_sufficient(coffee_object)

        if it_can_be_done:
            payment = my_money_machine.make_payment(coffee_object.cost)
            if payment:
                my_coffee_maker.make_coffee(coffee_object)





