"""Module to calculate Square Root"""

def square_root(number):
    """ Use the Heron method to round numbers 

    :param number: int - natural number greater than 0
    :return: int - square root of param number
    """
    out = 600
    for _ in range(0,25):
        out = 1/2 * (out + number / out)
    return round(out)
 