"""
The various classes in this file describe different behaviours that can be undertaken by the simulator
"""

import math
import random
import string


class GenerateValues:
    def __init__(self):
        self.inc_val = 0
        self.dec_val = 257
        self.sin_root = 0
        self.specified_values = None

    # Generate a random response
    @staticmethod
    def random_value(data_type):
        if data_type in ('num', 'int'):
            value = random.randint(0, 100)
        elif data_type in 'dbl':
            value = random.randint(0, 100) + random.random()
        elif data_type in 'str':
            value = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        else:
            value = random.random()
        return value

    # Return an incrementing value, reset to 1 at 256
    def inc_value(self):
        self.inc_val += 1
        if self.inc_val > 256:
            self.inc_val = 1
        return self.inc_val

    # Return a decrementing value, reset to 256 at 1
    def dec_value(self):
        self.dec_val -= 1
        if self.dec_val < 1:
            self.dec_val = 256
        return self.dec_val

    # Return a sinusoid value
    def sin_value(self):
        self.sin_root += 0.1
        value = 2 * math.sin(self.sin_root)
        return value

    # Set and return a specific values
    def specify_values(self, specified_values):
        self.specified_values = specified_values

    def spec_value(self, command):
        if self.specified_values is None:
            value = "Unknown"
        else:
            value = self.specified_values[command]
        return value
