import button
import typing
import renderer


class Text(button.Buttons):
    # ================================================================================================
    #  __init__
    #
    #  INPUT:  none
    #
    #  RETURNS:  none
    #
    #  CREATED: 27/07/2020
    # ================================================================================================
    def __init__(self):
        pos = (renderer.mid_x, renderer.mid_y)
        font = typing.retro_8x10
        message = 'sample text'
        max_length = len(message)
        super().__init__(pos, font, 'text box')
        self.size_x = (typing.fonts[font][typing.size_x] + 5) * max_length
        self.hit_box = (
            self.x - self.size_x / 2 - 5, self.y - typing.fonts[self.font][typing.size_y] / 2 - 5, self.size_x + 10,
            typing.fonts[self.font][typing.size_y] + 10)
        self.message = message

    def render(self):
        self.display(self.message)
