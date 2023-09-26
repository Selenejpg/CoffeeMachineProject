from Menu import menu
from Menu import resources

def print_report(total_costs):
    for resource, quantity in resources.items():
        if resource in ["water", "coffee", "milk"]:
            print(f"{resource}: {quantity} ml")
        else:
            print(f"{resource}: {quantity}")
    print(f"Money: ${total_costs:.2f}")

def process_coffee_order(coffee_choice):
    ingredients_needed = menu[coffee_choice]["ingredients"]
    cost = menu[coffee_choice]["cost"]
    
    insufficient_resource = False

    for ingredient, quantity in ingredients_needed.items():
        if resources.get(ingredient, 0) < quantity:
            print(f"Sorry, there is not enough {ingredient}.")
            insufficient_resource = True

    if insufficient_resource:
        return False

    print(f"The cost of {coffee_choice} is ${cost:.2f}")
    return cost

def insert_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))  # $0.25
    dimes = int(input("How many dimes?: "))        # $0.10
    nickels = int(input("How many nickels: "))    # $0.05
    pennies = int(input("How many pennies: "))    # $0.01

    total_inserted_quarters = 0.25 * quarters
    total_inserted_dimes = 0.10 * dimes
    total_inserted_nickels = 0.05 * nickels
    total_inserted_pennies = 0.01 * pennies

    total_inserted = (
        total_inserted_quarters
        + total_inserted_dimes
        + total_inserted_nickels
        + total_inserted_pennies
    )
    return round(total_inserted, 2)

def serve_coffee(coffee_choice, cost, ingredients_needed):
    total_inserted = insert_coins()
    
    if total_inserted >= cost:
        change = total_inserted - cost
        print(f"Here is ${change:.2f} dollars in change.")

        for ingredient, quantity in ingredients_needed.items():
            resources[ingredient] -= quantity

        print(f"Here is your {coffee_choice} ☕. Enjoy!")
    else:
        print("Sorry, that's not enough money. Money refunded.")

def coffee_machine():
    coffee_machine_status = "on"
    total_costs = 0.0

    while coffee_machine_status == "on":
        coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")

        if coffee_choice in ["espresso", "latte", "cappuccino"]:
            cost = process_coffee_order(coffee_choice)
            if cost:
                serve_coffee(coffee_choice, cost, menu[coffee_choice]["ingredients"])
                total_costs += cost
        elif coffee_choice == "off":
            coffee_machine_status = "off"
            print("Coffee machine is turning off.")
        elif coffee_choice == "report":
            print_report(total_costs)
        else:
            print("Invalid input. Please choose from 'espresso', 'latte', 'cappuccino', 'off', or 'report'.")

coffee_machine()
