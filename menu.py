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

    i = 1
    menu_keys_indexes = {}
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_keys_indexes[i] = key
        i += 1

    menu_selection = input("Enter a number to select a menu category: ")
    if not menu_selection.isdigit():
        print(f"Please enter a valid number. Received {menu_selection}.\n")
        continue

    menu_selection = int(menu_selection)
    if menu_selection > len(menu) or menu_selection < 1:
        print(
            f"{menu_selection} is not a valid menu option. Please enetr a valid number.\n"
        )
        continue

    sub_menu = menu[menu_keys_indexes[menu_selection]]

    print("Item # | Item name                | Price  ")
    print("-------|--------------------------|--------")

    i = 1
    sub_menu_keys_indexes = {}
    for key, value in sub_menu.items():
        if type(value) == dict:
            for key2, value2 in value.items():
                name = f"{key} - {key2}"
                sub_menu_keys_indexes[i] = {
                    "Name": name,
                    "Price": value2,
                    "Quantity": 0,
                }

                item_spaces = 6
                if i > 10:
                    item_spaces = 5

                name_spaces = 25 - len(name)
                print(f"{i}{' ' * item_spaces}| {name}{' ' * name_spaces}| ${value2}")
                i += 1
            continue

        item_spaces = 6
        if i > 10:
            item_spaces = 5
        name_spaces = 25 - len(key)
        print(f"{i}{' ' * item_spaces}| {key}{' ' * name_spaces}| ${value}")

        sub_menu_keys_indexes[i] = {
            "Name": key,
            "Price": value,
            "Quantity": 0,
        }
        i += 1

    item_number = input(
        "Enter a number to select an item. An invalid number will default to 1: "
    )
    if (
        not item_number.isdigit()
        or int(item_number) > len(sub_menu_keys_indexes)
        or int(item_number) < 1
    ):
        item_number = 1

    item_number = int(item_number)
    order = sub_menu_keys_indexes[item_number]
    item_name = order["Name"]

    quantity = input(f"How many items of {item_name} would you like? ")
    if not quantity.isdigit():
        quantity = 1

    quantity = int(quantity)
    order["Quantity"] = quantity

    order_list.append(order)

    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        match keep_ordering.lower():
            case "yes" | "y":
                break
            case "no" | "n":
                place_order = False
                break
            case _:
                print("Please enter (Y)es or (N)o")

print("Item name                | Price   | Quantity ")
print("-------------------------|---------|----------")

prices = []
for order in order_list:
    item_name = order["Name"]
    price = order["Price"]
    quantity = order["Quantity"]

    prices.append(price * quantity)
    price_spaces = 3
    if price > 10:
        price_spaces = 2

    name_spaces = 25 - len(item_name)
    print(f"{item_name}{' ' * name_spaces}| ${price}{' ' * price_spaces}| {quantity}")

print(f"The total order costs ${sum(prices)}")
