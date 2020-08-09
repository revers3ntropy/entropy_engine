import sprite_controller
import pygame as py
import fail_system
import utilities


class Image(sprite_controller.SpriteComponent):
    def __init__(self):
        super().__init__('image')
        self.image = None

    def start(self):
        pass

    def set_image(self, image):
        new_image = utilities.check_input(image, py.image, (f'Image must be of type py.image, not type {type(image)}',
                                                            'image.Image.set_image(image)'))
        if new_image is not False:

            self.image = new_image
            return self

    def set_image_from_file(self, file_name):
        new_file_name = utilities.check_input(file_name, str, (f'File name number must be of type str, not type {type(file_name)}.',
                                                               'image.Image.set_image_from_file(file_name)'))
        if new_file_name is not False:
            try:

                self.image = py.image.load(str(file_name))
                return self

            except:
                fail_system.error("File '" + str(file_name) + "' could not be found",
                                  'image.Image.set_image_from_file(file_name)')
