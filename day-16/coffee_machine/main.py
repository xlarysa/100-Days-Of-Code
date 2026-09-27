from importlib.resources import is_resource

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    order = input(f"What would you like? ({menu.get_items()}): ").lower()
    if order == "off":
        is_on = False
    elif order == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if drink is not None:
            if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)


