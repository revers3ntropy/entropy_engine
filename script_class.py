# ================================================================================================
# |------------------------------------={ Project Name }=----------------------------------------|
# ================================================================================================
#
#                                   Programmers : Joseph Coppin
#
#                                     File Name : scriptclass.py
#
#                                       Created : Month 00, 2020
#
# ------------------------------------------------------------------------------------------------
#
#   Imports:
import pygame as py
import math

from colour import Colour
import renderer
import typing
import time_controller
import global_data
import utilities
import scene_manager
#
# ------------------------------------------------------------------------------------------------
#
#                                       What the file does.
#
# ------------------------------------------------------------------------------------------------
#
# global_function_1
#
# class 'preset'
#   function_1
#
# ================================================================================================


class Script:
    def __init__(self):
        pass

    @staticmethod
    def get_screen_size():
        return renderer.mid[0] * 2, renderer.mid[1] * 2

    @staticmethod
    def force_screen_update():
        py.display.update()

    @staticmethod
    def chaos():
        return typing.chaos_14x16

    @staticmethod
    def retro():
        return typing.retro_8x10

    @staticmethod
    def keypress(key):
        try:
            if py.key.get_pressed()[key]:
                return True
            return False
        except IndexError:
            raise Exception(f'{key} is not a valid key input.')

    @staticmethod
    def get_mouse_position():
        return py.mouse.get_pos()

    @staticmethod
    def get_mouse_down():
        return py.mouse.get_pressed()

    @staticmethod
    def set_window_title(message):
        global_data.window_title = str(message)

    @staticmethod
    def file_to_image(file_name):
        return py.image.load(str(str(file_name)))

    @staticmethod
    def get_current_fps():
        return time_controller.current_fps

    @staticmethod
    def get_target_fps():
        return renderer.run_FPS

    @staticmethod
    def set_target_fps(fps):
        new_fps = utilities.check_input(fps, int)

        if 0 < new_fps < 10000:
            renderer.run_FPS = new_fps
        else:
            raise Exception(f'FPS cannot be set to {new_fps}. Make sure it is between 0 and 10000.')

    @staticmethod
    def get_current_tick():
        return time_controller.tick

    @staticmethod
    def new_colour(_colour):
        new_colour = utilities.check_vector(_colour, int)

        if len(new_colour) == 3:
            good = True
            for i in range(3):
                if 0 > new_colour[i] > 255:
                    good = False

            if good:
                return Colour(new_colour)

        raise Exception(f'Cannot create colour {new_colour}. Make sure there are three elements between 0 and 255.')

    class Vector2:
        def __init__(self, x, y):
            self.x = utilities.check_input(x, int)
            self.y = utilities.check_input(y, int)

        def add_to_vector(self, v2):
            v2 = utilities.check_input(v2, type(self))
            self.x = self.x + v2.x
            self.y = self.y + v2.y

        def times_by_vector(self, v2):
            self.x = (v2.x * self.x) + (v2.y * self.x)
            self.x = (v2.x * self.y) + (v2.y * self.y)

        def set_angle_magnitude(self, magnitude, direction):
            self.y = magnitude * math.cos(direction)
            self.x = magnitude * math.sin(direction)

    @staticmethod
    def create_sprite(name):
        return scene_manager.current_scene().create_sprite(name)

    @staticmethod
    def create_ui_element(name):
        return scene_manager.current_scene().create_ui_element(name)
