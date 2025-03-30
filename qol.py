"""This project is used as a helper file with useful quality of life functions"""
import os, time, random


class Colors:
    """Helper class for formmating colour of strings."""
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'
 
    class fg:
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
 
    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'


def invalid_option(seconds = 2, message = "Invalid option, try again."):
    """Helper function for informing user when an option selected in invalid."""
    os.system("cls")
    print(message)
    time.sleep(seconds)
    os.system("cls")


def get_pos_int(message, seconds = 2):
    """Helper function for retrieving a positive integer from the user"""
    while True:
        try:
            user_pos_int = int(input(message))
            if user_pos_int < 0:
                invalid_option(seconds)
            else:
                return user_pos_int
        except ValueError:
            invalid_option(seconds)


def get_int(message, seconds = 2):
    """Helper function for retrieving an integer from the user"""
    while True:
        try:
            user_int = int(input(message))
            return user_int
        except ValueError:
            invalid_option(seconds)


def get_pos_float(message, seconds = 2):
    """Helper function for retrieving a positive float from the user"""
    while True:
        try:
            user_pos_int = float(input(message))
            if user_pos_int < 0:
                invalid_option(seconds)
            else:
                return user_pos_int
        except ValueError:
            invalid_option(seconds)


def get_float(message, seconds = 2):
    """Helper function for retrieving a float from the user"""
    while True:
        try:
            user_float = float(input(message))
            return user_float
        except ValueError:
            invalid_option(seconds)


def get_string(message, seconds = 2):
    """Helper function for retrieving a string (with only letters) from the user"""
    while True:
        user_str = input(message)
        if not user_str.isalpha():
            invalid_option(seconds)
        else:
            return user_str