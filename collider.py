import sprite_controller
import renderer
import hit_box


class Collider(sprite_controller.SpriteComponent):
    def __init__(self):
        super().__init__('collider')
        self.hit_box = hit_box.HitBox(renderer.mid_x, renderer.mid_y, 10, 10)
        self.is_trigger = False

    def check_touching(self):
        pass

