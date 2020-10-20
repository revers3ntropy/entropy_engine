import time

import pygame as py
import pygame as keys  # so you can access the keys from entropy_engine

import global_data
import curser
import renderer
import unit_tests
import time_controller
import utilities
import scene_manager
import script_class
import game_data_manager  # again, for access through ee

# ================================================================================================
# |-------------------------------------={ Joseph Coppin }=-------------------------------------|
# ================================================================================================
#
#                                  Project Name : Entropy Engine
#
#                                     File Name : entropy_engine.py
#
# ------------------------------------------------------------------------------------------------
#
#      Controls the game engine. This is the file that the user accesses to use the engine.
#
# ------------------------------------------------------------------------------------------------
#
#   init - initialises the screen and game engine
#   __tick - ticks the game engine forward one tick
#   run_game - called at the end of the user file, runs the game
#   end - prematurely ends the game, eg if they click a quit button
#   create_sprite - returns and created a empty Sprite.
#   create_ui_element - returns and creates a empty ui element
#   get_screen_size - returns the dimensions of the screen in pixels by pixels
#   force_screen_update - forces the screen to refresh mid-tick
#   get_center - returns the coordinates of the center of the screen
#
# ================================================================================================


def init(screen_size):
    scene_manager.new_scene('Untitled')

    renderer.init_screen(utilities.check_vector2(screen_size, int))

    unit_tests.Tests().run_all_tests()


def __tick():
    # for finding the current fps
    start_time = time.time()

    # checks if the window should close, because you have pressed the close button
    for event in py.event.get():
        if event.type == py.QUIT:
            end()

    # controls the processing of sprites and ui elements
    current_scene = scene_manager.scenes[scene_manager.active_scene]
    current_scene.ui_controller.run_ui()
    current_scene.sprite_controller.update_sprites()

    # controls rendering of UI and sprites (keep this order)
    renderer.render_background()
    renderer.render_sprites()
    renderer.render_ui()
    renderer.render_cursor()
    renderer.tick_window()

    if global_data.typing_sticky_keys > 0:
        global_data.typing_sticky_keys -= 1

    curser.update_mouse_clicked()

    time_controller.update_fps(start_time)
    time_controller.tick += 1


def run_game():
    current_scene = scene_manager.scenes[scene_manager.active_scene]
    current_scene.sprite_controller.init_sprites()
    current_scene.ui_controller.init_ui()

    while global_data.go:
        __tick()

    py.quit()
    quit()


def get_center():
    return renderer.mid


def end():
    global_data.go = False


def create_sprite(name):
    return scene_manager.current_scene().create_sprite(name)


def create_ui_element(name):
    return scene_manager.current_scene().create_ui_element(name)


class Script(script_class.Script):
    def __init__(self):
        super().__init__()


class Prefab:
    def __init__(self):
        pass
