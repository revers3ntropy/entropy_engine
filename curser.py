import pygame as py
import global_data


# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : RE_pygame_menu
#
#                                     File Name : cursor.py
#
#                                       Created : August 31, 2020
#
#                                   Last Update : August 31, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                            Controls mouse collisions and clicks.
#
# ------------------------------------------------------------------------------------------------
#
# Imports:
#	pygame
#	global_data
#
# ------------------------------------------------------------------------------------------------
#
#	update_mouse_clicked  - updates the mouse clicks history
#	check_mouse_collision - checks if the cursor is colliding with a hit box passed in
#	check_new_click		  - checks for new mouse click
#
# ================================================================================================

# ================================================================================================
#  update_mouse_clicked -- updates the mouse clicks history
#
#      Checks for a new mouse press, and based on that updates the global mouse click history.
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 27/07/2020
# ================================================================================================
def update_mouse_clicked():
    global_data.mouse_history = global_data.mouse_pressed
    if py.mouse.get_pressed()[0]:
        global_data.mouse_pressed = 1
    else:
        global_data.mouse_pressed = 0


# ================================================================================================
#  check_mouse_collision -- checks whether or not the cursor is in a hit-box passed in
#
#      Checks whether or not the cursor is inside a rectangle passed in, and returns te result.
#
#  INPUT:  hit_box - tuple - a four-dimensional vector containing the coordinates of the top
#							 left corner of the rect, and the size of the rect.
#
#  RETURNS:  none
#
#  CREATED: 27/07/2020
# ================================================================================================
def check_mouse_collision(hit_box):
    py.event.get()
    mouse_pos = py.mouse.get_pos()
    if hit_box[0] < mouse_pos[0] < hit_box[0] + hit_box[2] and hit_box[1] < mouse_pos[1] < hit_box[1] + hit_box[3]:
        return True
    else:
        return False


# ================================================================================================
#  check_new_click -- checks whether or not a new click has been detected, as of the last update.
#
#      more detailed function description
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 00/00/2020
# ================================================================================================
def check_new_click():
    if py.mouse.get_pressed()[0] and not global_data.mouse_pressed:
        return True
    else:
        return False
