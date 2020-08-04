import sprite_controller
import renderer
import hit_box


class Collider(sprite_controller.SpriteComponent):
    def __init__(self, sprite):
        super().__init__('collider')
        self.size_x = 10
        self.size_y = 10
        self.hit_box = hit_box.HitBox(renderer.mid_x, renderer.mid_y, self.size_x, self.size_y)
        self.is_trigger = False
        self.solid = True
        self.bounce = 0.01
        self.body = sprite.get_component('body')
        self.scripts = []
        if sprite.get_component('script') is not False:
            self.scripts = sprite.get_component('script')

    def check_touching(self):
        touching = []
        for sprite in sprite_controller.list_of_sprites:
            if sprite.get_component('collider') is not False:
                if self.hit_box.check_hit_box_collision(sprite.get_component('collider').get_hit_box().get_hit_box()):
                    touching.append(sprite)

        return touching

    def collide(self, sprite):
        if self.is_trigger:
            for i in self.scripts:
                try:
                    self.scripts[i].get_script().on_coliision(sprite)
                except:
                    pass

        if self.solid:
            self.body.set_velocity(self.body.get_velocity()[0] * self.bounce,
                                   self.body.get_velocity()[1] * self.bounce)

    def update_collision(self):
        self.update_hit_box()

        touching = self.check_touching()
        for sprite in touching:
            self.collide(sprite)

    def set_size(self, new_size):
        self.size_x = new_size[0]
        self.size_y = new_size[1]

    def update_hit_box(self):
        x = self.body.get_position()[0]
        y = self.body.get_position()[1]
        self.hit_box = hit_box.HitBox(x, y, self.size_x, self.size_y)

    def get_hit_box(self):
        return self.hit_box
