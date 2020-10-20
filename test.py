import entropy_engine as ee
from entropy_engine import scene_manager
ee.init((500, 500))

sprite = ee.create_sprite('particle tester')
sprite.add_component('body')
particle_emitter = sprite.add_component('particle emitter')


class CameraController(ee.Script):
    def __init__(self, body, player_body):
        super().__init__()
        self.player_body = player_body
        self.body = body

    def update(self):
        self.body.go_to(self.player_body.position)


camera_controller = scene_manager.current_scene().find_sprite('camera').add_component('script')
camera_controller.set_script(CameraController(scene_manager.current_scene().find_sprite('camera').get_component('body'),
                                              scene_manager.current_scene().find_sprite('particle tester').get_component('body')))

ee.run_game()
