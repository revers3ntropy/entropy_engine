import button
import renderer
import typing
from hit_box import HitBox
import fail_system
import utilities
import colour


class SwitchButton(button.Buttons):
    def __init__(self):
        pos = (renderer.mid[0], renderer.mid[1])
        font = typing.retro_8x10

        super().__init__(pos, font, 'switch button')

        self.states = ['Type 1', 'Type 2']  # list of messages
        self.current_state = 0  # number to start on
        self.number_of_states = len(self.states)

        self.size_x = 0
        self.hit_box = HitBox(0, 0, 0, 0)

        self.selected_colour = colour.Colour((200, 200, 200))
        self.outside_colour = colour.Colour((180, 180, 180))
        self.inside_colour = colour.Colour(renderer.background_colour)

    def start(self):
        self.update_hit_box()

    def update_hit_box(self):
        self.size_x = (typing.fonts[self.font][typing.size_x] + 5) * len(self.states[self.current_state])

        pos = (self.x - self.size_x / 2, self.y - typing.fonts[self.font][typing.size_y] / 2)
        size = (self.size_x, typing.fonts[self.font][typing.size_y])
        self.hit_box = HitBox(pos[0], pos[1], size[0], size[1])

    # moves the button forward one step, called when the button is pressed
    def update_state(self):
        if self.number_of_states > 2:
            if self.current_state >= self.number_of_states - 1:
                self.current_state = 1
            else:
                self.current_state += 1
        else:
            if self.current_state == 1:
                self.current_state = 0
            else:
                self.current_state = 1

    def run(self):
        self.check_mouse(self.hit_box)

        if self.check_clicked():
            self.update_state()

        return self.current_state

    def render(self):
        self.display(self.states[self.current_state])

    def set_states(self, list_of_states):
        self.states = list_of_states

    def set_starting_state(self, state):
        # for state based off its contents
        if type(state) == str:
            found = False
            for i in range(len(self.states)):
                if self.states[i] == state:
                    found = True
                    self.current_state = i

            if found is False:
                fail_system.error(f'State {str(state)} does not seem to exist.', 'switch_button.SwitchButton.set_starting_state(state) (8)')

        new_state = utilities.check_input(state, int, (f'state has to be of type str, not {type(state)}.',
                                                       'switch_button.SwitchButton.set_starting_state(state) (10)'))

        # for state based of place in list
        if new_state is not False:
            if new_state < 0 or new_state > len(self.states):
                fail_system.error(f'state number {new_state} does not seem to exist. Try making it between 0 and {len(self.states)}',
                                  'switch_button.SwitchButton.set_starting_state(state) (13)')
            else:
                self.current_state = new_state

    def get_current_state(self):
        return self.states[self.current_state]
