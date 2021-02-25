import random
from string import ascii_uppercase, digits

class Robot:

    def __init__(self):
        self.generate_name()

    def reset(self):
        self.generate_name()

    def generate_name(self):
        random.seed()
        self.name = ''.join(random.choices(ascii_uppercase, k=2) + random.choices(digits, k=3))
        return self.name