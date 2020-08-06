import typing
import pygame as py
import global_data
import sprite_controller
import ui_controller
import curser
import renderer
import sprite
import ui
import fail_system
import unit_tests
import time
import time_controller

# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Entropy Engine
#
#                                     File Name : entropy_engine.py
#
#                                       Created : August 05, 2020
#
#                                   Last Update : August 06, 2020
#
# ------------------------------------------------------------------------------------------------
#
#   This is the file which is imported by the user. Contains top level functions for the user.
#
# ------------------------------------------------------------------------------------------------
#
# Imports:
#   typing
#   pygame as py
#   global_data
#   sprite_controller
#   ui_controller
#   curser
#   renderer
#   sprite
#   ui
#   fail_system
#   unit_tests
#   time
#   time_controller
#
# ------------------------------------------------------------------------------------------------
#
# global_function_1 - what this function does
#
# ================================================================================================


def init(screen_size):
    renderer.init_screen(screen_size)
    unit_tests.Tests().run_all_tests()
    camera = create_sprite('camera')
    camera.add_component('body').go_to((0, 0))


# ================================================================================================
#  tick -- controls each tick of the game
#
#      Controls rendering, physics ticks and the pygame display.
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 00/00/2020
# ================================================================================================
def __tick():
    # for finding the current fps
    start_time = time.time()

    # checks if the window should close, because you have pressed the close button
    for event in py.event.get():
        if event.type == py.QUIT:
            end()

    # ticks the pygame display
    py.display.set_caption(str(global_data.window_title))
    py.display.flip()
    renderer.clock.tick(renderer.run_FPS)

    # controls rendering of UI and sprites (keep this order)
    renderer.render_background()
    renderer.render_sprites()
    renderer.render_ui()

    # controls the processing of sprites and ui elements
    ui_controller.run_ui()
    sprite_controller.update_sprites()

    if global_data.typing_sticky_keys > 0:
        global_data.typing_sticky_keys -= 1

    curser.update_mouse_clicked()

    time_controller.update_fps(start_time)
    time_controller.tick += 1


def run_game():
    sprite_controller.init_sprites()
    ui_controller.init_ui()

    while global_data.go:
        __tick()

    py.quit()
    quit()


def end():
    global_data.go = False


def create_sprite(name):
    if sprite_controller.get_sprite(name) is not False:
        return False
    sprite_id = len(sprite_controller.list_of_sprites)

    new_spite = sprite.Sprite(sprite_id, name)

    sprite_controller.list_of_sprites.append(new_spite)
    return new_spite


def create_ui_element(name):
    if ui_controller.get_element(name) is not False:
        fail_system.error("UI element already exists with name '" + str(name) + "'.", 'entropy_engine.create_ui_element')
        return False

    ui_id = len(ui_controller.list_of_ui)

    new_element = ui.Element(ui_id, name)

    ui_controller.list_of_ui.append(new_element)
    return new_element


def get_screen_size():
    return renderer.mid[0] * 2, renderer.mid[1] * 2


def force_screen_update():
    py.display.update()


def get_center():
    return renderer.mid


def chaos():
    return typing.chaos_14x16


def retro():
    return typing.retro_8x10


def set_window_title(message):
    global_data.window_title = message


def keypress(key):
    if py.key.get_pressed()[key]:
        return True
    return False


def get_mouse_position():
    return py.mouse.get_pos()


def get_mouse_down():
    return py.mouse.get_pressed()


def file_to_image(file_name):
    try:
        return py.image.load(str(file_name))
    except:
        fail_system.error("File '" + str(file_name) + "' could not be found", 'entropy_engine.file_to_image()')


def find_sprite(name):
    name = str(name)
    for i in sprite_controller.list_of_sprites:
        if i.get_name() == name:
            return i


def get_current_fps():
    return time_controller.current_fps


def get_target_fps():
    return renderer.run_FPS


def set_target_fps(fps):
    try:
        fps = int(fps)
        if 0 < fps < 10000:
            renderer.run_FPS = fps
        else:
            fail_system.error('FPS cannot be set to ' + str(fps), 'entropy_engine.set_target_fps() (6)')
    except:
        fail_system.error('FPS cannot be set to ' + str(fps), 'entropy_engine.set_target_fps() (8)')


def get_current_tick():
    return time_controller.tick

