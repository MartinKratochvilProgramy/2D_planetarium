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

        add(Body(app, pos=(app.WIDTH/2, app.HEIGHT/2), radius=20, color=WHITE))

    def render(self):
        for obj in self.objects:
            obj.render()
