"""calculates if a given number is an armstrong number"""

def is_armstrong_number(number):
    """
    param number: int - given number
    return bool: whether the number is an armstrong number
    """

    total = 0
    for digit in str(number):
        total += int(digit) ** len(str(number))

    return total == number

    # return number == sum(int(c)**len(str(number)) for c in str(number))
