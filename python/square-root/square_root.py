"""Module to calculate Square Root"""

def square_root(number):
    """ Use the Heron method to round numbers 

    :param number: int - natural number greater than 0
    :return: int - square root of param number
    """
    base = 600
    out = 0
    for _ in range(0,10):
        out = (1/2) * (base + number / base)
        base = out
    return round(out)
