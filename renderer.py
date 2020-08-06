import pygame as py
import sprite_controller
import fail_system
import ui_controller
import global_data

# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : file_name.py
#
#                                       Created : July 25, 2020
#
#                                   Last Update : July 25, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                                   Controls the pygame screen.
#
# ------------------------------------------------------------------------------------------------
#
# Imports:
# 	pygame
#
# ------------------------------------------------------------------------------------------------
#
# ================================================================================================

mid = (0, 0)

run_FPS = 60

background_colour = (255, 255, 255)

py.init()
screen = None
clock = py.time.Clock()

background_images = []
current_background = 0


def init_screen(size):
    global screen
    screen = py.display.set_mode((size[0], size[1]))

    global mid
    mid = (size[0] * 0.5, size[1] * 0.5)


def set_target_fps(new_fps):
    global run_FPS
    run_FPS = new_fps


def set_background_colour(new_colour):
    global background_colour
    background_colour = new_colour


def add_background_image(image):
    global background_images
    background_images = image


def get_current_background_id():
    return current_background


def step_background():
    global current_background
    global background_images
    if current_background < len(background_images):
        current_background += 1
    else:
        current_background = 0


def set_current_background(new_background_id):
    global background_images
    global current_background
    if int(new_background_id) < 0 or int(new_background_id) > len(background_images):
        fail_system.error('Background cannot be set to ' + str(new_background_id), 'renderer.set_current_background()')


def render_background():
    if not background_images:
        screen.fill(background_colour)
    else:
        screen.blit(background_images[current_background], (0, 0))


def render_cursor():
    if global_data.mouse_image is not None:
        screen.blit(global_data.mouse_image, py.mouse.get_pos())


def render_sprites():
    camera = sprite_controller.list_of_sprites[0]
    camera_coords = camera.get_component('body').get_position()

    for i in sprite_controller.list_of_sprites:
        sprite_image = i.get_component('image')
        if sprite_image is not False and sprite_image.get_image() is not None:

            sprite_coords = i.get_component('body').get_position()
            render_coords = (round(sprite_coords[0] + -camera_coords[0]), round(sprite_coords[1] + -camera_coords[1]))
            screen.blit(sprite_image.get_image(), render_coords)


def render_ui():
    for i in ui_controller.list_of_ui:
        if i.get_state():
            i.render()
