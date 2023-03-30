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
money = 0

def resources_check(ingredients_order):
    are_there_enough_ingredients = True
    for item in ingredients_order:
        if ingredients_order[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            are_there_enough_ingredients =  False
    return are_there_enough_ingredients


def cash_or_card():
    payment_method = input("How would you like to pay, type 'cash' or 'card'")
    if payment_method == "cash":
        print("Please insert coins:")
        total = int(input("How many dollars:")) * 1.0 + int(input("How many quarters: ")) * 0.25 + int(input("How many dimes: ")) * 0.1 + int(input("How many nickles: ")) * 0.05
        return total
    elif payment_method == 'card':
        payment_by_card = float(input(f"Please pay {choice['cost']}$: "))
        return payment_by_card

def tranzaction(money_in, order_price):
    if money_in >= order_price:
        change = round(money_in - order_price, 2)
        print(f"Here is your change = ${change}")
        global money
        money += order_price
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def coffe(coffe_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Your {coffe_name} is ready!")

machine_on_off = True
print("☕ Hot Beverage")


# get order
while machine_on_off:
    order = input("What would you like? (espresso/latte/cappuccino):")
    if order == "off":
     machine_on_off = False
    elif order == "report":
        print(f"""
    Water: {resources["water"]}ml
    Milk: {resources["milk"]}ml
    Coffee: {resources["coffee"]}g
    Money: ${money}
    """)
    else:
        choice = MENU[order]
        if resources_check(choice["ingredients"]):
           payment = cash_or_card()
           if tranzaction(payment, choice["cost"]):
               coffe(order, choice["ingredients"])





