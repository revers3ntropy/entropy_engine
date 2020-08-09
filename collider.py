import sprite_controller
import hit_box
import fail_system
import utilities


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
        for sprite in sprite_controller.list_of_sprites:
            if sprite.name != self.sprite.name:
                if sprite.get_component('collider') is not False:
                    if self.hit_box.check_hit_box_collision(sprite.get_component('collider').hit_box):
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
            self.body.set_velocity((self.body.velocity[0] * -self.bounce, self.body.velocity[1] * -self.bounce))

    def update_collision(self):
        for sprite in self.check_touching():
            self.__collide(sprite)

    def set_size(self, size):
        new_size = utilities.check_vector2(size, int, 'collider.Collider.set_size(size)')
        if new_size is not False:
            self.size_x = new_size[0]
            self.size_y = new_size[1]

    def update_hit_box(self):
        x = self.body.position[0]
        y = self.body.position[1]
        self.hit_box = hit_box.HitBox(x, y, self.size_x, self.size_y)

    def set_is_trigger(self, value):
        try:
            self.is_trigger = bool(value)
        except:
            fail_system.error('is_trigger cannot be set to ' + str(value) + '. Please set it to either True or False.', 'collider.set_is_trigger()')

    def set_solid(self, value):
        try:
            self.solid = bool(value)
        except:
            fail_system.error('solid cannot be set to ' + str(value) + '. Please set it to either True or False.', 'collider.set_solid()')

    def set_bounce(self, value):
        try:
            bounce = float(value)
            if -100 > bounce > 100:
                fail_system.error('Bounce range is -100 to 100, which does not include ' + str(value), 'collider.set_bounce() (4)')
            else:
                self.bounce = bounce
        except:
            fail_system.error('Bounce range is -1 to 1, which does not include ' + str(value), 'collider.set_bounce() (6)')
