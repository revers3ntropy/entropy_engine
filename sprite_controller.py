list_of_sprites = []


def get_sprite(name):
    for i in list_of_sprites:
        if i.get_name() == name:
            return i
    return False


def init_sprites():
    for sprite in list_of_sprites:
        for component in sprite.get_components():
            component.start()


def update_sprites():
    for sprite in list_of_sprites:
        if sprite.get_name() != 'camera':
            for component in sprite.get_components():
                c_type = component.get_type()
                if c_type == 'body':
                    component.physics_tick()
                elif c_type == 'script':
                    component.tick_script()

    # so that the sprite can't move after the camera has been updated
    for component in list_of_sprites[0].get_components():
        c_type = component.get_type()
        if c_type == 'script':
            component.tick_script()
        elif c_type == 'body':
            component.physics_tick()


class SpriteComponent:
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type
