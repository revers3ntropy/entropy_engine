import entropy_engine as ee
from entropy_engine import scene_manager
# initialising entropy engine
ee.init((1000, 800))
ee.set_window_title('Example Game')
ee.set_target_fps(60)


# the script to control the player (this might be in another file in your game, but I have everything in one file for simplicity)
class PlayerController(ee.Script):
    def __init__(self, body, collider):
        super().__init__()
        self.__body = body
        self.__collider = collider
        self.__colliding_with = None
        # private variable __deaths
        self.__deaths = 0
        # some player initialisation
        self.__body.set_gravity(5)
        self.__collider.set_bounce(0.1)
        self.__collider.set_size([10, 20])
        self.__body.set_friction(1.15)

    # this is a private function, so you can't access it outside the script. it is only used once, when the player
    # reached below a certain y value, and that is all done inside the player script.
    def __die(self):
        # sends the player back to the start
        self.__body.go_to([0, 0])
        self.__deaths += 1
        # so the player doesn't keep the velocity from when they were falling (smoother transition when deactivated)
        # self.body.set_velocity((0, 6))

    # automatically called every tick
    def update(self):
        # player movement
        if ee.keypress(ee.py.K_LEFT) or ee.keypress(ee.py.K_a):
            self.__body.move([-2, 0])

        if ee.keypress(ee.py.K_RIGHT) or ee.keypress(ee.py.K_d):
            self.__body.move([2, 0])

        if ee.keypress(ee.py.K_UP) or ee.keypress(ee.py.K_SPACE):
            # so you can only jump when touching the ground
            if self.__colliding_with is not None:
                self.__body.jump(20)

        self.__colliding_with = None

        # if the player has fallen out the world, then die
        if self.__body.get_position()[1] > 1000:
            self.__die()

    # automatically called when a collision is detected
    def on_collision(self, collision_object):
        self.__colliding_with = collision_object

    # used by the death counter to get the number of times the player has died
    def get_deaths(self):
        return self.__deaths


# script to control the camera
class CameraController(ee.Script):
    def __init__(self, body, player_body):
        super().__init__()
        # this is how you get the position of other sprites, pass in their body adn then call body.get_position()
        self.player_body = player_body
        # this is the camera's body
        self.body = body

    def update(self):
        # makes the camera follow the player
        self.body.go_to(self.player_body.position)


class Obstacle(ee.Prefab):
    def __init__(self, number, x, y):
        super().__init__()
        self.sprite = ee.create_sprite('obstacle ' + str(number))
        self.collider = self.sprite.add_component('collider')
        self.collider.set_size((100, 30))
        self.body = self.sprite.add_component('body')
        self.body.go_to((x, y))
        self.image = self.sprite.add_component('image')
        self.image.set_image_from_file('graphics/obstacle.png')
        self.body.set_gravity(0)
        self.body.set_friction(100)


# this is a list of the locations for our obstacle
obstacle_locations = [
    (200, 300),
    (300, 400),
    (600, 400),
    (0, 300),
    (400, 500)
]

# this is a list of our Obstacle sprites, which can be used later if we want
list_of_obstacles = []
# loops through our list of obstacle locations, and makes a new sprite for each one
for i in range(len(obstacle_locations)):
    # makes new sprite, using the location in the list of locations and our Obstacle class
    list_of_obstacles.append(Obstacle(i, obstacle_locations[i][0], obstacle_locations[i][1]))

# creates a player
player = ee.create_sprite('player')
# gives the player a body and a collider
player_collider = player.add_component('collider')
player_body = player.add_component('body')
# this is how the player will look on the screen - a rectangle
player_renderer = player.add_component('rect renderer')
player_renderer.set_colour(ee.new_colour((0, 0, 0)))
# this adds the PlayerController script to the player
player.add_component('script').set_script(PlayerController(player_body, player_collider))


# this script controls the UI element death_counter, initialised below
class DeathCounterController(ee.Script):
    def __init__(self, player_controller, text):
        super().__init__()
        # this is the script PlayerController, which has the function get_deaths()
        self.player_controller = player_controller
        # this in the text ui component
        self.text = text

    def update(self):
        # sets the text to the number of deaths the player has had
        self.text.set_text(f'deaths: {self.player_controller.get_deaths()}')


# this initialises the death counter ui element
death_counter = ee.create_ui_element('deaths')
death_counter_text = death_counter.add_component('text')
# quickly adds the DeathCounterController script to the death counter element
death_counter.add_component('script').set_script(DeathCounterController(player.get_component('script')[0].script, death_counter_text))
# puts it in the corner on the screen
death_counter_text.set_position((ee.get_screen_size()[0] - 200, 50))

# adds the camera script to the camera game object, which has already been initialised
camera_controller = scene_manager.current_scene().find_sprite('camera').add_component('script')
camera_controller.set_script(CameraController(scene_manager.current_scene().find_sprite('camera').get_component('body'),
                                              scene_manager.current_scene().find_sprite('player').get_component('body')))

# runs the game
ee.run_game()
