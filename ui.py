import script
import standard_button
import switch_button
import text_box
import text_box_with_check
import ui_text
import utilities


class Element:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.components = []
        self.primary_component = None
        self.state = True

    def add_component(self, type):
        new_component = None
        if type == 'script':
            new_component = script.ScriptComponent()

        elif self.primary_component is None:
            if type == 'standard button':
                new_component = standard_button.StandardButton()
            elif type == 'switch button':
                new_component = switch_button.SwitchButton()
            elif type == 'text box':
                new_component = text_box.TextButton()
            elif type == 'text box with check':
                new_component = text_box_with_check.TextBoxWithCheck()
            elif type == 'text':
                new_component = ui_text.Text()

        if new_component is not None:
            if type in ('script', ''):
                self.components.append(new_component)
            else:
                self.primary_component = new_component

            return new_component
        else:
            raise Exception(f"component type '{type}' doesn't exist")

    def get_component(self, type_):
        new_type = utilities.check_input(type_, str)
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

    def get_primary_component(self):
        return self.primary_component

    def change_name(self, new_name):
        self.name = str(new_name)

    def render(self):
        if self.primary_component is not None:
            self.primary_component.render()

    def set_state(self, state):
        self.state = utilities.check_input(state, bool)
