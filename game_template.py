# initialising entropy engine
import entropy_engine as ee
ee.init((1000, 800))


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


ee.run_game()
