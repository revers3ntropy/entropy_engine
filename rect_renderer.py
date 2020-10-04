import sprite_controller
import utilities
from colour import Colour


class RectRenderer(sprite_controller.SpriteComponent):
    def __init__(self, sprite):
        super().__init__('rect renderer')
        self.sprite = sprite
        self.body = None

        self.offset = (0, 0)
        self.size = (10, 10)
        self.colour = Colour((255, 10, 10))

    def start(self):
        self.body = self.sprite.get_component('body')

    def set_size(self, size):
        new_size = utilities.check_vector2(size, int)

        self.size = (new_size[0], new_size[1])

    def set_offset(self, offset):
        self.offset = utilities.check_vector2(offset, int)

    def set_colour(self, colour_):
        self.colour = utilities.check_input(colour_, Colour)
