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
# global_function_1 - what this function does
#
# class 'preset' - what this class does
#   function_1 - what this function does
#
# ================================================================================================


class CompositeCollider(sprite_controller.SpriteComponent):
    def __init__(self, sprite):
        super().__init__('composite collider')
        self.sprite = sprite
        self.colliders = []

    def add_rect_collider(self):
        self.colliders.append(collider.Collider(self.sprite))
