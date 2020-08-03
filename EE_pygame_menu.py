import typing
import pygame as py
import global_data
import curser
import renderer
import ui_controller


# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : buttons.py
#
#                                       Created : July 27, 2020
#
#                                   Last Update : July 31, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                           Contains the general menu object classes.
#
# ------------------------------------------------------------------------------------------------
#
# Imports:
# 	typing
#	pygame
#
# ------------------------------------------------------------------------------------------------
#
# class 'Buttons' functions:
#	__init__
#	display       - displays the buttons current message
#	check_mouse   - checks whether or not the mouse is colliding with the button object
#	check_clicked - checks whether or not the button has been clicked
#
# class 'StandardButton(Buttons)' functions:
#	__init__
#	run       - controls displaying and pressing the button
#
# class 'SwitchButton(Buttons)' functions:
#	__init__
#	run          - controls displaying and pressing the button
#	switch_state - flips through the buttons possible states
#
# class 'TextButton(Buttons)' functions:
#	__init__
#	display_box     - Displays a box around the button, with a boarder
#	check_selected  - checks if the text box should be selected or not
#	remove_last_... - removes the last character from the message (backspace)
#	check_message   - updates the message based on keyboard inputs
#	run			    - controls the object
#
# class 'TextBoxWithCheck' functions:
#	__init__
#	display_box     - Displays a box around the button, with a boarder based on message
#	check_selected  - checks if the text box should be selected or not
#	remove_last_... - removes the last character from the message (backspace)
#	check_message   - updates the message based on keyboard inputs
#	run			    - controls the object
#
# ================================================================================================
class Buttons(ui_controller.UIComponent):
    # ================================================================================================
    #  __init__
    #
    #  INPUT:  x, y - int - the coordinates of the button, from the center
    #		   font -  int  - what font should the button use
    #
    #  RETURNS:  none
    #
    #  CREATED: 27/07/2020
    # ================================================================================================
    def __init__(self, pos, font, type):
        super().__init__(type)
        self.x = pos[0]
        self.y = pos[1]
        self.font = font
        self.moused = False

    # ================================================================================================
    #  display -- writes the message of the button on the screen
    #
    #  INPUT:  message - string -  what should be displayed
    #
    #  RETURNS:  none
    #
    #  CREATED: 27/07/2020
    # ================================================================================================
    def display(self, message):
        typing.write(self.font, message, (self.x, self.y))

    # ================================================================================================
    #  check_mouse -- returns whether or not the mouse is touching the button
    #
    #  INPUT:  hit_box - tuple(4, int)- the hit-box of the button, or the hit-box of where you want to check
    #
    #  RETURNS:  bool - is the mouse touching the button
    #
    #  CREATED: 27/07/2020
    # ================================================================================================
    def check_mouse(self, hit_box):
        if curser.check_mouse_collision(hit_box):
            self.moused = True
        else:
            self.moused = False

    # ================================================================================================
    #  check_clicked -- returns wether or not the button is being clicked or not
    #
    #      checks if the button is being touched by the mouse, and then if the program has regestered
    #		a new click.
    #
    #  INPUT:  none
    #
    #  RETURNS:  bool - whether or not the button has been pressed
    #
    #  CREATED: 27/07/2020
    # ================================================================================================
    def check_clicked(self):
        if self.moused and curser.check_new_click():
            return True
        return False

    def set_coordinates(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]

    def set_font(self, new_font):
        self.font = new_font


class StandardButton(Buttons):
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


class SwitchButton(Buttons):  # not used in this project, but I might as well include it
    # ================================================================================================
    #  __init__
    #
    #  INPUT:  x, y - int - coordinates of the button from the center
    #		   font - int - what font should be used for the button
    #		   states - list[n, string] - all states the button could be in, displayed on the button
    #		   starting_state - int - which state should start on, normally 0
    #
    #  RETURNS:  none
    #
    #  CREATED: 00/00/2020
    # ================================================================================================
    def __init__(self, pos, font, states, starting_state):
        super().__init__(pos, font, 'switch button')
        self.states = states  # list of messages
        self.current_state = starting_state  # number to start on

        self.number_of_states = len(states)
        self.size_x = (typing.fonts[font][typing.size_x] + 5) * len(self.states[self.current_state])
        self.hit_box = (
            pos[0] - self.size_x / 2, pos[1] - typing.fonts[font][typing.size_y] / 2, self.size_x,
            typing.fonts[font][typing.size_y])

    # ================================================================================================
    #  update_states -- pushed the state forward one
    #
    #      moves the button forward one step, called when the button is pressed
    #
    #  INPUT:  none
    #
    #  RETURNS:  none
    #
    #  CREATED: 27/07/2020
    # ================================================================================================
    def update_state(self):
        if self.number_of_states > 2:
            if self.current_state >= self.number_of_states - 1:
                self.current_state = 1
            else:
                self.current_state += 1
            self.size_x = (typing.fonts[self.font][typing.size_x] + 5) * len(self.states[self.current_state])
            self.hit_box = (self.x - self.size_x / 2, self.y - typing.fonts[self.font][typing.size_y] / 2, self.size_x,
                            typing.fonts[self.font][typing.size_y])
        else:
            if self.current_state == 1:
                self.current_state = 0
            else:
                self.current_state = 1

    # ================================================================================================
    #  run -- controls the button
    #
    #  INPUT:  none
    #
    #  RETURNS:  self.current_state - string - the current state of the button
    #
    #  CREATED: 00/00/2020
    # ================================================================================================
    def run(self):
        self.check_mouse(self.hit_box)

        if self.check_clicked():
            self.update_state()

        return self.current_state

    def render(self):
        self.display(self.states[self.current_state])


class TextButton(Buttons):
    # ================================================================================================
    #  __init__
    #
    #  INPUT:  x, y - int - coodinates of the Buttons
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
    def __init__(self, pos, font, initial_message, colour1, colour2, max_length, selected_colour):
        super().__init__(pos, font, 'text box')
        self.size_x = (typing.fonts[font][typing.size_x] + 5) * max_length
        self.hit_box = (
            self.x - self.size_x / 2 - 5, self.y - typing.fonts[self.font][typing.size_y] / 2 - 5, self.size_x + 10,
            typing.fonts[self.font][typing.size_y] + 10)
        self.message = initial_message
        self.initial_message = initial_message
        self.outside_colour = colour1
        self.inside_colour = colour2
        self.selected_colour = selected_colour
        self.selected = False
        self.max_length = max_length

    # ================================================================================================
    #  display_box -- draws the box of the text-box
    #
    #      draws the two rectagles which make the text box based on the hitbox and wehter the mouse
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
    #  check_selected -- updates wether or not the text-box has been selected or not
    #
    #      checks if there has been a click, and wehter the text-box is being touched by the moused
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
    #  remove_last_character_from_message -- removes the last charater from the current message
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
    #      checks all keyboard inputs, abnd if one is in the list of typable charactes then it
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


class TextBoxWithCheck(Buttons):  # very similar to TextButton
    # ================================================================================================
    #  __init__
    #
    #  INPUT:  x, y - int - coodinates of the Buttons
    #		   font - int - which font should be used
    #		   initial_message - string - the message to be displayed when the button generates
    #		   max_length - int - the maximum number of characters the text-box can hold, also size
    #		   check - function - the function to check if the button should be red or green
    #
    #  RETURNS:  none
    #
    #  CREATED: 27/07/2020
    # ================================================================================================
    def __init__(self, pos, font, initial_message, max_length, check):
        super().__init__(pos, font, 'text box with check')
        self.size_x = (typing.fonts[font][typing.size_x] + 5) * max_length
        self.hit_box = (
            self.x - self.size_x / 2 - 5, self.y - typing.fonts[self.font][typing.size_y] / 2 - 5, self.size_x + 10,
            typing.fonts[self.font][typing.size_y] + 10)
        self.message = initial_message
        self.initial_message = initial_message
        self.selected = False
        self.max_length = max_length
        self.check_function = check
        self.correct = False

    # ================================================================================================
    #  display_box -- draws the box of the text-box
    #
    #      draws the two rectagles which make the text box based on the hitbox and wether the mouse
    #		is touching the text-box or not. The outline colour is determined by the result of
    #		running the self.check function
    #
    #  INPUT:  none
    #
    #  RETURNS:  none
    #
    #  CREATED: 27/07/2020
    # ================================================================================================
    def display_box(self):

        if self.check_function(self.message):
            self.correct = True
            colour = (50, 255, 50)
        else:
            self.correct = False
            colour = (255, 50, 50)

        py.draw.rect(renderer.screen, colour, self.hit_box)
        new_hit_box = (self.hit_box[0] + 2, self.hit_box[1] + 2, self.hit_box[2] - 4, self.hit_box[3] - 4)
        py.draw.rect(renderer.screen, (200, 200, 200), new_hit_box)

    # ================================================================================================
    #  check_selected -- updates wether or not the text-box has been selected or not
    #
    #      checks if there has been a click, and wehter the text-box is being touched by the moused
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
    #  remove_last_character_from_message -- removes the last charater from the current message
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
    #      checks all keyboard inputs, abnd if one is in the list of typable charactes then it
    #		adds it to the message. Also controls backspace, enter and space, which are all
    #		exceptions.
    #
    #  INPUT:  none
    #
    #  RETURNS:  none
    #
    #  CREATED: 27/07/2020
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

            if character != '':  # adds the input. tothe end of message if it is valid
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
