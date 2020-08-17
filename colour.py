import utilities
import fail_system


class Colour:
    def __init__(self, colour):
        self.red = colour[0]
        self.green = colour[1]
        self.blue = colour[2]
        self.colour = colour

    # use negative number for lighter shade
    def get_darker(self, amount):
        new_amount = utilities.check_input(amount, int, (f'amount needs to be of type in, not type {type(amount)}', 'colour.Colour.get_darker(amount) (1)'))
        if new_amount is not False:
            if self.red >= new_amount:
                red = self.red - new_amount
                if self.green >= new_amount:
                    blue = self.red - new_amount
                    if self.blue >= new_amount:
                        green = self.red - new_amount
                        return red, green, blue
            fail_system.error(f'Make sure that the amount is smaller than the current shade for all parts. Amount: '
                              f'{new_amount}, current shade: {self.colour}.', 'colour.Colour.get_darker(amount) (10)')
