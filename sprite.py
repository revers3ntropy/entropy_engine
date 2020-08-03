import body
import image
import script
import fail_system


class Sprite:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.components = []

    def add_component(self, type):
        new_component = None
        if type == 'body' and self.get_component('body') is False:
            new_component = body.Body()
        elif type == 'image' and self.get_component('image') is False:
            new_component = image.Image()
        elif type == 'script':
            new_component = script.Script()

        if new_component is not None:
            self.components.append(new_component)
            return new_component
        else:
            fail_system.error("component type '" + str(type) + "' doesn't exist")

    def get_component(self, type):
        if type == 'script':
            components = []
            for component in self.components:
                if component.type == type:
                    components.append(component)
            return components
        else:
            for component in self.components:
                if component.type == type:
                    return component
            return False

    def get_name(self):
        return self.name

    def change_name(self, new_name):
        self.name = new_name

    def get_components(self):
        return self.components
