import utilities


class Colour:
    def __init__(self, colour):
        self.red = colour[0]
        self.green = colour[1]
        self.blue = colour[2]
        self.colour = colour

    # use negative number for lighter shade
    def get_darker(self, amount):
        new_amount = utilities.check_input(amount, int)

        if self.red >= new_amount:
            red = self.red - new_amount
            if self.green >= new_amount:
                blue = self.red - new_amount
                if self.blue >= new_amount:
                    green = self.red - new_amount
                    return red, green, blue

        raise Exception(
            f'Make sure that the amount is smaller than the current shade for all parts. Amount: '
            f'{new_amount}, current shade: {self.colour}.')
