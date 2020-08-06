import sprite_controller
import hit_box
import fail_system


class Collider(sprite_controller.SpriteComponent):
    def __init__(self, sprite):
        super().__init__('collider')
        self.sprite = sprite
        self.sprite_scripts = None

        self.size_x = 10
        self.size_y = 10
        self.hit_box = hit_box.HitBox(0, 0, self.size_x, self.size_y)
        self.is_trigger = True
        self.solid = True
        self.bounce = 0

    def start(self):
        self.sprite_scripts = self.sprite.get_component('script')

    def __check_touching(self):
        touching = []
        for sprite in sprite_controller.list_of_sprites:
            if sprite.get_component('collider') is not False:
                if self.hit_box.check_hit_box_collision(sprite.get_component('collider').get_hit_box()):
                    touching.append(sprite)

        return touching

    def __collide(self, collision_sprite, body):
        if self.is_trigger:
            for i in self.sprite_scripts:
                try:
                    i.get_script().on_collision(collision_sprite)
                except:
                    pass

        if self.solid:
            body.move((body.get_velocity()[0] * -1, body.get_velocity()[1] * -1))
            body.set_velocity(body.get_velocity()[0] * -self.bounce, body.get_velocity()[1] * -self.bounce)

    def update_collision(self, body):

        self.update_hit_box(body)

        touching = self.__check_touching()
        for sprite in touching:
            self.__collide(sprite, body)

    def set_size(self, new_size):
        self.size_x = new_size[0]
        self.size_y = new_size[1]

    def update_hit_box(self, body):
        x = body.get_position()[0]
        y = body.get_position()[1]
        self.hit_box = hit_box.HitBox(x, y, self.size_x, self.size_y)

    def get_hit_box(self):
        return self.hit_box

    def set_is_trigger(self, value):
        try:
            new_value = bool(value)
            self.is_trigger = new_value
        except:
            fail_system.error('is_trigger cannot be set to ' + str(value) + '. Please set it to either True or False.', 'collider.set_is_trigger()')

    def set_solid(self, value):
        try:
            new_value = bool(value)
            self.solid = new_value
        except:
            fail_system.error('solid cannot be set to ' + str(value) + '. Please set it to either True or False.', 'collider.set_solid()')

    def set_bounce(self, value):
        try:
            bounce = float(value)
            if -1 > bounce > 1:
                fail_system.error('Bounce range is -1 to 1, which does not include ' + str(value), 'collider.set_bounce() (4)')
        except:
            fail_system.error('Bounce range is -1 to 1, which does not include ' + str(value), 'collider.set_bounce() (6)')
