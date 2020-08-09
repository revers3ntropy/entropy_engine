import body
import image
import script
import fail_system
import collider
import utilities
import tag
import animation


class Sprite:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.components = []

        self.tag = ''

    def add_component(self, type_):
        new_component = None
        if type_ == 'body' and self.get_component('body') is False:
            new_component = body.Body(self)
        elif type_ == 'image' and self.get_component('image') is False:
            new_component = image.Image()
        elif type_ == 'script':
            new_component = script.Script()
        elif type_ == 'collider':
            new_component = collider.Collider(self)
        elif type_ == 'animation':
            new_component = animation.Animation(self)

        if new_component is not None:
            self.components.append(new_component)
            return new_component
        else:
            fail_system.error(f"component type {type(type_)} does not exist", 'sprite.Sprite.add_component()')

    def get_component(self, type_):
        new_type = utilities.check_input(type_, str, (f'type cannot be of type {type(type_)}, must be of type str.', 'sprite.get_component(type)'))
        if new_type is not False:
            if new_type == 'script':
                scripts = []
                for component in self.components:
                    if component.type == new_type:
                        scripts.append(component)
                return scripts
            else:

                for component in self.components:
                    if component.type == new_type:
                        return component
                return False

    def change_name(self, new_name):
        new_new_name = utilities.check_input(new_name, str, (f'new_name must be of type str, not {type(new_name)}', 'sprite.change_name(new_name)'))
        if new_new_name is not False:
            self.name = new_new_name

    def remove_component(self, type):
        new_type = utilities.check_input(type, str, (f'Component type must be of type str, not {type(type)}.', 'sprite.Sprite.remove_component(type) (1)'))
        if new_type is not False:
            component = self.get_component(new_type)
            if component is False:
                fail_system.error(f'Component {new_type} could not be found. Make sure you have initialised it, and spelt it correctly.', 'sprite.Sprite.remove_component(type) (5)')
                return False
            else:
                # remove_component
                pass

    def set_tag(self, tag_):
        new_tag = utilities.check_input(tag_, tag.Tag, (f'Tag must of of type Tag, not of type {type(tag_)}.', 'sprite.Sprite.set_tag(tag_)'))
        if new_tag is not False:

            self.tag = new_tag
