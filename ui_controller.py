list_of_ui = []


def get_element(name):
    for i in list_of_ui:
        if i.get_name() == name:
            return i
    return False


def run_ui():
    for i in list_of_ui:
        try:
            i.get_component('script').get_script().update()
        except:
            pass
        if i.get_primary_component().run():
            try:
                i.get_component('script').get_script().on_click()
            except:
                pass


class UIComponent:
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type
