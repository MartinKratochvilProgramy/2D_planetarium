import math
from model import *
from colors import *

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

        # SUN
        add(Body(
            app, 
            name="Sun",
            radius=696.34, 
            color=SUN, 
            orbit=CircularOrbit(
                app,
                center=(0, 0), 
                start_pos=(0, 0), 
                period=365)
                )
            )

        add(Body(
            app, 
            name="Earth",
            radius=6.374, 
            color=WHITE, 
            orbit=CircularOrbit(
                app,
                center=(0, 0), 
                start_pos=(146_600, 0), 
                period=365)
                )
            )

        add(Body(
            app, 
            name="Mars",
            radius=3.389, 
            color=WHITE, 
            orbit=CircularOrbit(
                app,
                center=(0, 0), 
                start_pos=(224_400, 0), 
                period=687)
                )
            )

        # add(Body(
        #     app, 
        #     radius=20, 
        #     color=WHITE, 
        #     orbit=ElipticalOrbit(
        #         app,
        #         center=(0, 0),
        #         start_fi=0,
        #         epsilon=0.9,
        #         p = 150,
        #         angular_velocity=6000.28,
        #         color=WHITE
        #         )
        #     )
        # )
    
    def render(self):
        for obj in self.objects:
            obj.render()

    
