"""this module does stuff"""

def square(number):
    """
    Does stuff
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 1 << (number - 1)

def total():
    """
    Also does stuff
    """
    return (1 << 64) - 1
