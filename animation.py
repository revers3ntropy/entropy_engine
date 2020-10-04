import sprite_controller
import image
import utilities


class Animation(sprite_controller.SpriteComponent):
    def __init__(self, sprite):
        super().__init__('animation')
        self.renders = []
        self.current_render = 0
        self.auto_step = False
        self.sprite = sprite
        self.collider = False

    def start(self):
        self.collider = self.sprite.get_component('collider')

    def tick(self):
        if self.auto_step:
            self.step(0)

    def set_render(self, render, number):
        render = utilities.check_input(render, image.Image)
        new_number = utilities.check_input(number, int)

        if new_number is not False:
            self.renders[new_number] = render
            return self

    def set_animation(self, animation):
        new_animation = utilities.check_input(animation, list)

        for i in range(len(new_animation)):
            self.set_render(animation[i], i)

    def set_animation_from_files(self, file_names):
        new_file_names = utilities.check_input(file_names, list)

        for i in range(len(new_file_names)):

            new_image = image.Image()
            new_image.set_image_from_file(str(file_names[i]))
            self.renders.append(new_image)

    def get_render(self, number):
        new_number = utilities.check_input(number, int)
        if new_number < 0 or new_number > len(self.renders):
            raise Exception(
                f'Render {new_number} does not seem to exist. Make sure it is between 0 and '
                f'{len(self.renders)}.')
        else:
            return self.renders[number]

    def __step_in_range(self, step_range):
        new_step_range = utilities.check_vector2(step_range, int)

        if new_step_range[0] < 0:
            raise Exception(
                f'the first element of step animation range is too low ({new_step_range[0]}). '
                f'Please set it to a value greater than 0.')

        elif new_step_range[0] > new_step_range[1]:
            raise Exception(
                f'the first element of step animation range is higher than the second ({new_step_range[0]} > {new_step_range[1]}). '
                f'Please set it to a value smaller than the second.')

        elif step_range[1] > len(self.renders):
            raise Exception(
                f'step range out of bounds: ({new_step_range[1]} > {len(self.renders)}. '
                f'Please set it to a smaller value.')

        elif self.current_render < new_step_range[1]:
            self.current_render += 1

        else:
            self.current_render = new_step_range[0]

    def step(self, step_range):
        if step_range == 0:

            # - 1 because otherwise it reaches len(self.renders), which throws an error, as it looks for the n+1th
            # element which doesn't exist
            if self.current_render < len(self.renders) - 1:
                self.current_render += 1

            else:
                self.current_render = 0

            self.update_collider()

        else:
            self.__step_in_range(step_range)

    def go_to_animation(self, number):
        new_number = utilities.check_input(number, int)

        if new_number < 0 or new_number > len(self.renders):
            raise Exception(
                f'Animation {number} does not exist. Needs to be in range 0 to {len(self.renders) - 1}')
        else:
            self.current_render = new_number
            self.update_collider()

    def set_auto_step(self, value):
        if value in (True, False):
            self.auto_step = value
        else:
            raise Exception(f'auto step cannot be set to {value}. Please set it to a bool.')

    def update_collider(self):
        if self.collider is not False:
            # self.collider is set in the start method, so it won't register it in the starting value, False
            self.collider.update_hit_box()
