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
                center=(app.WIDTH/2, app.HEIGHT/2), 
                start_pos=(app.WIDTH/2 + 80, app.HEIGHT/2), 
                angular_velocity=1)
                )
            )

    def render(self):
        for obj in self.objects:
            obj.render()
