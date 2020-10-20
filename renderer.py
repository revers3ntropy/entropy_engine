# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : renderer.py
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
import pygame as py
import global_data
import scene_manager
import time_controller
#
# ------------------------------------------------------------------------------------------------
#
# ================================================================================================

mid = (0, 0)

background_colour = (255, 255, 255)

py.init()

screen_size = width, height = 600, 400

screen = py.display.set_mode(screen_size, py.RESIZABLE)

background_images = []
current_background = 0


def init_screen(size):
    global screen
    screen = py.display.set_mode((size[0], size[1]))

    global mid
    mid = (size[0] * 0.5, size[1] * 0.5)


def tick_window():
    py.display.update()
    screen.fill(background_colour)

    py.display.set_caption(str(global_data.window_title))
    time_controller.clock_tick()


def set_target_fps(new_fps):
    time_controller.run_fps = new_fps


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
        raise Exception(f'Background cannot be set to {new_background_id}')


def render_background():
    if not background_images:
        screen.fill(background_colour)
    else:
        screen.blit(background_images[current_background], (0, 0))


def render_cursor():
    if global_data.mouse_image is not None:
        screen.blit(global_data.mouse_image, py.mouse.get_pos())


def __render_sprite(sprite, camera_coords):

    sprite_body = sprite.get_component('body')
    if sprite_body is not False:

        sprite_coords = sprite_body.position
        render_coords = (round(sprite_coords[0] + -camera_coords[0]), round(sprite_coords[1] + -camera_coords[1]))

        sprite_image = sprite.get_component('image')

        if sprite_image is not False:
            if sprite_image.image:
                render_coords = (render_coords[0] + sprite_image.offset[0], render_coords[0] + sprite_image.offset[0])
                screen.blit(sprite_image.image, render_coords)

        sprite_rect = sprite.get_component('rect renderer')
        if sprite_rect is not False:
            render_coords = (render_coords[0] + sprite_rect.offset[0], render_coords[0] + sprite_rect.offset[0])
            render_size = sprite_rect.size
            colour = sprite_rect.colour.colour
            py.draw.rect(screen, colour, (render_coords[0], render_coords[1], render_size[0], render_size[1]))


def render_sprites():
    camera = scene_manager.scenes[scene_manager.active_scene].sprite_controller.list_of_sprites[0]
    camera_coords = camera.get_component('body').position

    for i in scene_manager.scenes[scene_manager.active_scene].sprite_controller.list_of_sprites:
        __render_sprite(i, camera_coords)


def render_ui():
    for i in scene_manager.scenes[scene_manager.active_scene].ui_controller.list_of_ui:
        if i.state:
            i.render()
