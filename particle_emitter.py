# ================================================================================================
# |------------------------------------={ Entropy Engine }=--------------------------------------|
# ================================================================================================
#
#                                   Programmers : Joseph Coppin
#
#                                     File Name : particle_emitter.py
#
#                                       Created : October 8, 2020
#
# ------------------------------------------------------------------------------------------------
#
#   Imports:
import random

import sprite_controller
from colour import Colour
import utilities
from script_class import Script
#
# ------------------------------------------------------------------------------------------------
#
#                                       Controls the particle .
#
# ------------------------------------------------------------------------------------------------
#
# ================================================================================================


class ParticleEmitter(sprite_controller.SpriteComponent):
    def __init__(self, sprite):
        super().__init__('particle emitter')
        self.sprite = sprite

        self.rate = 1
        self.size = 3
        self.life_time = 10
        self.speed = 1
        self.angle_range = (0, 360)

        self.go = True
        self.colour = Colour((0, 0, 0))

        self.particles = []

        self.count = 0

    def __emit_particle(self):
        sprite = Script.create_sprite(f'particle {self.count} from {self.sprite.name}')

        body = sprite.add_component('body')
        body.go_to(self.sprite.get_component('body').position)
        body.set_speed(self.speed)
        body.set_direction(random.randint(self.angle_range[0], self.angle_range[1]))

        renderer = sprite.add_component('rect renderer')
        renderer.set_colour(self.colour)
        renderer.set_size([self.size, self.size])

        sprite.add_component('script').set_script(ParticleController(self.sprite, self.life_time))

        self.particles.append(sprite)

        self.count += 1

    def start(self):
        pass

    def go(self):
        self.go = True

    def stop(self):
        self.go = False

    def update(self):
        if self.go:
            self.__emit_particle()

        for particle in self.particles:
            particle.get_component('script')[0].script.update()

    def set_colour(self, colour):
        self.colour = utilities.check_input(colour, Colour)

    def set_size(self, size):
        self.size = utilities.check_input(size, float)

    def set_rate(self, rate):
        self.rate = utilities.check_input(rate, float)

    def set_life_time(self, life_time):
        self.life_time = utilities.check_input(life_time, float)

    def set_speed(self, speed):
        self.speed = utilities.check_input(speed, float)


class ParticleController(Script):
    def __init__(self, sprite, life_time):
        super().__init__()
        self.sprite = sprite

        self.timer = life_time

    def update(self):
        if self.timer < 1:
            try:
                self.sprite.remove_component('rect renderer')
            except Exception:
                pass

        self.timer -= 1
