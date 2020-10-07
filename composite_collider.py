# ================================================================================================
# |------------------------------------={ Entropy Engine }=----------------------------------------|
# ================================================================================================
#
#                                   Programmers : Joseph Coppin
#
#                                     File Name : composite_collider.py
#
#                                       Created : October 5, 2020
#
# ------------------------------------------------------------------------------------------------
#
#   Imports:
import collider
import sprite_controller
#
# ------------------------------------------------------------------------------------------------
#
#                        Controls the composite collider sprite component.
#
# ------------------------------------------------------------------------------------------------
#
# ================================================================================================


class CompositeCollider(sprite_controller.SpriteComponent):
    def __init__(self, sprite):
        super().__init__('composite collider')
        self.sprite = sprite
        self.colliders = []

    def add_rect_collider(self):
        self.colliders.append(collider.Collider(self.sprite))

    def update_colliders(self):
        for collider_ in self.colliders:
            collider_.update_collision()

    def update_hit_boxes(self):
        for collider_ in self.colliders:
            collider_.update_hit_box()
