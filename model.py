import pygame as pg
import numpy as np
from utils.safe_atan import safe_atan
from colors import WHITE

class Body:
    def __init__(self, app, radius, color, orbit):
        self.app = app
        self.radius = radius
        self.color = color
        self.orbit = orbit

    def update(self):
        self.orbit.update(self.app.delta_time)

    def render(self):
        self.update()
        self.orbit.render()
        pg.draw.circle(
            self.app.screen, 
            self.color, 
            center = (self.app.view.world_to_screen_transform(self.orbit.x, self.orbit.y)),
            radius = max(self.radius / self.app.view.zoom, 1)   # planet size could be less than 0
        )


class ElipticalOrbit():
    def __init__(self, app, center, start_fi, start_radius, epsilon, p, angular_velocity):
        self.app = app
        self.fi = start_fi
        self.radius = p / (1 + epsilon)
        self.epsilon = epsilon
        self.p = p
        self.angular_velocity = angular_velocity
        self.center = center
        
    def update(self, dt):
        self.fi += self.angular_velocity * dt / 1000 % 360       # from ms to s, floor to 360
        self.radius = self.p / (1 + self.epsilon * np.cos(self.fi))
        self.x = self.center[0] + self.radius * np.cos(self.fi)
        self.y = self.center[1] - self.radius * np.sin(self.fi)

    def render(self):
        r_max = self.p / (1 - self.epsilon)
        r_min = self.p / (1 + self.epsilon)
        b = np.sqrt(r_min * r_max)

        left = self.center[0] - r_max
        top = self.center[1] - b
        left, top = self.app.view.world_to_screen_transform(left, top)

        width = r_min + r_max
        height = 2*b

        pg.draw.ellipse(
            self.app.screen, 
            color=WHITE, 
            rect=(left, top, width, height),
            width=1
        )


class CircularOrbit():
    def __init__(self, app, center, start_pos, angular_velocity):
        self.app = app
        dx = start_pos[0] - center[0]
        dy = start_pos[1] - center[1]
        self.radius = np.sqrt(dx**2 + dy**2)
        self.angular_velocity = angular_velocity
        self.center = center
        
        self.x = start_pos[0]
        self.y = start_pos[1]
        self.fi = safe_atan(dy, dx)

    def update(self, dt):
        self.fi += self.angular_velocity * dt / 1000 % 360       # from ms to s, floor to 360
        self.x = self.center[0] + self.radius * np.cos(self.fi)
        self.y = self.center[1] - self.radius * np.sin(self.fi)

    def render(self):
        pg.draw.circle(
            self.app.screen, 
            color=WHITE, 
            center = self.app.view.world_to_screen_transform(self.center[0], self.center[1]),
            radius = max(self.radius / self.app.view.zoom, 1),
            width=1
        )