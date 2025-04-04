"""This program re-creates a pizza ordering experience through the Python terminal for the purpose the 2.7 DIT Internal."""
from qol import *
import sys


class Pizza:
    """Represents a pizza."""

    def __init__(self, pizza_type, size, crust_type, price, amount):
        """Initiate a pizza object with given arguments."""
        self.pizza_type = pizza_type
        self.size = size
        self.crust_type = crust_type
        self.price = price
        self.amount = amount

    def __eq__(self, other):
        """Define how pizza objects should be compared."""
        if isinstance(other, Pizza):
            return self.pizza_type == other.pizza_type and self.size == other.size and self.crust_type == other.crust_type and self.price == other.price and self.amount == other.amount
        return False

    def __repr__(self):
        """Display a pizza object's information neatly, exists for debugging purposes."""
        return f"{self.amount} {self.size} {self.pizza_type} with {self.crust_type} : ${self.price:.2f}"


TEXT_DELAY = 0.05
CHECKPOINT_STRING = "\n\n> ..."


def display_stats(orders_complete, total_revenue, order_revenue, customer_complaints, complaints_increase):
    """Display stats (used after serving a customer)."""
    print("New Stats:\n")
    print(f"Orders Complete: {str(orders_complete)}/10 (+1)\nCash Register: {Colors.fg.green}${total_revenue:.2f} (+${order_revenue:.2f}){Colors.reset}\nCustomer Complaints: {Colors.fg.red}{str(customer_complaints)} (+{complaints_increase}){Colors.reset}")


def reveal_message(message, clear_screen=True):
    """Slowly reveal a string to the terminal, creating an immersive and engaging visual experience different to a simple print()."""
    if clear_screen:  # Clear all text by default, otherwise, create an empty line for spacing
        os.system("cls")
    else:
        print("")
    for c in message:  # For each character in the string, display it using sys.stdout, and sys.stdout to do so instantly
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(TEXT_DELAY * 10 if c in ['.', ','] else TEXT_DELAY)  # Add a delay between each character, and increase the delay for certain characters


def initialise():
    """Introduce the user to the project (is called at the start of the program).

    This function also allows the user to customise certain settings that will affect the rest of the experience.
    """
    os.system("cls")
    while True:
        user_input = get_int("System settings corrupt, new settings required:\n\nText speed:\n(1) - 1x\n(2) - 2x\n(3) - 4x\n(4) - Instant\n\n> ")
        if user_input in [1, 2, 3, 4]:
            text_delay = [0.05, 0.025, 0.01, 0]
            global TEXT_DELAY
            TEXT_DELAY = text_delay[user_input - 1]
            reveal_message(f"{Colors.fg.green}System settings successfully updated.{Colors.reset}\nStarting program...")
            time.sleep(1)
            break
        else:
            invalid_option()
    reveal_message("Welcome to Peppy's Pizza Shack.")
    input(CHECKPOINT_STRING)
    reveal_message("Your job is to take every customer's order, process their payments, and ensure they have a wonderful experience here at Peppy's Pizza Shack.")
    input(CHECKPOINT_STRING)
    reveal_message("As a new employee, we will be monitoring your work today.")
    reveal_message(f"Take orders very carefully, as we take customer complaints very {Colors.fg.yellow}seriously.{Colors.reset}", False)
    input(CHECKPOINT_STRING)
    reveal_message("Get to work.")
    input(CHECKPOINT_STRING)
    os.system("cls")
    main()


def get_pizza(AVAILABLE_PIZZAS, AVAILABLE_PIZZA_SIZES, AVAILABLE_PIZZA_CRUSTS):
    """Create and return a pizza object (used by the user to create pizzas for customers)."""
    while True:
        formatted_input_message = "What type of pizza does the customer want?\n\n"
        for pizza in AVAILABLE_PIZZAS:
            formatted_input_message += f"({AVAILABLE_PIZZAS.index(pizza) + 1}) {pizza[0]} - ${pizza[1]:.2f}\n"
        user_input = get_int(formatted_input_message + "\n> ")
        if 1 <= user_input <= len(AVAILABLE_PIZZAS):
            prepared_pizza_type = AVAILABLE_PIZZAS[user_input - 1]
            break
        else:
            invalid_option()
    os.system("cls")
    while True:
        formatted_input_message = "What pizza size does the customer want?\n\n"
        for size in AVAILABLE_PIZZA_SIZES:
            formatted_input_message += f"({AVAILABLE_PIZZA_SIZES.index(size) + 1}) {size[0]} - ${size[1]:.2f}\n"
        user_input = get_int(formatted_input_message + "\n> ")
        if 1 <= user_input <= len(AVAILABLE_PIZZA_SIZES):
            prepared_pizza_size = AVAILABLE_PIZZA_SIZES[user_input - 1]
            break
        else:
            invalid_option()
    os.system("cls")
    while True:
        formatted_input_message = "What type of crust does the customer want?\n\n"
        for crust in AVAILABLE_PIZZA_CRUSTS:
            formatted_input_message += f"({AVAILABLE_PIZZA_CRUSTS.index(crust) + 1}) {crust[0]} - ${crust[1]:.2f}\n"
        user_input = get_int(formatted_input_message + "\n> ")
        if 1 <= user_input <= len(AVAILABLE_PIZZA_CRUSTS):
            prepared_pizza_crust = AVAILABLE_PIZZA_CRUSTS[user_input - 1]
            break
        else:
            invalid_option()
    os.system("cls")
    while True:
        prepared_pizza_amount = get_int("How many of this pizza does the customer want? (Max. 100) \n\n> ")
        if 1 <= prepared_pizza_amount <= 100:
            break
        else:
            invalid_option(message="Invalid number of pizzas, try again.")
    total_price = round((prepared_pizza_type[1] + prepared_pizza_size[1] + prepared_pizza_crust[1]) * prepared_pizza_amount, 2)
    return Pizza(prepared_pizza_type[0], prepared_pizza_size[0], prepared_pizza_crust[0], total_price, prepared_pizza_amount)


def ending(total_revenue, customer_complaints):
    """Determine the ending of the program based on the user's performance at serving customers."""
    reveal_message("Your shift has finished, and you have served 10 customers...")
    input(CHECKPOINT_STRING)
    reveal_message(f"You have received {customer_complaints} customer complaints.")
    if customer_complaints == 0:  # No customer complaints, ending 1 or 5
        if total_revenue > 300:  # Business revenue is greater than $300, ending 5
            reveal_message(f"Due to your spectacular performance here today, we have decided to give you a large promotion.\n\nCongratulations.\n\nEnding 5/5")
        else:  # Ending 1
            reveal_message(f"Due to your great performance here today, we have decided to give you a raise.\n\nCongratulations.\n\nEnding 1/5")
    elif customer_complaints == 1:  # 1 customer complaint, ending 2
        reveal_message(f"Your performance here today was not great... but, it was also not terrible.\n\nWith that, we will allow you to keep working with us.\n\nEnding 2/5")
    elif customer_complaints < 9:  # 2 or more customer complaints, ending 3
        reveal_message(f"Due to your horrific performance here today, we have decided to fire you.\n\nGet out.\n\nEnding 3/5")
    else:  # 10 customer complaints, ending 4
        reveal_message(f"Your performance here today was so awful, that we fail to even comprehend how you even pulled it off.\n\nYou are fired, get out.\n\nEnding 4/5")
    exit()


def main():
    """This is the main function for this project, as the core project loop resides within this function."""
    CUSTOMER_NAMES = ["Josh", "Joey", "Hugo", "Cameron", "Nathaniel", "Angelina", "Tomi", "July", "Alice", "Lily", "Chris", "Daisy"]
    AVAILABLE_PIZZAS = [["Pepperoni Pizza", 10.99], ["Neapolitan Pizza", 12.99], ["Margherita Pizza", 9.99], ["BBQ Chicken Pizza", 14.99], ["Meat Lovers Pizza", 17.99], ["Hawaiian Pizza", 10.99], ["Buffalo Chicken Pizza", 14.99]]
    AVAILABLE_PIZZA_SIZES = [["Small", 0], ["Medium", 1.99], ["Large", 2.99]]
    AVAILABLE_PIZZA_CRUSTS = [["Regular Crust", 0], ["Stuffed Crust", 0.99], ["Gluten Free Crust", 1.29], ["Thick Crust", 1.99]]
    GREETINGS = ["Hello, please get me", "Oi! Get me", "Good morning. I'd like"]
    MESSAGES = ["Please also get me", "Oh! And also get", "I would also like"]
    FAREWELLS = ["Thanks.", "Took you long enough.", "Thank you."]
    COMPLAINTS = ["I'm outta here.", "How dare you! I'm never coming back!", "That's disappointing... I'm leaving."]
    orders_complete = 0
    total_revenue = 0
    customer_complaints = 0
    previous_customer_name = ""
    while True:  # Begin project core loop of customers coming in
        while True:
            current_customer = [random.choice(CUSTOMER_NAMES), []]  # Initiate a customer
            if current_customer[0] != previous_customer_name:  # Prevent immediate duplicate customer names
                break
        number_of_pizzas = random.randint(1, 2)
        for i in range (number_of_pizzas):
            selected_pizza_type = random.choice(AVAILABLE_PIZZAS)
            selected_size = random.choice(AVAILABLE_PIZZA_SIZES)
            selected_crust = random.choice(AVAILABLE_PIZZA_CRUSTS)
            selected_amount = random.randint(1, 5)
            total_price = (selected_pizza_type[1] + selected_size[1] + selected_crust[1]) * selected_amount
            selected_pizza = Pizza(selected_pizza_type[0], selected_size[0], selected_crust[0], total_price, selected_amount)
            if selected_pizza in current_customer[1]:  # Prevent customer from ordering duplicate sets of pizzas
                i -= 1
            else:
                current_customer[1].append(selected_pizza)
        customer_personality_index = random.randint(0, len(GREETINGS) - 1)
        mistake_made = False
        total_payments = 0
        for i in range(number_of_pizzas):
            current_customer_message = GREETINGS[customer_personality_index] if i == 0 else MESSAGES[customer_personality_index]
            customer_message = f"{current_customer[0]}: {current_customer_message} {current_customer[1][i].amount} {current_customer[1][i].size} {current_customer[1][i].pizza_type + ('s' if current_customer[1][i].amount > 1 else '')} with {current_customer[1][i].crust_type}."
            reveal_message(customer_message)
            input(CHECKPOINT_STRING)
            os.system("cls")
            prepared_pizza = get_pizza(AVAILABLE_PIZZAS, AVAILABLE_PIZZA_SIZES, AVAILABLE_PIZZA_CRUSTS)
            total_payments += prepared_pizza.price
            reveal_message(f"You: Here is your order, your total payments are now ${total_payments:.2f}.")
            input(CHECKPOINT_STRING)
            if prepared_pizza != current_customer[1][i]:
                reveal_message(f"{current_customer[0]}: You got my order wrong... {COMPLAINTS[customer_personality_index]}")
                input(CHECKPOINT_STRING)
                mistake_made = True
                total_payments = 0
                customer_complaints += 1
                break
        if not mistake_made:
            reveal_message(f"{current_customer[0]}: {FAREWELLS[customer_personality_index]}\n")
            input(CHECKPOINT_STRING)
            total_revenue += total_payments
        orders_complete += 1
        os.system("cls")
        display_stats(orders_complete, total_revenue, total_payments, customer_complaints, 1 if mistake_made else 0)
        input(CHECKPOINT_STRING)
        previous_customer_name = current_customer[0]  # Update previous customer name
        if orders_complete == 10:  # Game ends after 10 orders are completed
            break
    ending(total_revenue, customer_complaints)


initialise()
