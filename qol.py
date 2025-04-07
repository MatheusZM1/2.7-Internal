"""This project is used as a helper file with useful quality of life functions."""
import os
import time


class Colors:
    """Helper class for formmating colour of strings."""

    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class Fg:
        """Helper class for formatting colour of characters."""

        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class Bg:
        """Helper class for formatting highlight colour of characters."""

        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'


def invalid_option(seconds=2, message="Invalid option, try again."):
    """Inform user when an option selected is invalid."""
    os.system("cls")
    print(message)
    time.sleep(seconds)
    os.system("cls")


def get_pos_int(message, seconds=2):
    """Retrieve a positive integer from user (helper function)."""
    while True:  # Input validation
        try:
            user_pos_int = int(input(message))
            if user_pos_int < 0:  # Check if integer is negative
                invalid_option(seconds)
            else:
                return user_pos_int
        except ValueError:
            invalid_option(seconds)


def get_int(message, seconds=2):
    """Retrieve an integer from user (helper function)."""
    while True:  # Input validation
        try:
            user_int = int(input(message))
            return user_int
        except ValueError:
            invalid_option(seconds)


def get_pos_float(message, seconds=2):
    """Retrieve a positive float from user (helper function)."""
    while True:  # Input validation
        try:
            user_pos_int = float(input(message))
            if user_pos_int < 0:  # Check if float is negative
                invalid_option(seconds)
            else:
                return user_pos_int
        except ValueError:
            invalid_option(seconds)


def get_float(message, seconds=2):
    """Retrieve a float from user (helper function)."""
    while True:  # Input validation
        try:
            user_float = float(input(message))
            return user_float
        except ValueError:
            invalid_option(seconds)


def get_string(message, seconds=2):
    """Retrieve a string (with only letters) from user (helper function)."""
    while True:  # Input validation
        user_str = input(message)
        if not user_str.isalpha():
            invalid_option(seconds)
        else:
            return user_str
