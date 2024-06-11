# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": 0.99,
        "Banana": 0.69,
        "Apple": 0.49,
        "Granola bar": 1.99,
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99,
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49,
            "Vegetarian": 9.49,
        },
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99,
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49,
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49,
        },
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49,
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49,
    },
}

order_list = []

place_order = True
while place_order:
    print("From which menu would you like to order? ")

    for index, key in enumerate(menu.keys(), start=1):
        print(f"{index}: {key}")

    menu_selection = input("Enter a number to select a menu category: ")
    if not menu_selection.isdigit() or not (1 <= int(menu_selection) <= len(menu)):
        print(f"Please enter a valid number. Received {menu_selection}.\n")
        continue

    menu_selection = int(menu_selection)
    sub_menu = menu[list(menu.keys())[menu_selection - 1]]

    print("Item # | Item name                | Price  ")
    print("-------|--------------------------|--------")

    i = 1
    for key, value in sub_menu.items():
        if isinstance(value, dict):
            for key2, value2 in value.items():
                name = f"{key} - {key2}"
                print(f"{i:<7}| {name:<25}| ${value2}")
                i += 1
        else:
            print(f"{i:<7}| {key:<25}| ${value}")
            i += 1

    item_number = input(
        "Enter a number to select an item. An invalid number will default to 1: "
    )
    item_number = int(item_number) if item_number.isdigit() else 1
    item_number = max(1, min(item_number, len(sub_menu)))

    order = list(sub_menu.items())[item_number - 1]
    item_name = order[0]
    price = order[1] if isinstance(order[1], float) else list(order[1].values())[0]

    quantity = input(f"How many items of {item_name} would you like? ")
    quantity = int(quantity) if quantity.isdigit() else 1

    order_list.append({"Name": item_name, "Price": price, "Quantity": quantity})

    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()
        if keep_ordering in {"yes", "y"}:
            break
        elif keep_ordering in {"no", "n"}:
            place_order = False
            break
        else:
            print("Please enter (Y)es or (N)o")

print("Item name                | Price   | Quantity ")
print("-------------------------|---------|----------")

prices = []
for order in order_list:
    item_name = order["Name"]
    price = order["Price"]
    quantity = order["Quantity"]

    prices.append(price * quantity)
    price_spaces = 3 if price > 10 else 2
    name_spaces = 25 - len(item_name)
    print(f"{item_name}{' ' * name_spaces}| ${price}{' ' * price_spaces}| {quantity}")

print(f"The total order costs ${sum(prices)}")
