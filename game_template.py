# initialising entropy engine
import entropy_engine as ee
ee.init((1000, 800))
ee.set_window_title('Example Game')
ee.set_target_fps(60)


class PlayerController(ee.Script):
    def __init__(self):
        super().__init__()

    # this gets called when the program is run
    def start(self):
        pass

    # this gets called every frame
    def update(self):
        pass


player = ee.create_sprite('player')
player.add_component('script').set_script(PlayerController())
