from model import *
from colors import WHITE

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        add(Body(
            app, 
            radius=20, 
            color=WHITE, 
            orbit=CircularOrbit(
                center=(0, 0), 
                start_pos=(0, 80), 
                angular_velocity=5)
                )
            )

    def render(self):
        for obj in self.objects:
            obj.render()
