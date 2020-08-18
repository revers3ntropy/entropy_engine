import sprite_controller
import utilities
import fail_system


class RectRenderer(sprite_controller.SpriteComponent):
    def __init__(self, sprite):
        super().__init__('rect renderer')
        self.sprite = sprite
        self.body = None

        self.offset = (0, 0)
        self.colour = (255, 10, 10)
        self.size = (10, 10)

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

    def set_colour(self, colour):
        new_colour = utilities.check_vector(colour, int, 'image.Image.set_offset(offset)')
        if new_colour is not False:
            if len(colour) == 3:

                good = True
                for i in range(3):
                    if 255 <= new_colour[i] <= 0:
                        good = False

                if good:
                    self.offset = new_colour
                    return True

        fail_system.error(f'Colour cannot be set to {colour}. Make sure each value is between 0 and 255, and there are only three values',
                          'rect_renderer.RectRenderer.set_colour(colour)')
