class SpriteController:
    def __init__(self):
        self.list_of_sprites = []

    def get_sprite(self, name):
        for i in self.list_of_sprites:
            if i.name == name:
                return i
        return False

    def init_sprites(self):
        for sprite in self.list_of_sprites:
            for component in sprite.components:
                component.start()

    def update_sprites(self):
        for sprite in self.list_of_sprites:
            if sprite.name != 'camera':
                for component in sprite.components:

                    c_type = component.type

                    if c_type == 'body':
                        component.physics_tick()
                    elif c_type == 'script':
                        component.tick_script()
                    elif c_type == 'animation':
                        component.tick()

        # so that the sprite can't move after the camera has been updated
        for component in self.list_of_sprites[0].components:

            c_type = component.type

            if c_type == 'script':
                component.tick_script()
            elif c_type == 'body':
                component.physics_tick()


class SpriteComponent:
    def __init__(self, type):
        self.type = type
