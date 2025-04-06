def place_order(menu):
    """
    Displays a restaurant menu, asks customers for their order, then returns
    their receipt and total price.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their 
                       prices, using the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered.
    order_total (float): The total price of the order.
    """
    # Set up order list. Order list will store a list of dictionaries for
    # menu item name, item price, and quantity ordered
    order = []

    # Get the menu items mapped to the menu numbers
    menu_items = get_menu_items_dict(menu)

    # Launch the store and present a greeting to the customer
    print("Welcome to the Generic Take Out Restaurant.")

    # TODO: Create a continuous while loop so customers can order multiple items
    while True:
        print('Menu:')
        print_menu_heading()
        i = 1

        for food_category, options in menu.items():
            for meal, price in options.items():
                print_menu_line(i, food_category, meal, price)
                i += 1
                place_order(menu)

        # TODO: Ask the customer what they want to order
        menu_selection = input("What would you like to order?").strip()
        order = update_order(order, menu_selection, menu_items)

        another = input("Would you like to order anything else? (y/n): ").strip().lower()
        if another == 'n':
                print('Thank you for your order!')
                break

        # TODO: Loop through the menu dictionary
        # for food_category, options in menu():
        #     for meal, price in options():
        #         menu(i, food_category, meal, price)
        #         i += 1

        # TODO: Extract the food category and the options for each category
        # for food_category, options in menu():
        #     print(f'Category: {food_category}')
        #     print('Options:')
        #     for meal, price in options():
        #         print(f' {meal} - ${price:.2f}')

            # TODO: Loop through the options for each food category
            # for food_category in menu():
            #     print(f'Food Category: {food_category}')
                
            # TODO: Extract the meal and the price for each option
            # for food_category, options in menu():
            #     for meal, price in options():
            #         print(i, food_category, meal, price)

                # Print the menu item number, food category, meal, and price
                # TODO: Only if you used different variable names


                # TODO: Update the variable names in the following function
                # print_menu_line(i, food_category, meal, price)

                # Update the menu selection number
                # i += 1

        # TODO: Ask customer to input menu item number
        # menu_selection = input('Please enter the item number')

        # TODO: Update the order list using the update_order function
        # TODO: Send the order list, menu selection, and menu items as arguments
        # order = (order, menu_selection, menu_items)

        # TODO: Ask the customer if they would like to order anything else
        # TODO: Let the customer know if they should type 'n' or 'N' to quit
        # another = input('' \
        # 'Would you like to order anything else? (y/n): ').strip().lower()
        # if another == 'n':
        # TODO: Write a conditional statement that checks the user's input
        # TODO: The conditional statement should check for 'n' or 'N'
        #     another = input('' \
        # 'Would you like to order anything else? (y/n): ').strip().lower()
        # if another == 'n':
                
            # TODO: Write a print statement that thanks the customer for their order
            # print('Thank you for your order!')

            # TODO: Use list comprehension to create a list called prices_list,
            # TODO: which contains the total prices for each item in the order list:
            # TODO: The total price for each item should multiply the price by quantity
    if order:
        prices_list = [item["Price"] * item["Quantity"] for item in order]

            # TODO: Create an order_total from the prices list using sum()
            # TODO: Round the prices to 2 decimal places.
        order_total = round(sum(prices_list), 2)
    else:
            order_total = 0.00

            # TODO: Exit the ordering loop
            # TODO: Either use a break statement or set the condition to False
            # break

    # TODO: Return the order list and the order total
    return order, order_total

def update_order(order, menu_selection, menu_items):
    """
    Checks if the customer menu selection is valid, then updates the order.

    Parameters:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    menu_selection (str): The customer's menu selection.
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered (updated as needed).
    """
    # TODO: Check if the customer typed a number
    if not menu_selection.isdigit():
        print("Invalid input. Please enter a vlaid item number")
        return order

        # TODO: Convert the menu selection to an integer
    item_number = int(menu_selection)

        # TODO: Check if the menu selection is in the menu items keys
    if item_number not in menu_items:
        print("That item number is not on the menu")
        return order
        
            # TODO: Store the item name as a variable
    meal_name, price = menu_items[item_number]

            # TODO: Ask the customer for the quantity of the menu item
            # TODO: Use the item name variable in the question
    quantity_input = input(f"How many '{meal_name}' would you like?").strip()

            # TODO: Check if the quantity is a number, default to 1 if not
    if not quantity_input.isdigit():
                quantity = 1
    else: 
                quantity = int(quantity_input)

            # TODO: Add a dictionary to the order list 
            # TODO: The dictionary should include the item name, price, and quantity
            # TODO: Use the following names for the dictionary keys:
            # TODO: "Item name", "Price", "Quantity"
    order.append({
        'Item name': meal_name,
        'Price': price,
        'Quantity': quantity
    })

        # TODO: When the user's input isn't valid, 
        # TODO: tell the customer that their input isn't valid
        # else: 
        #     print('Invalid selection. Choose a valid menu item')

    # TODO: When the menu selection wasn't valid:
    # TODO: Print the menu selection and 
    # TODO: Tell the customer they didn't select a menu option
        # else:
    print(f"Added {quantity} x {meal_name} to your order")

    # TODO: Return the updated order
    return order

def print_itemized_receipt(receipt):
    """
    Prints an itemized receipt for the customer.

    Parameters:
    receipt (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    """

    print(receipt)

    # TODO: Loop through the items in the customer's receipt
    # TODO Store the dictionary items as variables
    for item in receipt:
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]

        # TODO: Print the receipt line using the print_receipt_line function
        # TODO: Send the item name, price, and quantity as separate arguments
        print_receipt_line(item_name, price, quantity)


##################################################
#  STARTER CODE
#  Do not modify any of the code below this line:
##################################################

def print_receipt_line(item_name, price, quantity):
    """
    Prints a line of the receipt.

    Parameters:
    item_name (str): The name of the meal item.
    price (float): The price of the meal item.
    quantity (int): The quantity of the meal item.
    """
    # Calculate the number of spaces for formatted printing
    num_item_spaces = 32 - len(item_name)
    num_price_spaces = 6 - len(str(price))

    # Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces

    # Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")

def print_receipt_heading():
    """
    Prints the receipt heading.
    """
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("--------------------------------|--------|----------")

def print_receipt_footer(total_price):
    """
    Prints the receipt footer with the total price of the order.

    Parameters:
    total_price (float): The total price of the order.
    """
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")

def print_menu_heading():
    """
    Prints the menu heading.
    """
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")

def print_menu_line(index, food_category, meal, price):
    """
    Prints a line of the menu.

    Parameters:
    index (int): The menu item number.
    food_category (str): The category of the food item.
    meal (str): The name of the meal item.
    price (float): The price of the meal item.
    """
    # Print the menu item number, food category, meal, and price
    num_item_spaces = 32 - len(food_category + meal) - 3
    item_spaces = " " * num_item_spaces
    if index < 10:
        i_spaces = " " * 6
    else:
        i_spaces = " " * 5
    print(f"{index}{i_spaces}| {food_category} - {meal}{item_spaces} | ${price}")

def get_menu_items_dict(menu):
    """
    Creates a dictionary of menu items and their prices mapped to their menu 
    number.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their
                        prices.

    Returns:
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.
    """
    # Create an empty dictionary to store the menu items
    menu_items = {}

    # Create a variable for the menu item number
    i = 1

    # Loop through the menu dictionary
    for food_category, options in menu.items():
        # Loop through the options for each food category
        for meal, price in options.items():
            # Store the menu item number, item name and price in the menu_items
            menu_items[i] = {
                "Item name": food_category + " - " + meal,
                "Price": price
            }
            i += 1

    return menu_items

def get_menu_dictionary():
    """
    Returns a dictionary of menu items and their prices.

    Returns:
    meals (dictionary): A nested dictionary containing the menu items and their
                        prices in the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }
    """
    # Create a meal menu dictionary
    #"""
    meals = {
        "Burrito": {
            "Chicken": 4.49,
            "Beef": 5.49,
            "Vegetarian": 3.99
        },
        "Rice Bowl": {
            "Teriyaki Chicken": 9.99,
            "Sweet and Sour Pork": 8.99
        },
        "Sushi": {
            "California Roll": 7.49,
            "Spicy Tuna Roll": 8.49
        },
        "Noodles": {
            "Pad Thai": 6.99,
            "Lo Mein": 7.99,
            "Mee Goreng": 8.99
        },
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    }
    """
    # This menu is just for testing purposes
    meals = {
        "Cake": {
            "Kuih Lapis": 3.49,
            "Strawberry Cheesecake": 6.49,
            "Chocolate Crepe Cake": 6.99
        },
        "Pie": {
            "Apple": 4.99,
            "Lemon Meringue": 5.49
        },
        "Ice-cream": {
            "2-Scoop Vanilla Cone": 3.49,
            "Banana Split": 8.49,
            "Chocolate Sundae": 6.99
        }
    }
    """
    return meals

# Run the program
if __name__ == "__main__":
    # Get the menu dictionary
    meals = get_menu_dictionary()

    receipt, total_price = place_order(meals)

    # Print out the customer's order
    print("This is what we are preparing for you.\n")

    # Print the receipt heading
    print_receipt_heading()

    # Print the customer's itemized receipt
    print_itemized_receipt(receipt)

    # Print the receipt footer with the total price
    print_receipt_footer(total_price)

