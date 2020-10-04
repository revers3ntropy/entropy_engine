import button
import typing
import pygame as py
import renderer
from hit_box import HitBox
import colour


class StandardButton(button.Buttons):
    def __init__(self):
        pos = (renderer.mid[0], renderer.mid[1])
        font = typing.retro_8x10
        message = 'button text'
        super().__init__(pos, font, 'standard button')
        self.message = message
        self.size_x = (typing.fonts[font][typing.size_x] + 5) * len(message)
        self.hit_box = HitBox(0, 0, 0, 0)

        self.selected_colour = colour.Colour((200, 200, 200))
        self.outside_colour = colour.Colour((180, 180, 180))
        self.inside_colour = colour.Colour(renderer.background_colour)

    def start(self):
        self.update_hit_box()

    def update_hit_box(self):
        pos = (self.x - self.size_x / 2 - 7, self.x - typing.fonts[self.font][typing.size_y] / 2 - 7)
        size = (self.size_x + 14, typing.fonts[self.font][typing.size_y] + 14)
        self.hit_box = HitBox(pos[0], pos[1], size[0], size[1])

    # ================================================================================================
    #  display_box -- draws a box around the button
    #
    #      Uses the hit box to draw two rectangles of slightly different sizes on top of each other,
    #		thus drawing a background and outline to the button. Also is effected by self.moused
    #		which is if the button is being touched by the cursor.
    #
    #  INPUT:  none
    #
    #  RETURNS:  none
    #
    # ================================================================================================
    def display_box(self):
        if self.moused:
            py.draw.rect(renderer.screen, self.selected_colour.colour, self.hit_box)
        else:
            py.draw.rect(renderer.screen, self.outside_colour.colour, self.hit_box)

        new_hit_box = (self.hit_box.x() + 2, self.hit_box.y() + 2, self.hit_box.size_x() - 4, self.hit_box.size_y() - 4)
        py.draw.rect(renderer.screen, self.inside_colour.colour, new_hit_box)

    # ================================================================================================
    #  run -- runs the button, and returns whether it is being pressed or not
    #
    #      Controls the button's tick, by drawing the button, updating self.moused, and returning
    #		True if it being clicked on.
    #
    #  INPUT:  none
    #
    #  RETURNS:  none
    #
    # ================================================================================================
    def run(self):
        self.check_mouse(self.hit_box)

        if self.check_clicked():
            return True

    def render(self):
        self.display_box()
        self.display(self.message)

    def set_message(self, message):
        self.message = str(message)
