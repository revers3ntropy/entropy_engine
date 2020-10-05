# initialising entropy engine
import entropy_engine as ee
ee.init((1000, 800))

ee.scene_manager.new_scene('main game')
ee.scene_manager.set_active_scene('main game')


class PlayerController(ee.Script):
    def __init__(self, sprite):
        super().__init__()
        self.sprite = sprite

    # this gets called when the program is run
    def start(self):
        pass

    # this gets called every frame
    def update(self):
        pass


player = ee.create_sprite('player')
player.add_component('script').set_script(PlayerController([player]))
