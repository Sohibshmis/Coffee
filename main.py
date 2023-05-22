from coffee_data import MENU, resources
# TODO 1.Print report of all coffee machine resources


def report():
    for x in resources:
        print(f"{x}: {resources[x]}")



# TODO 2.Check that the resources to the drink are sufficient

def check_resources(order):

    if MENU[order]["ingredients"]["water"] > resources['water']:
        return "Sorry, there isn't enough water. "
    elif MENU[order]["ingredients"]["milk"] > resources['milk']:
        return "Sorry, there isn't enough milk. "
    elif MENU[order]["ingredients"]["coffee"] > resources['coffee']:
        return "Sorry, there isn't enough coffee. "
    else:
        return payment(order)


def update_resources(order):
    resources['water'] -= MENU[order]["ingredients"]["water"]
    resources['milk'] -= MENU[order]["ingredients"]["milk"]
    resources['coffee'] -= MENU[order]["ingredients"]["coffee"]
    resources['profit'] += MENU[order]["cost"]


# TODO 3.Process coins

def payment(order):
    coins = {
        'Penny': 0.01,
        'Nickel': 0.05,
        'Dime': 0.10,
        'Quarter': 0.25
    }
    quarters = int(input("How many Quarters? ")) * coins["Quarter"]
    dimes = int(input("How many Dimes? ")) * coins["Dime"]
    nickels = int(input("How many Nickels? ")) * coins["Nickel"]
    pennies = int(input("How many Pennies? ")) * coins["Penny"]
    total = quarters + dimes + nickels + pennies

    # TODO 4.Check if the transaction is successful
    if total < MENU[order]["cost"]:
        return f"Sorry, that's not enough money. Money Refunded. "
    update_resources(order)
    return f'Here is {round(total - MENU[order]["cost"], 2)}$ in change.\n Here is your {order}. Enjoy :). '

# TODO 5.Make Coffee


def make_coffee():
    order = input("What would you like? (espresso, latte, cappuccino): ")
    if order == "report":
        report()
        make_coffee()
    print(check_resources(order))
    make_coffee()

make_coffee()

