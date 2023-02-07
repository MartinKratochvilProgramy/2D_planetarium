from model import *
from colors import WHITE, GRAY

class Scene:
    def __init__(self, app):
        self.app = app
        self.clock = app.clock
        self.batch = app.batch
        self.window = app.window
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        add(Body(
            app, 
            radius=5, 
            color=WHITE, 
            orbit=CircularOrbit(
                app,
                center=(400, 400), 
                start_pos=(500, 400), 
                angular_velocity=1,
                color=GRAY)
                )
            )

        add(Body(
            app, 
            radius=5, 
            color=WHITE, 
            orbit=CircularOrbit(
                app,
                center=(400, 400), 
                start_pos=(450, 400), 
                angular_velocity=1,
                color=GRAY)
                )
            )
