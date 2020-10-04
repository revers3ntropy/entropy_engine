import typing
import curser
import ui_controller
import utilities


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
        if curser.check_mouse_collision(hit_box.get_hit_box()):
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
        new_coords = utilities.check_vector2(coordinates, float)

        self.x = new_coords[0]
        self.y = new_coords[1]

    def set_font(self, font):
        new_font = utilities.check_input(font, int)

        self.font = new_font
