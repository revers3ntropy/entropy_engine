import sprite_controller
import math
import renderer


class Body(sprite_controller.SpriteComponent):
    def __init__(self):
        super().__init__('body')
        self.position = (renderer.mid_x, renderer.mid_y)
        self.velocity = (0, 0)
        self.components = []
        self.mass = 1
        self.gravity = 1
        self.friction = 1

    def change_velocity(self, speed_change, direction_change):
        self.velocity = (self.velocity[0] + speed_change, self.velocity[1] + direction_change)

    def set_velocity(self, new_speed, new_direction):
        self.velocity = (new_speed, new_direction)

    def get_velocity(self):
        return self.velocity

    def move(self, position_change):
        self.position = (self.position[0] + position_change[0], self.position[1] + position_change[1])

    def go_to(self, new_coords):
        self.position = new_coords

    def get_position(self):
        return self.position

    def apply_force(self, magnitude, angle):
        acceleration = magnitude / self.mass

        x_component = acceleration * math.sin(angle)  # trig to get the components of the vector
        y_component = acceleration * math.cos(angle)
        v2 = (x_component, y_component)
        x_component = self.velocity[0] * math.sin(self.velocity[1])  # trig to get the components of the vector
        y_component = self.velocity[0] * math.cos(self.velocity[1])
        v1 = (x_component, y_component)

        new_v = (v1[0] + v2[0], v1[1] + v2[1])

        new_magnitude = math.sqrt(new_v[0] ** 2 + new_v[1] ** 2)
        new_angle = math.acos(new_v[1] / new_magnitude)

        self.velocity = (new_magnitude, new_angle)

    def physics_tick(self):
        x_component = self.velocity[0] * math.sin(self.velocity[1])  # trig to get the components of the vector
        y_component = self.velocity[0] * math.cos(self.velocity[1])
        self.position = (self.position[0] + x_component, self.position[1] + y_component)

        self.velocity = (self.velocity[0] * (1 / self.friction), self.velocity[1])
