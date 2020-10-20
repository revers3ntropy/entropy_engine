from body import Body
from image import Image
from script import ScriptComponent
from collider import Collider
from composite_collider import CompositeCollider
from tag import Tag
from animation import Animation
from rect_renderer import RectRenderer
from particle_emitter import ParticleEmitter

import utilities


class Sprite:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.components = []

        self.tag = ''

    def add_component(self, type_):
        def fail():
            raise Exception(
                f'Cannot add component {type_}, as another component is interfering with it.',
                'sprite.Sprite.add_component(type_)')

        new_component = None
        if type_ == 'body':
            if self.get_component('body') is False:
                new_component = Body(self)
            else:
                fail()

        elif type_ == 'image':
            if self.get_component('image') is False and self.get_component(
                    'rect renderer') is False and \
                    self.get_component('circle renderer') is False:
                new_component = Image()
            else:
                fail()

        elif type_ == 'rect renderer':
            if self.get_component('image') is False and self.get_component(
                    'rect renderer') is False and \
                    self.get_component('circle renderer') is False:
                new_component = RectRenderer(self)
            else:
                fail()

        elif type_ == 'script':
            new_component = ScriptComponent()

        elif type_ == 'collider':
            if not self.get_component('collider') and not self.get_component('composite collider'):
                new_component = Collider(self)

        elif type_ == 'composite collider':
            if not self.get_component('collider') and not self.get_component('composite collider'):
                new_component = CompositeCollider(self)

        elif type_ == 'animation':
            if not self.get_component('animation'):
                new_component = Animation(self)

        elif type_ == 'particle emitter':
            if not self.get_component('particle emitter'):
                new_component = ParticleEmitter(self)

        if new_component is not None:
            self.components.append(new_component)
            return new_component
        else:
            raise Exception(f"component {type_} does not exist")

    def get_component(self, type_):
        type_ = str(type_)

        if type_ == 'script':
            scripts = []
            for component in self.components:
                if component != None:
                    if component.type == type_:
                        scripts.append(component)
            return scripts
        else:

            for component in self.components:
                if component != None:
                    if component.type == type_:
                        return component
            return False

    def change_name(self, name):
        self.name = str(name)

    def remove_component(self, type):
        component = self.get_component(str(type))
        if component is False:
            raise Exception(
                f'Component {str(type)} could not be found to remove. Make sure you have initialised it, and spelt it correctly.')
        else:
            for i in range(len(self.components)):
                if self.components[i].type == str(type):
                    self.components[i] = None

    def set_tag(self, tag_):
        self.tag = utilities.check_input(tag_, Tag)
