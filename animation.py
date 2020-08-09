import sprite_controller
import image
import utilities
import fail_system


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
        render = utilities.check_input(render, image.Image, (f'Image must be of type py.image, not type {type(render)}', 'image.Image.set_image(image, number)'))
        if render is not False:
            new_number = utilities.check_input(number, int, (f'Number must be of type int, not type {type(number)}.',
                                                             'image.Image.set_image(image, number)'))
            if new_number is not False:
                self.renders[new_number] = render
                return self

    def set_animation(self, animation):
        new_animation = utilities.check_input(animation, list, (f'animation must be of type list, not type {type(animation)}',
                                                                'image.Image.set_animation(animation)'))
        if new_animation is not False:
            for i in range(len(new_animation)):
                self.set_render(animation[i], i)

    def set_animations_from_files(self, file_names):
        new_file_names = utilities.check_input(file_names, list, (f'File names must be of type list, not type {type(file_names)}.',
                                               'animation.Animation.set_animation_from_files(file_name, number) (1)'))
        if new_file_names is not False:

            for i in range(len(new_file_names)):

                new_file_name = utilities.check_input(file_names[i], str, (f'File names must contain type str, not type {type(file_names[i])}.',
                                                      'animation.Animation.set_animation_from_files(file_name, number) (6)'))
                if new_file_names is not False:
                    try:
                        new_image = image.Image()
                        new_image.set_image_from_file(str(new_file_names[i]))
                        self.renders.append(new_image)

                    except:
                        fail_system.error("File '" + str(new_file_name) + "' could not be found",
                                          'animation.Animation.set_image_from_files(file_name, number) (14)')

    def get_render(self, number):
        new_number = utilities.check_input(number, int, (f'Image number must be of type int, not type {type(number)}.',
                                                         'image.Image.set_current_image(number'))
        if new_number is not False:
            if new_number < 0 or new_number > len(self.renders):
                fail_system.error(f'Render {new_number} does not seem to exist. Make sure it is between 0 and {len(self.renders)}.', 'animation.Animation.get_render(number)')
            else:
                return self.renders[number]

    def __step_in_range(self, step_range):
        new_step_range = utilities.check_vector2(step_range, int, 'animation.Animation.step_animation')
        if new_step_range is not False:
            if new_step_range[0] < 0:
                fail_system.error(f'the first element of step animation range is too low ({new_step_range[0]}). '
                                  f'Please set it to a value greater than 0.',
                                  'animation.Animation.step_animation(step_range) (4)')
                return False

            if new_step_range[0] > new_step_range[1]:
                fail_system.error(
                    f'the first element of step animation range is higher than the second ({new_step_range[0]} > {new_step_range[1]}). '
                    f'Please set it to a value smaller than the second.',
                    'animation.Animation.step_animation(step_range) (6)')
                return False

            if step_range[1] > len(self.renders):
                fail_system.error(f'step range out of bounds: ({new_step_range[1]} > {len(self.renders)}. '
                                  f'Please set it to a smaller value.',
                                  'animation.Animation.step_animation(step_range) (6)')
                return False

            if self.current_render < new_step_range[1]:
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
        new_number = utilities.check_input(number, int, (f'Cannot go to animation {number}. Make sure that it is within '
                                                         f'the animation range, and of type int.', 'animation.Animation.go_to_animation(number)'))
        if new_number is not False:
            if new_number < 0 or new_number > len(self.renders):
                fail_system.error(f'Animation {number} does not exist. Needs to be in range 0 to {len(self.renders)}',
                                  'animation.Animation.go_to_animation(number)')
            else:
                self.current_render = new_number
                self.update_collider()

    def set_auto_step(self, value):
        if value in (True, False):
            self.auto_step = value
        else:
            fail_system.error(f'auto step cannot be set to {value}. Please set it to a bool.', 'animation.Animation.set_auto_step(value)')

    def update_collider(self):
        if self.collider is not False:
            # self.collider is set in the start method, so it won't register it in the starting value, False
            self.collider.update_hit_box()
