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
                app,
                center=(0, 0), 
                start_pos=(-150, 0), 
                angular_velocity=0)
                )
            )

        add(Body(
            app, 
            radius=20, 
            color=WHITE, 
            orbit=ElipticalOrbit(
                app,
                center=(0, 0),
                start_fi=0,
                start_radius=150,
                epsilon=0.5,
                p = 150,
                angular_velocity=1
                )
            )
        )

    def render(self):
        for obj in self.objects:
            obj.render()
