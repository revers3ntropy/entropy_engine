import ui_controller


class ScriptComponent(ui_controller.UIComponent):
    def __init__(self):
        super().__init__('script')
        self.script = None

    def start(self):
        pass

    def set_script(self, script_class):
        if type(script_class) in (float, int, str, bool, list, dict, tuple):
            raise Exception(f'Script must be a class object, not type {type(script_class)}.', 'script.Script.set_script(script_class)')

        if script_class.__class__.__bases__[0].__name__ != 'Script':
            raise Exception(f'Script must inherit from type Script', 'script.Script.set_script(script_class)')

        self.script = script_class
        try:
            self.script.start()
        except:
            pass
        return self

    def tick_script(self):
        try:
            self.script.update()
        except:
            pass
