import pygame as pg

PAN_SPEED = 0.1

class View:
    def __init__(self, app):
        self.app = app
        self.x_offset = self.app.WIDTH / 2
        self.y_offset = self.app.HEIGHT / 2
        self.mouse_x, self.mouse_y = pg.mouse.get_pos()

    def update(self):
        self.move()

    def move(self):
        # keys = pg.key.get_pressed()

        new_mouse_x, new_mouse_y = pg.mouse.get_pos()
        mouse_dx = new_mouse_x - self.mouse_x
        mouse_dy = new_mouse_y - self.mouse_y
        self.mouse_x, self.mouse_y = new_mouse_x, new_mouse_y

        LMB, MMB, RMB = pg.mouse.get_pressed()
        if (MMB):
            self.x_offset += mouse_dx
            self.y_offset += mouse_dy
