import pygame as py
import sprite_controller
import ui_controller

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

screen_x = 1000
screen_y = 600
mid_x = screen_x / 2
mid_y = screen_y / 2

run_FPS = 60

background_colour = (255, 255, 255)

py.init()
screen = py.display.set_mode((screen_x, screen_y))
clock = py.time.Clock()

screen.fill((255, 255, 255))
py.display.update()


def set_target_fps(new_fps):
    global run_FPS
    run_FPS = new_fps


def set_background_colour(new_colour):
    global background_colour
    background_colour = new_colour


def render_sprites():
    camera = sprite_controller.list_of_sprites[0]
    camera_coords = camera.get_component('body').get_position()

    for i in sprite_controller.list_of_sprites:
        sprite_image = i.get_component('image')
        if sprite_image is not False and sprite_image.get_image() is not None:

            sprite_coords = i.get_component('body').get_position()
            render_coords = (round(sprite_coords[0] + camera_coords[0]), round(sprite_coords[1] + camera_coords[1]))
            screen.blit(sprite_image.get_image(), render_coords)


def render_ui():
    for i in ui_controller.list_of_ui:
        if i.get_state():
            i.render()
