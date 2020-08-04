import ui_controller


class Script(ui_controller.UIComponent):
    def __init__(self):
        super().__init__('script')
        self.script = None

    def start(self):
        pass

    def set_script(self, script_class):
        self.script = script_class
        try:
            self.script.start()
        except:
            pass
        return self

    def get_script(self):
        return self.script

    def tick_script(self):
        try:
            self.script.update()
        except:
            pass
