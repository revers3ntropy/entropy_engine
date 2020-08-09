import ui_controller
import fail_system


class Script(ui_controller.UIComponent):
    def __init__(self):
        super().__init__('script')
        self.script = None

    def start(self):
        pass

    def set_script(self, script_class):
        if type(script_class) in (float, int, str, bool, list, dict, tuple):
            fail_system.error(f'Script must be a class object, not type {type(script_class)}.', 'script.Script.set_script(script_class)')

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
