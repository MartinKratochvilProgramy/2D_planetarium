import pygame as pg

PAN_SPEED = 0.1

class View:
    def __init__(self, app):
        self.app = app
        self.x_offset = self.app.WIDTH / 2
        self.y_offset = self.app.HEIGHT / 2

    def update(self):
        self.move()

    def move(self):
        velocity = PAN_SPEED * self.app.delta_time
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.y_offset += velocity
        if keys[pg.K_s]:
            self.y_offset -= velocity
        if keys[pg.K_a]:
            self.x_offset += velocity
        if keys[pg.K_d]:
            self.x_offset -= velocity
