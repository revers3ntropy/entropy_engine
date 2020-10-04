import sprite_controller
import pygame as py
import utilities


class Image(sprite_controller.SpriteComponent):
    def __init__(self):
        super().__init__('image')
        self.image = None

        self.offset = (0, 0)

    def start(self):
        pass

    def set_image(self, image):
        self.image = utilities.check_input(image, py.image)

    def set_image_from_file(self, file_name):
        self.image = py.image.load(str(file_name))

    def set_offset(self, offset):
        self.offset = utilities.check_vector2(offset, int)
