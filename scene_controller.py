# ================================================================================================
# |-----------------------------------={ Entropy Engine }=---------------------------------------|
# ================================================================================================
#
#                                   Programmers : Joseph Coppin
#
#                                     File Name : scene_controller.py
#
#                                       Created : September 30, 2020
#
# ------------------------------------------------------------------------------------------------
#
#   Imports:
import fail_system
from sprite_controller import SpriteController
import sprite
from ui_controller import UIController
import ui
import utilities
#
# ------------------------------------------------------------------------------------------------
#
#                               Controls scene management and scenes.
#
# ------------------------------------------------------------------------------------------------
#
# ================================================================================================


class SceneManager:
    def __init__(self):
        self.scenes = []
        self.active_scene = 0

        self.new_scene()

    def new_scene(self):
        self.scenes.append(Scene('Untitled'))

    def set_active_scene(self, scene_id):
        self.active_scene = scene_id

    def current_scene(self):
        return self.scenes[self.active_scene]


class Scene:
    def __init__(self, name):
        self.name = name
        self.sprites = SpriteController()
        self.ui = UIController('hello')
        camera = self.create_sprite('camera')
        camera.add_component('body').go_to((0, 0))

    def create_sprite(self, name):
        new_name = utilities.check_input(name, str, (
            f'Sprite with name {name} cannot be created. Must be of type str.',
            'entropy_engine.create_sprite(name)'))
        if new_name is not False:
            if self.sprites.get_sprite(new_name) is not False:
                fail_system.error(f'Sprite {new_name} already exists.',
                                  'entropy_engine.create_sprite(name)')
                return False

            sprite_id = len(self.sprites.list_of_sprites)

            new_spite = sprite.Sprite(sprite_id, new_name)

            self.sprites.list_of_sprites.append(new_spite)
            return new_spite
        return False

    def create_ui_element(self, name):
        new_name = utilities.check_input(name, str, (
            'Name must of be of type str, not ' + str(type(name)) + '.',
            'entropy_engine.create_ui_element(name)'))
        if new_name is not False:
            if self.ui.get_element(new_name) is not False:
                fail_system.error("UI element already exists with name '" + str(new_name) + "'.",
                                  'entropy_engine.create_ui_element')
            else:

                ui_id = len(self.ui.list_of_ui)

                new_element = ui.Element(ui_id, new_name)

                self.ui.list_of_ui.append(new_element)
                return new_element

    def find_sprite(self, name):
        new_name = utilities.check_input(name, str, (
            'Sprite names cannot be of type ' + str(type(name)) + '. Are of type str.',
            'entropy_engine.find_sprite(name)'))
        if new_name is not False:

            new_name = str(new_name)
            for i in self.sprites.list_of_sprites:
                if i.name == new_name:
                    return i

    def find_all_with_tag(self, tag):
        new_tag = utilities.check_input(tag, str,
                                        (f'Tag has to be of type str, not {type(tag)}.', ''))
        if new_tag is not False:

            sprites = []

            for search in self.sprites.list_of_sprites:
                if search.tag == new_tag:
                    sprites.append(search)

            return sprites


scene_manager = SceneManager()
