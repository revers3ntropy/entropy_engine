import script
import EE_pygame_menu
import fail_system


class Element:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.components = []
        self.primary_component = None

    def add_component(self, type):
        new_component = None
        if type == 'script':
            new_component = script.Script()

        elif self.primary_component is None:
            if type == 'standard button':
                new_component = EE_pygame_menu.StandardButton()
                print('new: ' + str(new_component))

        if new_component is not None:
            if type in ('script', ''):
                self.components.append(new_component)
            else:
                self.primary_component = new_component

            return new_component
        else:
            fail_system.error("component type '" + str(type) + "' doesn't exist")

    def get_component(self, type):
        for component in self.components:
            if component.get_type() == type:
                return component
        return False

    def get_primary_component(self):
        return self.primary_component

    def get_name(self):
        return self.name

    def change_name(self, new_name):
        self.name = new_name

    def render(self):
        if self.primary_component is not None:
            self.primary_component.render()
