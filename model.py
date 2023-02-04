import pygame as pg
from utils.safe_atan import safe_atan
import numpy as np

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
        pg.draw.circle(self.app.screen, self.color, center=(self.orbit.x + self.app.view.x_offset, self.orbit.y + self.app.view.y_offset), radius=self.radius)


class CircularOrbit:
    def __init__(self, center, start_pos, angular_velocity):
        dx = start_pos[0] - center[0]
        dy = start_pos[1] - center[1]
        self.radius = np.sqrt(dx**2 + dy**2)
        self.angular_velocity = angular_velocity
        self.center = center
        
        self.x = start_pos[0]
        self.y = start_pos[1]
        self.fi = safe_atan(dy, dx)

    def update(self, dt):
        self.fi += self.angular_velocity * dt / 1000        # from ms to s
        self.x = self.center[0] + self.radius * np.cos(self.fi)
        self.y = self.center[1] - self.radius * np.sin(self.fi)
