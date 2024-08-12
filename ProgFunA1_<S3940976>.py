# SUKHUM BOONDECHARAK (S3940976)
# The Highest Part Attempted: PART 3
# Problems: Could not extract the strings from list in part 3 for printing order history
# This assignment is not easy but fun. I felt proud after accomplishing this program
# I know this is not a perfect program, but it is the first complicated program I could do on my own
# And out of the four subject I study this semester, this is the most comfortable class so far
# I suffered a lot more with assignments in other classes, and this is quite serious
# So, if there is an alternative of changing program, so I can do more of this kind of activity, please advise.

##############################################################################################################

# Identify lists that will be used within this program with some initial information stating in part 1
# List of food and sold-out is dictionaries to store both name and price
list_of_food = {"hamburger": 12.5, "coke": 3.0, "pizza": 14.0}
list_of_sold_out = {}
list_of_rewards_customers = ["Kate"]
list_of_normal_customers = ["Tom"]
list_of_history = []


# ORDER_MEAL
def order_meal():
    """
    Collect name and order with multiple inputs
    Ensure if users want to register for a rewards program
    Calculate and display a summary of order
    """
    # Define customer name
    # Check if the name is already in a reward list and enforce a valid answer using while loop
    # .strip() is implemented to avoid spacing error
    customer_name = input("Please enter your name: \n").strip()
    if customer_name not in list_of_rewards_customers:
        valid_ans = False
        while not valid_ans:
            enter_reward = input("Do you want to register to be in the rewards program? "
                                 "\nType \"y\" to register or \"n\" to ignore.\n").strip()
            if enter_reward == "y":
                list_of_rewards_customers.append(customer_name)
                valid_ans = True
            elif enter_reward == 'n' and customer_name not in list_of_normal_customers:
                list_of_normal_customers.append(customer_name)
                valid_ans = True
            else:
                print("Please answer with \"y\" or \"n\".")

    # Order food
    # Prepare temporary blank lists for the information that will be calculated in while loops
    ordered_food = []
    ordered_price = []
    ordered_amount = []

    # Use while loop to ensure the multiple orders are fulfilled, otherwise, keep asking
    # Use another while loop to indicate a valid food name
    # Also check if the food is sold-out
    enough_food = False
    while not enough_food:
        valid_food = False
        while not valid_food:
            food_name = input("Please select your food:\n").strip()
            if food_name in list_of_food:
                ordered_food.append(food_name)
                valid_food = True
            elif food_name in list_of_sold_out:
                print("This food is sold-out.")
            else:
                print("You must enter a valid food name.")

        # If the food entered is valid, identify the price from the dictionary and store the value
        food_price = list_of_food[food_name]
        ordered_price.append(food_price)

        # Same concept applied for while loop, keep asking until the input is in a valid format
        # User try & except to avoid typing error
        valid_amount = False
        while not valid_amount:
            try:
                food_amount = int(input("Please select the amount that you want: \n"))
                if food_amount == int(food_amount) and food_amount > 0:
                    ordered_amount.append(food_amount)
                    valid_amount = True
                else:
                    print("You must enter a positive number!")
            except ValueError:
                print("You must enter a number!")

        # Same concept applied for while loop, keep asking until the input is in a valid format
        # This chunk is to check the decision of users
        # They can continue order, finish ordering, or cancel the order entirely
        valid_answer = False
        while not valid_answer:
            next_option = input("Type \"y\" to add more food.\n"
                                "Type \"n\" to see the summary.\n"
                                "Type \"c\" to cancel the order. \n")
            if next_option == "y":
                valid_answer = True
                enough_food = False
            elif next_option == "n":
                valid_answer = True
                enough_food = True
            elif next_option == "c":
                valid_answer = True
                enough_food = True
            else:
                print("You type an incorrect command.")

    # To ensure to proceed next, we have to check if users did not want to cancel
    # If they cancel, we exit the function
    # Otherwise, calculate costs using for loops with zip to extract information from temporary lists
    # Identify a sum of costs with a counter in another for loop
    # Calculate a total cost by applying service fee using if to check with their rewards
    if next_option != "c":
        cost = []
        for price, amount in zip(ordered_price, ordered_amount):
            cost.append(price*amount)
        food_cost = 0
        for total in cost:
            food_cost += total

        if customer_name in list_of_rewards_customers:
            service_fee = food_cost * 0
        else:
            service_fee = food_cost * 0.1
        total_cost = food_cost + service_fee

        # Displayed Message
        # f-string is applied to align text within 50 characters
        print(("*" * 50) + "\n" + "Receipt of Customer " + customer_name + "\n" + ("*" * 50))
        for name, price, amount in zip(ordered_food, ordered_price, ordered_amount):
            print(f"{name + ':':<20}{str(price) + ' (AUD) x ' + str(amount):>30}")
        print(f"{'Service fee:':<20}{service_fee:>24.1f}{' (AUD)':>6}")
        print(f"{'Total cost:':<20}{total_cost:>24.1f}{' (AUD)':>6}\n")

        # before exiting function, create a new temporary lists to store values that will be used in history
        # Store the multiple amounts and names of food in a precise format in one list using for loop
        # Then add customer name, the above list, and total cost respectively into another list
        # And keep the record of the list in the history list
        order = []
        list_of_items = []
        for amount, food in zip(ordered_amount, ordered_food):
            items = str(amount) + " x " + str(food)
            list_of_items.append(items)
        order.append(customer_name)
        order.append(list_of_items)
        order.append(total_cost)
        list_of_history.append(order)
    else:
        print("We are sorry to hear that. We have cancelled your order.")


# ADD/UPDATE
def add_update():
    """
    Allow users to provide an update with a specific format
    Ensure to update only valid number for updated information
    """
    # Same concept applied for while loop, keep asking until the input is in a valid format
    valid_format = False
    while not valid_format:
        # Only run this if precise format is entered
        try:
            # Split the first string with commas
            # Usr for loop to run each string after being split the first time and split each of them again with colons
            # Then run another for loop to see individual values in the inner index
            # The index zero will be the name, and the index one will be the price
            updated_list = input("Please enter update(s) in the following format: \n"
                                 "dish_1: price_1, dish_2: price_2,...\n").split(',')
            for pair in range(len(updated_list)):
                updated_list[pair] = updated_list[pair].strip().split(':')
                for ind_update in range(len(updated_list[pair])):
                    updated_list[pair][ind_update] = updated_list[pair][ind_update].strip()
                updated_food = updated_list[pair][0]
                updated_price = updated_list[pair][1]

                # Validate the value with if
                # Update the list of food with the new price input if more than zero
                # Otherwise, notify users to put a valid number
                try:
                    if float(updated_price) > 0:
                        list_of_food[updated_food] = float(updated_price)
                        valid_format = True
                    else:
                        print("The price for \"" + updated_food + "\" is not more than zero.")
                        valid_format = True
                except ValueError:
                    print("The price for \"" + updated_food + "\" is not a number.")
                    valid_format = True
            print("\nThis list has been updated!\n")
        except IndexError:
            print("\nYou have entered in a wrong format!\n")


# DISPLAY EXISTING CUSTOMERS INFORMATION
def customers_information():
    """
    Display a list of customers both with and without rewards
    """
    # Display two list of customers using for loop for each list
    print("="*30 + "\n" + "CUSTOMERS WITH REWARDS" + "\n" + "="*30)
    for name in list_of_rewards_customers:
        print(str(list_of_rewards_customers.index(name) + 1) + ". " + name)
    print("")

    print("="*30 + "\n" + "CUSTOMERS WITHOUT REWARDS" + "\n" + "="*30)
    for name in list_of_normal_customers:
        print(str(list_of_normal_customers.index(name) + 1) + ". " + name)
    print("")


# DISPLAY EXISTING FOOD INFORMATION
def food_information():
    """
    Display a list of food information with name, price, and availability
    """
    # f-string is applied to align text within 40 characters
    # Use for loop to print the available food first
    # The use another for loop to print sold-out food
    print("="*40 + "\n" + f"{'FOOD':<20}{'PRICE (AUD)':>20}" + "\n" + "="*40)
    for name in list_of_food:
        print(f"{name:<20}{list_of_food[name]:>20}")
    for name in list_of_sold_out:
        print(f"{name + ' (sold out)':<20}{list_of_sold_out[name]:>20}")
    print("")


# ADD SOLD-OUT FOOD
def add_sold_out():
    """
    Allow users to update a sold-out status with a specific format
    """
    # Split the input by commas
    # Use for loop to check if names entered are in the available list or not
    # If not, let the users know, otherwise, add food name and price to sold out list
    # Then delete the same food name and price from the food list
    sold_out_food = input("Please add sold-out food in the following format: [food_1, food_2, ...]\n").split(",")
    for name in range(len(sold_out_food)):
        # Add this variable so that we don't have to strip every single variable in the loop
        the_sold_out = sold_out_food[name].strip()

        if the_sold_out in list_of_food:
            list_of_sold_out[the_sold_out] = list_of_food[the_sold_out]
            del list_of_food[the_sold_out]
        elif the_sold_out not in list_of_food:
            print(the_sold_out, "is not in the menu.")
    print("The menu has been updated!\n")


# DISPLAY THE MOST FREQUENT CUSTOMER
def most_frequent_customer():
    """
    Display information of customer who has the highest number of orders
    """
    # Create a temporary list and use for loop to extract only names from the list of history
    # Then start counting every name in the temporary list using another for loop
    # print the most counted name with the number of counts
    try:
        frequent_customer = []
        for i in range(len(list_of_history)):
            frequent_customer.append(list_of_history[i][0].strip())

        count = 0
        name = frequent_customer[0]
        for i in range(len(frequent_customer)):
            target = frequent_customer.count(i)
            if target > count:
                count = target
                name = frequent_customer[i]
        print("\nThe most frequent customer is " + name + " with " + str(frequent_customer.count(name)) + " order(s)!")
    # To avoid an error when running this at the beginning while there's no order recorded.
    except IndexError:
        print("Sorry, there is still no order in the list.")


# ORDER_HISTORY
def order_history():
    """
    Allow users to find order history from a given name
    """
    # Check if the history is empty to avoid printing a blank record
    # Otherwise, prepare a temporary list to store history information
    if not list_of_history:
        print("There is still no record.")
    else:
        valid_name = False
        specific_history_list = []
        while not valid_name:
            name_search = input("Please enter a name:\n")

            # Create a temporary name list and add all the names from list of history using for loop
            only_name_list = []
            for i in range(len(list_of_history)):
                only_name_list.append(list_of_history[i][0])

            # Check if the input is in the temporary list
            # If yes, run a for loop to extract the information from list of history with the input name
            # And store the information into the prepared list
            # Run another for loop to print the element in the prepared list
            # This is the part I gave up for extracting strings from squared brackets
            if name_search in only_name_list:
                print("This is the order history of " + name_search + ".")
                print(f"{'':<15}{'Dishes':<50}{'Total Cost':^10}")
                for num in range(len(list_of_history)):
                    if list_of_history[num][0] == name_search:
                        specific_history_list.append(list_of_history[num])
                for number in range(len(specific_history_list)):
                    print(f"{'Order '}{number+1:<9}{str(specific_history_list[number][1]):<50}{str(specific_history_list[number][2]):^10}")
                    valid_name = True
            else:
                print("The name does not have a record.")
        specific_history_list.clear()
        print("")


# MAIN MENU
def main_menu():
    """
    Display a welcome message and main command for the program

    """
    # Display the welcome message and all the command keys
    print("Welcome to the RMIT restaurant ordering system!\n")
    print("#" * 60)
    print("You can choose from the following options:")
    print("1: Order a meal")
    print("2: Add/update dishes and prices")
    print("3: Display existing customers information")
    print("4: Display existing dishes information")
    print("5: Add sold-out dishes")
    print("6: Display the most frequent customer")
    print("7: Display a customer order history")
    print("0: Exit the program")
    print("#" * 60)

    # Enforce users to input a valid number using while loop as usual
    # If the valid input is entered, run a valid function
    # Otherwise, let them try again
    valid_input = False
    while not valid_input:
        user_option = input("Please enter a valid number to select your option:\n")
        if user_option == "1":
            valid_input = True
            order_meal()
            continue_to_browse()
        elif user_option == "2":
            valid_input = True
            add_update()
            continue_to_browse()
        elif user_option == "3":
            valid_input = True
            customers_information()
            continue_to_browse()
        elif user_option == "4":
            valid_input = True
            food_information()
            continue_to_browse()
        elif user_option == "5":
            valid_input = True
            add_sold_out()
            continue_to_browse()
        elif user_option == "6":
            valid_input = True
            most_frequent_customer()
            continue_to_browse()
        elif user_option == "7":
            valid_input = True
            order_history()
            continue_to_browse()
        elif user_option == "0":
            valid_input = True
            exit_program()
        else:
            print("You have entered an invalid number!")


def continue_to_browse():
    """
    A transition before going back to main menu
    """
    # Just a transition to let the user know it is going to main menu again
    input("Press enter to go back to main menu.")
    main_menu()


def exit_program():
    """
    Display a thank you message and exit the program
    """
    # An exit of the program
    print("\nThank you for coming!\nHave a good day!")


# MAIN MENU TO DISPLAY
# The only function that runs when triggering the program
main_menu()
