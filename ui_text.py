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
        pos = renderer.mid
        font = typing.retro_8x10
        message = 'sample text'
        max_length = len(message)
        super().__init__(pos, font, 'text box')
        self.size_x = (typing.fonts[font][typing.size_x] + 5) * max_length
        self.hit_box = (
            self.x - self.size_x / 2 - 5, self.y - typing.fonts[self.font][typing.size_y] / 2 - 5, self.size_x + 10,
            typing.fonts[self.font][typing.size_y] + 10)
        self.message = message

    def start(self):
        pass

    def render(self):
        self.display(self.message)

    def set_text(self, new_text):
        self.message = new_text

    def run(self):
        pass

    def __update_position(self):
        self.hit_box = (
            self.x - self.size_x / 2 - 5, self.y - typing.fonts[self.font][typing.size_y] / 2 - 5, self.size_x + 10,
            typing.fonts[self.font][typing.size_y] + 10)

    def set_position(self, new_pos):
        self.x = new_pos[0]
        self.y = new_pos[1]
        self.__update_position()
