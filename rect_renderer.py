import sprite_controller
import utilities
import colour


class RectRenderer(sprite_controller.SpriteComponent):
    def __init__(self, sprite):
        super().__init__('rect renderer')
        self.sprite = sprite
        self.body = None

        self.offset = (0, 0)
        self.size = (10, 10)
        self.colour = colour.Colour((255, 10, 10))

    def start(self):
        self.body = self.sprite.get_component('body')

    def set_size(self, size):
        new_size = utilities.check_vector2(size, int, 'hit_box.HitBox.set_size(size)')
        if new_size is not False:

            self.size = (new_size[0], new_size[1])

    def set_offset(self, offset):
        new_offset = utilities.check_vector2(offset, int, 'image.Image.set_offset(offset)')
        if new_offset is not False:
            self.offset = new_offset

    def set_colour(self, colour_):
        new_colour = utilities.check_input(colour_, colour.Colour, (f'Colour cannot be set to {colour_}. Make sure it is of type Colour.', 'rect_renderer.RectRenderer.set_colour(colour)'))
        if new_colour is not False:

            self.colour = new_colour

