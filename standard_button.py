import button
import typing
import pygame as py
import renderer


class StandardButton(button.Buttons):
    # ================================================================================================
    #  __init__
    #
    #  INPUT:  x, y     - int  - coordinates of the button, taken from Button class
    #		   font     -  int   - which font should used for the button - taken from Button
    #		   message - string - what should the button say
    #
    #  RETURNS:  none
    #
    #  CREATED: 27/07/2020
    # ================================================================================================
    def __init__(self):
        pos = (renderer.mid_x, renderer. mid_y)
        font = typing.retro_8x10
        message = 'button text'
        super().__init__(pos, font, 'standard button')
        self.message = message
        self.size_x = (typing.fonts[font][typing.size_x] + 5) * len(message)
        self.hit_box = (pos[0] - self.size_x / 2 - 7, pos[1] - typing.fonts[font][typing.size_y] / 2 - 7, self.size_x + 14,
                        typing.fonts[font][typing.size_y] + 14)

        self.selected_colour = (
            renderer.background_colour[0] - 100, renderer.background_colour[1] - 100,
            renderer.background_colour[2] - 100)
        self.outside_colour = (
            renderer.background_colour[0] - 50, renderer.background_colour[1] - 50, renderer.background_colour[2] - 50)
        self.inside_colour = renderer.background_colour

    # ================================================================================================
    #  display_box -- draws a box around the button
    #
    #      Uses the hitbox to draw two rectangles of slightly different sizes on top of each other,
    #		thus drawing a background and outline to the button. Also is effected by self.moused
    #		which is if the button is being touched by the curser.
    #
    #  INPUT:  none
    #
    #  RETURNS:  none
    #
    #  CREATED: 27/07/2020
    # ================================================================================================
    def display_box(self):
        if self.moused:
            py.draw.rect(renderer.screen, self.selected_colour, self.hit_box)
        else:
            py.draw.rect(renderer.screen, self.outside_colour, self.hit_box)
        new_hit_box = (self.hit_box[0] + 2, self.hit_box[1] + 2, self.hit_box[2] - 4, self.hit_box[3] - 4)
        py.draw.rect(renderer.screen, self.inside_colour, new_hit_box)

    # ================================================================================================
    #  run -- runs the button, and returns wether it is being pressed or not
    #
    #      Controls the button's tick, by drawing the button, updating self.moused, and returning
    #		True if it being clicked on.
    #
    #  INPUT:  none
    #
    #  RETURNS:  none
    #
    #  CREATED: 27/07/2020
    # ================================================================================================
    def run(self):
        self.check_mouse(self.hit_box)

        if self.check_clicked():
            return True

    def render(self):
        self.display_box()
        self.display(self.message)

    def set_message(self, message):
        self.message = message
