import pygame as pg
import numpy as np
from utils.safe_atan import safe_atan
from colors import WHITE
from settings import GRAV_CONST

class Body:
    def __init__(self, app, radius, color, orbit):
        self.app = app
        self.radius = radius
        self.color = color
        self.orbit = orbit

    def update(self):
        self.orbit.update()

    def render(self):
        self.update()
        self.orbit.render()
        pg.draw.circle(
            self.app.screen, 
            self.color, 
            center = (self.app.camera.world_to_screen_transform(self.orbit.x, self.orbit.y)),
            radius = max(self.radius / self.app.camera.zoom, 1)   # planet size could be less than 0
        )


class CircularOrbit():
    def __init__(self, app, center, start_pos, period):
        self.app = app
        dx = start_pos[0] - center[0]
        dy = start_pos[1] - center[1]
        self.radius = np.sqrt(dx**2 + dy**2)
        self.angular_velocity = 2*np.pi / period
        self.center = center
        
        self.x = start_pos[0]
        self.y = start_pos[1]
        self.fi = safe_atan(dy, dx)

    def update(self):
        self.fi += self.angular_velocity * self.app.clock.dt      # from ms to s, floor to 360
        self.fi = self.fi % 360
        self.x = self.center[0] + self.radius * np.cos(self.fi)
        self.y = self.center[1] - self.radius * np.sin(self.fi)

    def render(self):
        pg.draw.circle(
            self.app.screen, 
            color=WHITE, 
            center = self.app.camera.world_to_screen_transform(self.center[0], self.center[1]),
            radius = self.radius / self.app.camera.zoom,
            width=1
        )


class ElipticalOrbit():
    def __init__(self, app, center, start_fi, epsilon, p, angular_velocity, color):
        self.app = app
        self.center = center
        self.fi = start_fi
        self.epsilon = epsilon
        self.epsilon = epsilon
        self.p = p
        self.radius = p / (1 + epsilon)
        self.angular_velocity = angular_velocity
        self.color = color

        self.r_max = self.p / (1 - self.epsilon)
        self.r_min = self.p / (1 + self.epsilon)
        self.b = np.sqrt(self.r_min * self.r_max)
        self.a = self.b**2 / self.p

        self.left = self.center[0] - self.r_max
        self.top = self.center[1] - self.b
        
    def update(self):
        v = (2 * self.angular_velocity) / (self.radius * np.sin(np.pi/2 + self.fi))
        dfi = np.arcsin(v * self.app.clock.dt / self.radius)
        self.fi += dfi        # from ms to s, floor to 360
        self.fi %= 360
        self.radius = self.p / (1 + self.epsilon * np.cos(self.fi))
        self.x = self.center[0] + self.radius * np.cos(self.fi)
        self.y = self.center[1] - self.radius * np.sin(self.fi)

    def render(self):
        left = self.center[0] - self.r_max
        top = self.center[1] - self.b
        left, top = self.app.camera.world_to_screen_transform(self.left, self.top)

        width = (self.r_min + self.r_max) / self.app.camera.zoom
        height = 2*self.b / self.app.camera.zoom

        pg.draw.ellipse(
            self.app.screen, 
            color=self.color, 
            rect=(left, top, width, height),
            width=1
        )

        pg.draw.circle(
            self.app.screen,
            color=self.color,
            center = self.app.camera.world_to_screen_transform(self.center[0], self.center[1]),
            radius = 1,
        )
