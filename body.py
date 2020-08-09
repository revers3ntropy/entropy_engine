import sprite_controller
import renderer
import fail_system
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
        new_change = utilities.check_vector2(change, float, 'body.Body.change_velocity(change)')
        if new_change is not False:

            self.velocity = utilities.add_vectors(new_change, self.velocity)

    def set_velocity(self, velocity):
        new_velocity = utilities.check_vector2(velocity, float, 'body.Body.set_velocity(velocity)')
        if new_velocity is not False:

            self.velocity = new_velocity

    def set_speed(self, speed):
        new_speed = utilities.check_input(speed, float, 'body.Body.set_velocity(velocity)')
        if new_speed is not False:

            direction = math.atan(self.velocity[0] / self.velocity[1]) % 360
            magnitude = new_speed

            self.velocity = utilities.angle_magnitude_to_vector(magnitude, direction)

    def get_speed(self):
        return math.sqrt(self.velocity[0] ** 2 + self.velocity[1] ** 2)

    def push(self, amount):
        new_amount = utilities.check_input(amount, float, (f'Cannot push by {amount}. Make sure it is of type float.', 'body.Body.push(amount)'))
        if new_amount is not False:
            self.set_speed(self.get_speed() + new_amount)

    def set_direction(self, angle):
        new_angle = utilities.check_input(angle, float, 'body.Body.set_velocity(velocity)')
        if new_angle is not False:

            direction = new_angle % 360
            magnitude = math.sqrt(self.velocity[0] ** 2 + self.velocity[1] ** 2)

            self.velocity = utilities.angle_magnitude_to_vector(magnitude, direction)

    def rotate(self, angle):
        new_angle = utilities.check_input(angle, float, (f'Cannot rotate velocity by {angle}. Make sure it is of type int', 'body.Body.rotate(angle)'))
        if new_angle is not None:

            self.set_direction(self.get_direction() + angle)

    def get_direction(self):
        return math.atan(self.velocity[0] / self.velocity[1])

    # ------------------------------------------------------------------------------------------------------------------

    def check_collision(self):
        if len(self.collider.check_touching()) > 0:
            return True
        return False

    def move(self, position_change):
        new_position_change = utilities.check_vector2(position_change, float, 'body.Body.move(position_change)')
        if new_position_change is not False:

            previous_pos = self.position

            self.position = utilities.add_vectors(new_position_change, self.position)

            if self.check_collision():
                #self.position = previous_pos
                pass

    def go_to(self, new_coords):
        new_new_coords = utilities.check_vector2(new_coords, float, 'body.Body.go_to(new_coords)')
        if new_new_coords is not False:

            if self.sprite.name == 'camera':
                self.position = [new_new_coords[0] - renderer.mid[0], new_new_coords[1] - renderer.mid[1]]
            else:
                self.position = new_new_coords

    def apply_force(self, force):
        new_force = utilities.check_vector2(force, float, 'body.Body.apply_force(force)')
        if new_force is not False:

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
        new_strength = utilities.check_input(strength, float, (f'strength must be of type float, not type {type(strength)}.', 'body.Body.set_gravity'))

        if -100 > new_strength > 100:
            fail_system.error(f'Gravity cannot be set to {new_strength}. Please set it to a float number between -100 and 100.', 'body.Body.set_gravity() (11)')
        else:
            self.gravity = new_strength / 10

    def jump(self, force):
        new_force = utilities.check_input(force, float, (f'force has to be of type float, not type {type(force)}.', 'body.Body.jump(force)'))
        if new_force is not False:

            self.move((0, -1))
            self.apply_force((0, -new_force))

    def set_friction(self, amount):
        new_amount = utilities.check_input(amount, float, (f'friction cannot be set to type {type(amount)}. Must be of type float.', 'body.Body.set_friction'))
        if new_amount is not False:
            if new_amount > 0:
                print(new_amount)
                self.friction = new_amount

    def set_mass(self, mass):
        new_mass = utilities.check_input(mass, float, (f'Mass must be of type float, not {type(mass)}.', 'body.Body.set_mass(mass)'))
        if new_mass is not False:
            self.mass = new_mass
