"""this module does stuff"""

def square(number):
    """
    Does stuff
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)

def total():
    """
    Also does stuff
    """
    return 2 ** 64 - 1
