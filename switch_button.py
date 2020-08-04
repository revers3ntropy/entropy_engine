import button
import renderer
import typing
import hit_box


class SwitchButton(button.Buttons):  # not used in this project, but I might as well include it
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
    def __init__(self):
        pos = (renderer.mid_x, renderer.mid_y)
        font = typing.retro_8x10
        super().__init__(pos, font, 'switch button')
        self.states = ['Type 1', 'Type 2']  # list of messages
        self.current_state = 0  # number to start on

        self.number_of_states = len(self.states)
        self.size_x = (typing.fonts[font][typing.size_x] + 5) * len(self.states[self.current_state])
        self.hit_box = hit_box.HitBox(pos[0] - self.size_x / 2, pos[1] - typing.fonts[font][typing.size_y] / 2,
                                      self.size_x, typing.fonts[font][typing.size_y])

    def start(self):
        pass

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
