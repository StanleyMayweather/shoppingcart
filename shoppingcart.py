# Shopping Cart Program
# Each item now includes a quantity field, allowing the user to track how
# many of each item are in the cart.
# Coding starts here...

shopping_cart = []  # Will contain dictionaries like {'name': 'bed', 'price': 150.0, 'quantity': 2}

currency_symbol = "$"

while True:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    action = input("Please enter an action: ")

    if action == "1":
        name = input("What item would you like to add? ")
        price_input = input(f"What is the price of '{name}'? ")
        quantity_input = input(f"How many '{name}' would you like to add? ")

        try:
            price = float(price_input)
            quantity = int(quantity_input)
            shopping_cart.append({
                "name": name,
                "price": price,
                "quantity": quantity
            })
            print(f"'{name}' has been added to the cart.")
        except ValueError:
            print("Invalid price or quantity. Please try again.")

    elif action == "2":
        if not shopping_cart:
            print("Your shopping cart is empty.")
        else:
            print("\nThe contents of the shopping cart are:")
            print("{:<5} {:<15} {:<10} {:<10}".format("No.", "Item", "Price", "Qty"))
            print("-" * 40)
            for index, item in enumerate(shopping_cart, start=1):
                print("{:<5} {:<15} {:<10} {:<10}".format(
                    index,
                    item["name"],
                    f"{currency_symbol}{item['price']:.2f}",
                    item["quantity"]
                ))

    elif action == "3":
        if not shopping_cart:
            print("There are no items to remove.")
        else:
            remove_input = input("Which item number would you like to remove? ")
            try:
                index_to_remove = int(remove_input) - 1
                if 0 <= index_to_remove < len(shopping_cart):
                    removed_item = shopping_cart.pop(index_to_remove)
                    print(f"'{removed_item['name']}' has been removed from the cart.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Please enter a valid number.")

    elif action == "4":
        total = 0
        for item in shopping_cart:
            total += item["price"] * item["quantity"]
        print(f"The total price of the items in the cart is: {currency_symbol}{total:.2f}")

    elif action == "5":
        print("Thank you. Goodbye.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
