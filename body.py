import sprite_controller
import renderer
import utilities
import math


class Body(sprite_controller.SpriteComponent):
    def __init__(self, sprite):
        super().__init__('body')
        self.sprite = sprite
        self.collider = None

        self.position = (0, 0)
        self.velocity = (0, 0)
        self.mass = 1
        self.gravity = 0
        self.friction = 1

    def start(self):
        self.collider = self.sprite.get_component('collider')

    # -------------------------------------------={ Velocity }=---------------------------------------------------------

    def change_velocity(self, change):
        new_change = utilities.check_vector2(change, float)

        self.velocity = utilities.add_vectors(new_change, self.velocity)

    def set_velocity(self, velocity):
        self.velocity = utilities.check_vector2(velocity, float)

    def set_speed(self, speed):
        new_speed = utilities.check_input(speed, float)

        direction = math.atan(self.velocity[0] / self.velocity[1]) % 360
        magnitude = new_speed

        self.velocity = utilities.angle_magnitude_to_vector(magnitude, direction)

    def get_speed(self):
        return math.sqrt(self.velocity[0] ** 2 + self.velocity[1] ** 2)

    def push(self, amount):
        self.set_speed(self.get_speed() + utilities.check_input(amount, float))

    def set_direction(self, angle):
        new_angle = utilities.check_input(angle, float)

        direction = new_angle % 360
        magnitude = math.sqrt(self.velocity[0] ** 2 + self.velocity[1] ** 2)

        self.velocity = utilities.angle_magnitude_to_vector(magnitude, direction)

    def rotate(self, angle):
        self.set_direction(self.get_direction() + utilities.check_input(angle, float))

    def get_direction(self):
        return math.atan(self.velocity[0] / self.velocity[1])

    # ------------------------------------------------------------------------------------------------------------------

    def check_collision(self):
        if len(self.collider.check_touching()) > 0:
            return True
        return False

    def move(self, position_change):
        new_position_change = utilities.check_vector2(position_change, float)

        # leave, stupid collisions
        previous_pos = self.position

        print(f'change: {new_position_change}')
        print(f'position: {self.position}')
        print(f'new: {utilities.add_vectors(new_position_change, self.position)}')

        self.position = utilities.add_vectors(new_position_change, self.position)

        if self.check_collision():
            # self.position = previous_pos
            pass

    def go_to(self, new_coords):
        new_new_coords = utilities.check_vector2(new_coords, float)

        if self.sprite.name == 'camera':
            self.position = [new_new_coords[0] - renderer.mid[0], new_new_coords[1] - renderer.mid[1]]
        else:
            self.position = new_new_coords

    def apply_force(self, force):
        new_force = utilities.check_vector2(force, float)

        if force[0] != 0 or force[1] != 0:

            x_component = new_force[0] / self.mass
            y_component = new_force[1] / self.mass

            self.velocity = utilities.add_vectors(self.velocity, (x_component, y_component))

    # -------------------------------------------={ physics engine }=---------------------------------------------------

    def __apply_friction(self):
        self.velocity = (self.velocity[0] * (1 / self.friction), self.velocity[1] * (1 / self.friction))

    def physics_tick(self):
        self.apply_gravity()

        self.__apply_friction()

        if self.collider is not False and self.collider is not None:
            self.collider.update_collision()

        self.position = utilities.add_vectors(self.position, self.velocity)
        if self.collider is not False and self.collider is not None:
            self.collider.update_hit_box()

    def apply_gravity(self):
        self.apply_force((0, self.gravity))

    # ------------------------------------------------------------------------------------------------------------------

    def counter_gravity(self):
        self.apply_force((0, self.gravity * -1))

    def set_gravity(self, strength):
        new_strength = utilities.check_input(strength, float)

        if -100 > new_strength > 100:
            raise Exception(f'Gravity cannot be set to {new_strength}. Please set it to a float number between -100 and 100.')
        else:
            self.gravity = new_strength / 10

    def jump(self, force):
        self.move((0, -1))
        self.apply_force((0, -utilities.check_input(force, float)))

    def set_friction(self, amount):
        new_amount = utilities.check_input(amount, float)
        if new_amount > 0:
            self.friction = new_amount
        else:
            raise Exception(f'Friction must be greater than 0')

    def set_mass(self, mass):
        self.mass = utilities.check_input(mass, float)
