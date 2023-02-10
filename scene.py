from model import *
from colors import WHITE
from settings import TIME_SCALE_SPEED

class Scene:
    def __init__(self, app, time_scale=1):
        self.app = app
        self.time_scale = time_scale
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
                epsilon=0.9,
                p = 150,
                angular_velocity=100,
                color=WHITE
                )
            )
        )

    def increase_time_scale(self):
        self.time_scale *= 1 + TIME_SCALE_SPEED
    
    def decrease_time_scale(self):
        self.time_scale *= 1 - TIME_SCALE_SPEED
    
    def render(self):
        for obj in self.objects:
            obj.render()

    
