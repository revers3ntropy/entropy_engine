# ================================================================================================
# |-----------------------------------={ Entropy Engine }=---------------------------------------|
# ================================================================================================
#
#                                   Programmers : Joseph Coppin
#
#                                     File Name : scene_manager.py
#
#                                       Created : September 30, 2020
#
# ------------------------------------------------------------------------------------------------
#
#   Imports:
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


scenes = []
active_scene = 0


def new_scene(name):
    global scenes

    scenes.append(Scene(str(name)))


def set_active_scene(scene):
    global active_scene
    global scenes

    if type(scene) == int:
        active_scene = scene
    else:
        for i in range(len(scenes)):
            if scenes[i].name == str(scene):
                active_scene = i


def get_scene(scene):
    global scenes

    if type(scene) == int:
        return scenes[scene]
    else:
        for i in range(len(scenes)):
            if scenes[i].name == str(scene):
                return scenes[i]


def current_scene():
    global active_scene
    global scenes

    return scenes[active_scene]


class Scene:
    def __init__(self, name):
        self.name = name
        self.sprite_controller = SpriteController()
        self.ui_controller = UIController()
        camera = self.create_sprite('camera')
        camera.add_component('body').go_to((0, 0))

    def create_sprite(self, name):
        name = str(name)

        if self.sprite_controller.get_sprite(name) is not False:
            raise Exception(f'Sprite {name} already exists.')

        sprite_id = len(self.sprite_controller.list_of_sprites)

        new_spite = sprite.Sprite(sprite_id, name)

        self.sprite_controller.list_of_sprites.append(new_spite)
        return new_spite

    def create_ui_element(self, name):
        name = str(name)

        if self.ui_controller.get_element(name) is not False:
            raise Exception(f"UI element already exists with name '{name}'.")
        else:

            ui_id = len(self.ui_controller.list_of_ui)

            new_element = ui.Element(ui_id, name)

            self.ui_controller.list_of_ui.append(new_element)
            return new_element

    def find_sprite(self, name):
        for i in self.sprite_controller.list_of_sprites:
            if i.name == str(name):
                return i

    def find_all_with_tag(self, tag_name):

        sprites = []

        for search in self.sprite_controller.list_of_sprites:
            if search.tag == str(tag_name):
                sprites.append(search)

        return sprites

    def get_sprites(self):
        return self.sprite_controller.list_of_sprites

    def get_ui_elements(self):
        return self.ui_controller.list_of_ui
