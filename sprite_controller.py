list_of_sprites = []


def get_sprite(name):
    for i in list_of_sprites:
        if i.get_name() == name:
            return i
    return False


def update_sprites():
    for sprite in list_of_sprites:
        for component in sprite.get_components():
            c_type = component.get_type()
            if c_type == 'script':
                component.tick_script()
            elif c_type == 'body':
                component.physics_tick()
            elif c_type == 'collider':
                component.update_collision()


class SpriteComponent:
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type
