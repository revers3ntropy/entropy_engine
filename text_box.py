import button
import typing
import pygame as py
import global_data
import curser
import renderer


class TextButton(button.Buttons):
    # ================================================================================================
    #  __init__
    #
    #  INPUT:  x, y - int - coordinates of the Buttons
    #		   font - int - which font should be used
    #		   initial_message - string - the message to be displayed when the button generates
    #		   colour1 - tuple[3, int] - colour of the boarder of the text-box
    #		   colour2 - tuple[3, int] - colour of the inside of the text-box
    #		   max_length - int - the maximum number of characters the text-box can hold, also size
    #		   selected_colour - tuple[3, int] - the colour the boarder of the text-box should be
    #											 when the mouse is over it
    #
    #  RETURNS:  none
    #
    #  CREATED: 27/07/2020
    # ================================================================================================
    def __init__(self):
        pos = (renderer.mid_x, renderer.mid_y)
        font = typing.retro_8x10
        initial_message = 'text box'
        max_length = len(initial_message)
        super().__init__(pos, font, 'text box')
        self.size_x = (typing.fonts[font][typing.size_x] + 5) * max_length
        self.hit_box = (
            self.x - self.size_x / 2 - 5, self.y - typing.fonts[self.font][typing.size_y] / 2 - 5, self.size_x + 10,
            typing.fonts[self.font][typing.size_y] + 10)
        self.message = initial_message
        self.initial_message = initial_message
        self.outside_colour = (100, 100, 100)
        self.inside_colour = (200, 200, 200)
        self.selected_colour = (175, 175, 175)
        self.selected = False
        self.max_length = max_length

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
            py.draw.rect(renderer.screen, self.selected_colour, self.hit_box)
        else:
            py.draw.rect(renderer.screen, self.outside_colour, self.hit_box)
        new_hit_box = (self.hit_box[0] + 2, self.hit_box[1] + 2, self.hit_box[2] - 4, self.hit_box[3] - 4)
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
        if self.selected and global_data.typing_sticky_keys <= 0:
            character = ''
            keys = py.key.get_pressed()
            for i in range(len(keys)):
                try:
                    if keys[typing.typeable_characters_py_game[i]]:
                        character = typing.typeable_characters[i]
                        global_data.typing_sticky_keys = 20
                except IndexError:
                    pass

            if keys[py.K_BACKSPACE]:
                global_data.typing_sticky_keys = 10
                self.message = self.remove_last_character_from_message()

            if keys[py.K_KP_ENTER]:
                global_data.typing_sticky_keys = 50
                self.selected = False
                global_data.writing = False

            if keys[py.K_SPACE]:
                global_data.typing_sticky_keys = 10
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
