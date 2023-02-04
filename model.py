import pygame as pg

class Body:
    def __init__(self, app, pos, radius, color, orbit):
        self.app = app
        self.radius = radius
        self.pos = pos
        self.color = color
        self.orbit = orbit

    def update(self):
        pass

    def render(self):
        self.update()
        pg.draw.circle(self.app.screen, self.color, self.pos, self.radius)

class CircularOrbit:
    def __init__(self, center, radius, start_pos, angular_velocity):
        self.center = center
        self.radius = radius
        self.start_pos = start_pos
        self.angular_velocity = angular_velocity