import sprite_controller
import pygame as py
import fail_system


class Image(sprite_controller.SpriteComponent):
    def __init__(self):
        super().__init__('image')
        self.image = None

    def set_image(self, image):
        self.image = image
        return self

    def set_image_from_file(self, file_name):
        try:
            self.image = py.image.load(str(file_name))
            return self
        except:
            fail_system.error("File '" + str(file_name) + "' could not be found")

    def get_image(self):
        return self.image
