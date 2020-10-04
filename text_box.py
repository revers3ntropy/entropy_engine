import button
import typing
import pygame as py
import global_data
import curser
import renderer
from hit_box import HitBox
import colour


class TextButton(button.Buttons):
    def __init__(self):
        pos = renderer.mid
        font = typing.retro_8x10

        initial_message = 'text box'
        max_length = len(initial_message)
        self.message = initial_message
        self.initial_message = initial_message

        super().__init__(pos, font, 'text box')

        self.size_x = (typing.fonts[font][typing.size_x] + 5) * max_length
        self.hit_box = HitBox(
            self.x - self.size_x / 2 - 5, self.y - typing.fonts[self.font][typing.size_y] / 2 - 5, self.size_x + 10,
            typing.fonts[self.font][typing.size_y] + 10)

        self.selected_colour = colour.Colour((200, 200, 200))
        self.outside_colour = colour.Colour((180, 180, 180))
        self.inside_colour = colour.Colour(renderer.background_colour)

        self.selected = False
        self.max_length = max_length

    def start(self):
        pass

    # ================================================================================================
    #  display_box -- draws the box of the text-box
    #
    #      draws the two rectangles which make the text box based on the hit-box and whether the mouse
    #		is touching the text-box or not
    #
    #  INPUT:  none
    #
    #  RETURNS:  none
    #
    #  CREATED: 00/00/2020
    # ================================================================================================
    def display_box(self):
        if self.moused:
            py.draw.rect(renderer.screen, self.selected_colour, self.hit_box.hit_box)
        else:
            py.draw.rect(renderer.screen, self.outside_colour, self.hit_box.hit_box)
        new_hit_box = (self.hit_box.x + 2, self.hit_box.y + 2, self.hit_box.size_x - 4, self.hit_box.size_y - 4)
        py.draw.rect(renderer.screen, self.inside_colour, new_hit_box)

    # ================================================================================================
    #  check_selected -- updates whether or not the text-box has been selected or not
    #
    #      checks if there has been a click, and whether the text-box is being touched by the moused
    #		and then updates self.selected and global_data.writing.
    #
    #  INPUT:  none
    #
    #  RETURNS:  none
    #
    #  CREATED: 27/07/2020
    # ================================================================================================
    def check_selected(self):
        if curser.check_new_click():
            if self.moused:
                self.selected = True
                global_data.writing = True
            else:
                self.selected = False
                global_data.writing = False

    # ================================================================================================
    #  remove_last_character_from_message -- removes the last character from the current message
    #
    #      goes through the message and adds all but the last letter to a new list, which is returned
    #
    #  INPUT:  none
    #
    #  RETURNS:  new_message - string - the result of the removal
    #
    #  CREATED: 27/07/2020
    # ================================================================================================
    def remove_last_character_from_message(self):
        new_message = ''
        for i in range(len(self.message)):
            if i < len(self.message) - 1:
                new_message += self.message[i]
        return new_message

    # ================================================================================================
    #  check_message -- controls typing in the text-box
    #
    #      checks all keyboard inputs, and if one is in the list of typeable characters then it
    #		adds it to the message. Also controls backspace, enter and space, which are all
    #		exceptions.
    #
    #  INPUT:  none
    #
    #  RETURNS:  none
    #
    #  CREATED: 00/00/2020
    # ================================================================================================
    def check_message(self):
        if self.selected:
            character = ''
            keys = py.key.get_pressed()
            for i in range(len(keys)):
                try:
                    if keys[typing.typeable_characters_py_game[i]]:
                        if global_data.typing_last_key != typing.typeable_characters_py_game[i] or global_data.typing_sticky_keys <= 0:
                            character = typing.typeable_characters[i]
                            global_data.typing_sticky_keys = 20
                            global_data.typing_last_key = typing.typeable_characters_py_game[i]
                except IndexError:
                    pass

            if keys[py.K_BACKSPACE]:
                if global_data.typing_last_key != py.K_BACKSPACE or global_data.typing_sticky_keys <= 0:
                    global_data.typing_last_key = py.K_BACKSPACE
                    global_data.typing_sticky_keys = 10
                    self.message = self.remove_last_character_from_message()

            if keys[py.K_KP_ENTER]:
                global_data.typing_last_key = py.K_KP_ENTER
                global_data.typing_sticky_keys = 50
                self.selected = False
                global_data.writing = False

            if keys[py.K_SPACE]:
                if global_data.typing_last_key != py.K_SPACE or global_data.typing_sticky_keys <= 0:
                    global_data.typing_last_key = py.K_SPACE
                    global_data.typing_sticky_keys = 5
                    character = ' '

            if character != '':
                if len(self.message) < self.max_length:
                    if self.message == self.initial_message:
                        self.message = character
                    else:
                        self.message += character

    # ================================================================================================
    #  run -- controls the button
    #
    #      runs all checks and then returns the current message
    #
    #  INPUT:  none
    #
    #  RETURNS:  self.message - string - the current message the text-box has
    #
    #  CREATED: 27/07/2020
    # ================================================================================================
    def run(self):
        self.check_mouse(self.hit_box)
        self.check_selected()
        self.check_message()
        return self.message

    def render(self):
        self.display_box()
        self.display(self.message)
