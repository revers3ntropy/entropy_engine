list_of_ui = []


def get_element(name):
    for i in list_of_ui:
        if i.name == str(name):
            return i
    return False


def init_ui():
    for sprite in list_of_ui:
        for component in sprite.components:
            component.start()


def run_ui():
    for i in list_of_ui:
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
    def __init__(self, type):
        self.type = type
