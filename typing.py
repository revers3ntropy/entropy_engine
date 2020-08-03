import pygame as py
import renderer as renderer

# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : typing.py
#
#                                       Created : July 25, 2020
#
#                                   Last Update : July 25, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                               Controls the typing function of the program.
#
# ------------------------------------------------------------------------------------------------
#
# Imports:
# 	pygame
#	renderer
#
# ------------------------------------------------------------------------------------------------
#
#	write           - writes the contents of a string on the screen, centered
#	write_from_left - writes a string on the screen from the left
#
# ================================================================================================


# which characters are capable of being typed by this system
typeable_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# the pygame codes of all typeable characeters
typeable_characters_py_game = [py.K_a, py.K_b, py.K_c, py.K_d, py.K_e, py.K_f, py.K_g, py.K_h, py.K_i, py.K_j, py.K_k,
                               py.K_l,
                               py.K_m, py.K_n, py.K_o, py.K_p, py.K_q, py.K_r, py.K_s, py.K_t, py.K_u, py.K_v, py.K_w,
                               py.K_x,
                               py.K_y, py.K_z, py.K_1, py.K_2, py.K_3, py.K_4, py.K_5, py.K_6, py.K_7, py.K_8, py.K_9,
                               py.K_0]

# codes for each letter
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10
k = 11
l = 12
m = 13
n = 14
o = 15
p = 16
q = 17
r = 18
s = 19
t = 20
u = 21
v = 22
w = 23
x = 24
y = 25
z = 26

# codes for the size of the font, in pixels
size_x = 27
size_y = 28

# codes for the names of the fonts
chaos_14x16 = 29
retro_8x10 = 30

# data for the image and size for each font
fonts = {
    chaos_14x16: {
        size_x: 28,
        size_y: 32,
        'a': py.image.load('graphics/chaos_14x16/A.png'),
        'b': py.image.load('graphics/chaos_14x16/B.png'),
        'c': py.image.load('graphics/chaos_14x16/C.png'),
        'd': py.image.load('graphics/chaos_14x16/D.png'),
        'e': py.image.load('graphics/chaos_14x16/E.png'),
        'f': py.image.load('graphics/chaos_14x16/F.png'),
        'g': py.image.load('graphics/chaos_14x16/G.png'),
        'h': py.image.load('graphics/chaos_14x16/H.png'),
        'i': py.image.load('graphics/chaos_14x16/I.png'),
        'j': py.image.load('graphics/chaos_14x16/J.png'),
        'k': py.image.load('graphics/chaos_14x16/K.png'),
        'l': py.image.load('graphics/chaos_14x16/L.png'),
        'm': py.image.load('graphics/chaos_14x16/M.png'),
        'n': py.image.load('graphics/chaos_14x16/N.png'),
        'o': py.image.load('graphics/chaos_14x16/O.png'),
        'p': py.image.load('graphics/chaos_14x16/P.png'),
        'q': py.image.load('graphics/chaos_14x16/Q.png'),
        'r': py.image.load('graphics/chaos_14x16/R.png'),
        's': py.image.load('graphics/chaos_14x16/S.png'),
        't': py.image.load('graphics/chaos_14x16/T.png'),
        'u': py.image.load('graphics/chaos_14x16/U.png'),
        'v': py.image.load('graphics/chaos_14x16/V.png'),
        'w': py.image.load('graphics/chaos_14x16/W.png'),
        'x': py.image.load('graphics/chaos_14x16/X.png'),
        'y': py.image.load('graphics/chaos_14x16/Y.png'),
        'z': py.image.load('graphics/chaos_14x16/Z.png'),
        '-': py.image.load('graphics/chaos_14x16/-.png'),
        '/': py.image.load('graphics/chaos_14x16/forward_slash.png'),
        '!': py.image.load('graphics/chaos_14x16/!.png'),
        '?': py.image.load('graphics/chaos_14x16/?.png'),
        '@': py.image.load('graphics/chaos_14x16/@.png'),
        '#': py.image.load('graphics/chaos_14x16/#.png'),
        '^': py.image.load('graphics/chaos_14x16/^.png'),
        '=': py.image.load('graphics/chaos_14x16/=.png'),
        '+': py.image.load('graphics/chaos_14x16/+.png'),
        '_': py.image.load('graphics/chaos_14x16/_.png'),
        ':': py.image.load('graphics/chaos_14x16/;.png'),  # wrong file, I know
        '0': py.image.load('graphics/chaos_14x16/0.png'),
        '1': py.image.load('graphics/chaos_14x16/1.png'),
        '2': py.image.load('graphics/chaos_14x16/2.png'),
        '3': py.image.load('graphics/chaos_14x16/3.png'),
        '4': py.image.load('graphics/chaos_14x16/4.png'),
        '5': py.image.load('graphics/chaos_14x16/5.png'),
        '6': py.image.load('graphics/chaos_14x16/6.png'),
        '7': py.image.load('graphics/chaos_14x16/7.png'),
        '8': py.image.load('graphics/chaos_14x16/8.png'),
        '9': py.image.load('graphics/chaos_14x16/9.png'),
    },
    retro_8x10: {
        size_x: 16,
        size_y: 20,
        'a': py.image.load('graphics/retro_8x10/A.png'),
        'b': py.image.load('graphics/retro_8x10/B.png'),
        'c': py.image.load('graphics/retro_8x10/C.png'),
        'd': py.image.load('graphics/retro_8x10/D.png'),
        'e': py.image.load('graphics/retro_8x10/E.png'),
        'f': py.image.load('graphics/retro_8x10/F.png'),
        'g': py.image.load('graphics/retro_8x10/G.png'),
        'h': py.image.load('graphics/retro_8x10/H.png'),
        'i': py.image.load('graphics/retro_8x10/I.png'),
        'j': py.image.load('graphics/retro_8x10/J.png'),
        'k': py.image.load('graphics/retro_8x10/K.png'),
        'l': py.image.load('graphics/retro_8x10/L.png'),
        'm': py.image.load('graphics/retro_8x10/M.png'),
        'n': py.image.load('graphics/retro_8x10/N.png'),
        'o': py.image.load('graphics/retro_8x10/O.png'),
        'p': py.image.load('graphics/retro_8x10/P.png'),
        'q': py.image.load('graphics/retro_8x10/Q.png'),
        'r': py.image.load('graphics/retro_8x10/R.png'),
        's': py.image.load('graphics/retro_8x10/S.png'),
        't': py.image.load('graphics/retro_8x10/T.png'),
        'u': py.image.load('graphics/retro_8x10/U.png'),
        'v': py.image.load('graphics/retro_8x10/V.png'),
        'w': py.image.load('graphics/retro_8x10/W.png'),
        'x': py.image.load('graphics/retro_8x10/X.png'),
        'y': py.image.load('graphics/retro_8x10/Y.png'),
        'z': py.image.load('graphics/retro_8x10/Z.png'),
        '-': py.image.load('graphics/retro_8x10/-.png'),
        '/': py.image.load('graphics/retro_8x10/slash.png'),
        '!': py.image.load('graphics/retro_8x10/!.png'),
        '?': py.image.load('graphics/retro_8x10/?.png'),
        '@': py.image.load('graphics/retro_8x10/@.png'),
        '#': py.image.load('graphics/retro_8x10/#.png'),
        '^': py.image.load('graphics/retro_8x10/^.png'),
        '=': py.image.load('graphics/retro_8x10/=.png'),
        '+': py.image.load('graphics/retro_8x10/+.png'),
        '_': py.image.load('graphics/retro_8x10/_.png'),
        ':': py.image.load('graphics/retro_8x10/;.png'),  # wrong file, I know
        '0': py.image.load('graphics/retro_8x10/0.png'),
        '1': py.image.load('graphics/retro_8x10/1.png'),
        '2': py.image.load('graphics/retro_8x10/2.png'),
        '3': py.image.load('graphics/retro_8x10/3.png'),
        '4': py.image.load('graphics/retro_8x10/4.png'),
        '5': py.image.load('graphics/retro_8x10/5.png'),
        '6': py.image.load('graphics/retro_8x10/6.png'),
        '7': py.image.load('graphics/retro_8x10/7.png'),
        '8': py.image.load('graphics/retro_8x10/8.png'),
        '9': py.image.load('graphics/retro_8x10/9.png'),
    }
}


# ================================================================================================
#  write -- writes a string passed in as images on the screen
#
#      Splits and goes through a passed in string of characters and blits them onto the pygame
#		screen object. Writes the middle character at the given x-pos.
#
#  INPUT:  font    - int   - the code for the font to be used
#  	  	   message - str   - a string which contains the message to be displayed
#		   pos     - tuple - the position of the message to be displayed
#
#  RETURNS:  none
#
#  CREATED: 25/07/2020
# ================================================================================================
def write(font, message, pos):
    my_font = fonts[font]
    message = str.lower(message)
    if len(message) > 0:
        for i in range(len(message)):
            if message[i] != ' ':
                letter_image = my_font[message[i]]
                pos_y = pos[1] - my_font[size_y] / 2
                pos_x = (i - (len(message) / 2)) * (my_font[size_x] + 5) + pos[0]
                renderer.screen.blit(letter_image, (pos_x, pos_y))


# ================================================================================================
#  write -- writes a string passed in as images on the screen
#
#      Splits and goes through a passed in string of characters and blits them onto the pygame
#		screen object. Writes the first character at the given x-pos.
#
#  INPUT:  font    - int   - the code for the font to be used
#  	  	   message - str   - a string which contains the message to be displayed
#		   pos     - tuple - the position of the message to be displayed
#
#  RETURNS:  none
#
#  CREATED: 25/07/2020
# ================================================================================================
def write_from_left(font, message, pos):
    my_font = fonts[font]
    message = str.lower(message)
    if len(message) > 0:
        for i in range(len(message)):
            if message[i] != ' ':
                letter_image = my_font[message[i]]
                pos_y = pos[1] - my_font[size_y] / 2
                pos_x = i * (my_font[size_x] + 20) + pos[0]
                renderer.screen.blit(letter_image, (pos_x, pos_y))
