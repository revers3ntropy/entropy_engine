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
import utilities
import colour

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
    new_size = utilities.check_vector2(screen_size, int, 'entropy_engine.init(screen_size)')
    if new_size is not False:

        renderer.init_screen(new_size)

        unit_tests.Tests().run_all_tests()
        camera = create_sprite('camera')
        camera.add_component('body').go_to((0, 0))


def __tick():
    # for finding the current fps
    start_time = time.time()

    # checks if the window should close, because you have pressed the close button
    for event in py.event.get():
        if event.type == py.QUIT:
            end()

    # controls the processing of sprites and ui elements
    ui_controller.run_ui()
    sprite_controller.update_sprites()

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
    sprite_controller.init_sprites()
    ui_controller.init_ui()

    while global_data.go:
        __tick()

    py.quit()
    quit()


def end():
    global_data.go = False


def create_sprite(name):
    new_name = utilities.check_input(name, str, ('Sprite cannot be created with type ' + str(type(name)) + '. Must be of type str.',
                                                 'entropy_engine.create_sprite(name)'))
    if new_name is not False:
        if sprite_controller.get_sprite(new_name) is not False:
            fail_system.error(f'Sprite {new_name} already exists.', 'entropy_engine.create_sprite(name)')
            return False

        sprite_id = len(sprite_controller.list_of_sprites)

        new_spite = sprite.Sprite(sprite_id, new_name)

        sprite_controller.list_of_sprites.append(new_spite)
        return new_spite


def create_ui_element(name):
    new_name = utilities.check_input(name, str, ('Name must of be of type str, not ' + str(type(name)) + '.', 'entropy_engine.create_ui_element(name)'))
    if new_name is not False:
        if ui_controller.get_element(new_name) is not False:
            fail_system.error("UI element already exists with name '" + str(new_name) + "'.", 'entropy_engine.create_ui_element')
        else:

            ui_id = len(ui_controller.list_of_ui)

            new_element = ui.Element(ui_id, new_name)

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
    new_message = utilities.check_input(message, str, ('Window title must be set to type str, not ' + str(type(message)) +
                                                       '.', 'entropy_engine.set_window_title(message)'))
    if new_message is not False:
        global_data.window_title = new_message


def keypress(key):
    try:
        if py.key.get_pressed()[key]:
            return True
        return False
    except IndexError:
        fail_system.error(str(key) + ' is not a valid key input.', 'entropy_engine.keypress(key)')


def get_mouse_position():
    return py.mouse.get_pos()


def get_mouse_down():
    return py.mouse.get_pressed()


def file_to_image(file_name):
    new_file_name = utilities.check_input(file_name, str, ('File name cannot be ' + str(file_name) + '. Must be of type str.', 'entropy_engine.file_to_image(file_name)'))
    if new_file_name is not False:
        try:
            return py.image.load(str(new_file_name))
        except:
            fail_system.error("File '" + str(new_file_name) + "' could not be found", 'entropy_engine.file_to_image()')


def find_sprite(name):
    new_name = utilities.check_input(name, str, ('Sprite names cannot be of type ' + str(type(name)) + '. Are of type str.', 'entropy_engine.find_sprite(name)'))
    if new_name is not False:

        new_name = str(new_name)
        for i in sprite_controller.list_of_sprites:
            if i.name == new_name:
                return i


def find_all_with_tag(tag):
    new_tag = utilities.check_input(tag, str, (f'Tag has to be of type str, not {type(tag)}.', ''))
    if new_tag is not False:

        sprites = []

        for search in sprite_controller.list_of_sprites:
            if search.tag == new_tag:
                sprites.append(search)

        return sprites


def get_current_fps():
    return time_controller.current_fps


def get_target_fps():
    return renderer.run_FPS


def set_target_fps(fps):
    new_fps = utilities.check_input(fps, int, ('target FPS cannot be get to type ' + str(type(fps)) + '. Must be of type int.',
                                               'entropy_engine.set_target_fps(fps)'))
    if new_fps is not False:
        try:
            new_fps = int(new_fps)
            if 0 < new_fps < 10000:
                renderer.run_FPS = new_fps
            else:
                fail_system.error('FPS cannot be set to ' + str(new_fps), 'entropy_engine.set_target_fps() (6)')
        except:
            fail_system.error('FPS cannot be set to ' + str(new_fps), 'entropy_engine.set_target_fps() (8)')


def get_current_tick():
    return time_controller.tick


def new_colour(_colour):
    new_colour = utilities.check_vector(_colour, int, 'entropy_engine.new_colour(colour)')
    if new_colour is not False:
        if len(new_colour) == 3:
            good = True
            for i in range(3):
                if 0 > new_colour[i] > 255:
                    good = False

            if good:
                return colour.Colour(new_colour)

    fail_system.error(f'Cannot create colour {new_colour}. Make sure there are three elements between 0 and 255.',
                      'entropy_engine.new_colour(_colour)')
    return False
