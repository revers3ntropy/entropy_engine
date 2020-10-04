class UIController:
    def __init__(self):
        self.list_of_ui = []

    def get_element(self, name):
        for i in self.list_of_ui:
            if i.name == str(name):
                return i
        return False

    def init_ui(self):
        for sprite in self.list_of_ui:
            for component in sprite.components:
                component.start()

    def run_ui(self):
        for i in self.list_of_ui:
            if i.state:

                for component in i.components:
                    if component.type == 'script':
                        try:
                            component.script.update()
                        except:
                            pass

                if i.get_primary_component().run():
                    try:
                        i.get_component('script').script.on_click()
                    except:
                        pass


class UIComponent:
    def __init__(self, type_):
        self.type = type_
