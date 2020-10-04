import sprite_controller
import hit_box
import utilities
import scene_manager
import pygame as py


class Collider(sprite_controller.SpriteComponent):
    def __init__(self, sprite):
        super().__init__('collider')
        self.sprite = sprite
        self.sprite_scripts = None
        self.body = None

        self.size_x = 10
        self.size_y = 10
        self.hit_box = hit_box.HitBox(0, 0, self.size_x, self.size_y)
        self.is_trigger = True
        self.solid = True
        self.bounce = 0

    def start(self):
        self.sprite_scripts = self.sprite.get_component('script')
        self.body = self.sprite.get_component('body')

    def check_touching(self):
        touching = []
        for sprite in scene_manager.scenes[scene_manager.active_scene].sprite_controller.list_of_sprites:

            if sprite.name != self.sprite.name:
                if sprite.get_component('collider') is not False:
                    if self.hit_box.check_hit_box_collision(
                            sprite.get_component('collider').hit_box):
                        touching.append(sprite)

        return touching

    def __move_back(self):
        self.body.move((-self.body.velocity[0], -self.body.velocity[1]))

    def __collide(self, collision_sprite):
        if collision_sprite.name == self.sprite.name:
            return False

        if self.is_trigger:
            for i in self.sprite_scripts:
                try:
                    i.script.on_collision(collision_sprite)
                except:
                    pass

        if self.solid and collision_sprite.get_component('collider').solid:
            self.__move_back()
            self.body.set_velocity(
                (self.body.velocity[0] * -self.bounce, self.body.velocity[1] * -self.bounce))

    def update_collision(self):
        for sprite in self.check_touching():
            self.__collide(sprite)

    def set_size(self, size):
        new_size = utilities.check_vector2(size, int)

        self.size_x = new_size[0]
        self.size_y = new_size[1]

    def update_hit_box(self):
        x = self.body.position[0]
        y = self.body.position[1]
        self.hit_box = hit_box.HitBox(x, y, self.size_x, self.size_y)

    def set_is_trigger(self, value):
        self.is_trigger = utilities.check_input(value, bool)

    def set_solid(self, value):
        self.solid = utilities.check_input(value, bool)

    def set_bounce(self, value):
        bounce = utilities.check_input(value, float)
        if -100 > bounce > 100:
            raise Exception(f'Bounce range is -100 to 100, which does not include {value}')
        self.bounce = bounce

    def get_moused(self):
        if self.hit_box.check_point_collision(py.mouse.get_pos()):
            return True
        return False

    def get_clicked(self):
        if self.get_moused() and py.mouse.get_pressed()[0]:
            return True
        return False
