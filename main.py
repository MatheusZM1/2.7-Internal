'''This program re-creates a pizza ordering experience through the Python terminal for the purpose the 2.7 DIT Internal'''

'''
Module imports go at the top, qol is a custom made python file for this project to seperate 
some useful and re-usable functions in order to not clog this  main file with more code
'''
from qol import *
import sys

class Pizza:
    def __init__(self, pizza_type, size, crust_type, price):
        self.pizza_type = pizza_type
        self.size = size
        self.crust_type = crust_type
        self.price = price

    def __repr__(self):
        return f"{self.size} {self.pizza_type} with {self.crust_type} : ${self.price:.2f}" 

CHECKPOINT_STRING = "\n\n> ..."
TEXT_DELAY = [0.05] # TEXT_DELAY is not a true constant, as it is modified exactly once at the very beginning of the program, but will be treated as one

current_customer = ["Joey", [], [], ]

'''
This function is used to slowly reveal a string to the terminal, creating an immersive and engaging visual experience different to a simple print()
'''
def reveal_message(message, clear_screen = True):
    if clear_screen: # Clear all text by default, otherwise, create an empty line for spacing
        os.system("cls")
    else: 
        print("")
    for c in message: # For each character in the string, display it using sys.stdout, and sys.stdout to do so instantly
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(TEXT_DELAY[0] * 10 if c in ['.', ','] else TEXT_DELAY[0]) # Add a delay between each character, and increase the delay for certain characters

'''
This function is used at the beginning of the program to introduce the user to this experience, 
and allow them to customise certain settings that will affect the rest of the experience. 
'''
def initialise():
    os.system("cls")
    while True:
        user_input = get_int("System settings corrupt, new settings required:\n\nText speed:\n1 - 1x\n2 - 2x\n3 - 4x\n\n> ")
        if user_input in [1, 2, 3]:
            text_delay = [0.05, 0.025, 0.01]
            TEXT_DELAY[0] = text_delay[user_input - 1]
            reveal_message(f"{colors.fg.green}System settings successfully updated.{colors.reset}\nStarting program...")
            time.sleep(1)
            break
        else:
            invalid_option()
    reveal_message("Welcome to Peppy's Pizza Shack.")
    input(CHECKPOINT_STRING)
    reveal_message("Your job is to take every customer's order, process their payments, and ensure they have a wonderful experience here at Peppy's Pizza Shack.")
    input(CHECKPOINT_STRING)
    reveal_message("As a new employee, a training video teaching you how to do your job will be avaiable for your viewing.")
    reveal_message(f"Watch it carefully, as we take customer complaints very {colors.fg.yellow}seriously.{colors.reset}", False)
    input(CHECKPOINT_STRING)
    reveal_message("Get to work.")

'''This function initiates the ordering process, and is the menu of the program.'''
def menu():
    while True:
        user_int = get_int("Pizza Shack\n1- ")

initialise()