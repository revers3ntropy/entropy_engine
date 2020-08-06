import sprite_controller
import renderer
import fail_system
import utilities


class Body(sprite_controller.SpriteComponent):
    def __init__(self, sprite):
        super().__init__('body')
        self.sprite = sprite
        self.collider = None

        self.position = (0, 0)
        self.velocity = (0, 0)
        self.components = []
        self.mass = 1
        self.gravity = 0
        self.friction = 1

    def start(self):
        self.collider = self.sprite.get_component('collider')

    def change_velocity(self, x_component, y_component):
        self.velocity = utilities.add_vectors([x_component, y_component], self.velocity)

    def set_velocity(self, new_velocity):
        self.velocity = new_velocity

    def get_velocity(self):
        return self.velocity

    def check_collision(self):
        if len(self.collider.check_touching()) > 0:
            return True
        return False

    def move(self, position_change):
        previous_pos = self.position

        self.position = utilities.add_vectors(position_change, self.position)

        if self.check_collision():
            # self.position = previous_pos
            pass

    def go_to(self, new_coords):
        if self.sprite.get_name() == 'camera':
            self.position = [new_coords[0] - renderer.mid[0], new_coords[1] - renderer.mid[1]]
        else:
            self.position = new_coords

    def get_position(self):
        return self.position

    def apply_force(self, x_component, y_component):
        if x_component != 0 or y_component != 0:

            x_component = x_component / self.mass
            y_component = y_component / self.mass

            self.velocity = utilities.add_vectors(self.velocity, (x_component, y_component))

    def physics_tick(self):
        self.apply_gravity()

        self.velocity = (self.velocity[0] * (1 / self.friction), self.velocity[1] * (1 / self.friction))

        if self.collider is not False:
            self.collider.update_collision()

        self.position = utilities.add_vectors(self.position, self.velocity)
        if self.collider is not False:
            self.collider.update_hit_box()

    def apply_gravity(self):
        self.apply_force(0, self.gravity)

    def counter_gravity(self):
        self.apply_force(0, self.gravity * -1)

    def set_gravity(self, strength):
        try:
            strength = float(strength)
        except:
            fail_system.error('Gravity has to be of type float, not ' + str(type(strength)), 'body.Body.set_gravity() (4)')
            return False

        if -100 > strength > 100:
            fail_system.error('Gravity cannot be set to ' + str(
                strength) + '. Please set it to a float number between -100 and 100.', 'body.Body.set_gravity() (11)')
        else:
            self.gravity = strength / 10

    def jump(self, force):
        self.move((0, -1))
        self.apply_force(0, -force)
