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


def write(font, message, pos):  # just so that you only have to import one file
    typing.write(font, message, pos)


def write_from_left(font, message, pos):  # just so that you only have to import one file
    typing.write_from_left(font, message, pos)


def get_screen():
    return renderer.screen


def get_screen_size():
    return renderer.screen_x, renderer.screen_y


def force_screen_update():
    py.display.update()


def get_center():
    return renderer.mid_x, renderer.mid_y


def chaos():
    return typing.chaos_14x16


def retro():
    return typing.retro_8x10


def set_window_title(message):
    global_data.window_title = message


def set_window_size(size_x, size_y):
    try:
        size_y = int(size_y)
        size_x = int(size_x)
    except:
        fail_system.error("Screen size cannot be set to (" + str(size_x) + ', ' + str(size_y) + "). Please set it to (int, int).")
    renderer.screen = py.display.set_mode((size_x, size_y))


def tick():
    py.display.set_caption(str(global_data.window_title))
    py.display.flip()
    renderer.clock.tick(renderer.run_FPS)

    renderer.screen.fill(renderer.background_colour)

    renderer.render_ui()
    ui_controller.run_ui()
    renderer.render_sprites()
    sprite_controller.update_sprites()

    if global_data.typing_sticky_keys > 0:
        global_data.typing_sticky_keys -= 1

    curser.update_mouse_clicked()

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            return False
    return True


def create_sprite(name):
    if sprite_controller.get_sprite(name) is not False:
        return False
    sprite_id = len(sprite_controller.list_of_sprites)

    new_spite = sprite.Sprite(sprite_id, name)

    sprite_controller.list_of_sprites.append(new_spite)
    return new_spite


def create_ui_element(name):
    if ui_controller.get_element(name) is not False:
        fail_system.error("UI element already exists with name '" + str(name) + "'")
        return False

    ui_id = len(ui_controller.list_of_ui)

    new_element = ui.Element(ui_id, name)

    ui_controller.list_of_ui.append(new_element)
    return new_element


def init_ee():
    unit_tests.Tests().run_all_tests()
    camera = create_sprite('camera')
    camera.add_component('body')


def run_game():
    while global_data.go:
        tick()
    py.quit()


def keypress(key):
    pass


def get_mouse_position():
    return py.mouse.get_pos()


def get_mouse_down():
    return py.mouse.get_pressed()


def file_to_image(file_name):
    try:
        return py.image.load(str(file_name))
    except:
        fail_system.error("File '" + str(file_name) + "' could not be found")


def set_gravity(strength):
    try:
        strength = float(strength)
    except:
        fail_system.error('Gravity has to be of type float, not ' + str(type(strength)))
        return False

    if -100 > strength > 100:
        fail_system.error('Gravity cannot be set to ' + str(strength) + '. Please set it to a float number betweenb -100 and 100.')
    else:
        global_data.gravity = strength


def end():
    global_data.go = False
