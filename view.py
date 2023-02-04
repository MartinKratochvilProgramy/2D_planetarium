import pygame as pg

PAN_SPEED = 0.1
ZOOM_SPEED = 0.1

class View:
    def __init__(self, app):
        self.app = app
        
        self.x_offset = self.app.WIDTH / 2
        self.y_offset = self.app.HEIGHT / 2
        self.zoom = 1.

        self.mouse_x, self.mouse_y = pg.mouse.get_pos()
        self.camera_action = False

    def update(self):
        self.camera_action = False
        self.handle_pan()
        self.handle_zoom()

    def handle_pan(self):
        new_mouse_x, new_mouse_y = pg.mouse.get_pos()
        mouse_dx = new_mouse_x - self.mouse_x
        mouse_dy = new_mouse_y - self.mouse_y
        self.mouse_x, self.mouse_y = new_mouse_x, new_mouse_y

        LMB, MMB, RMB = pg.mouse.get_pressed()
        if (MMB):
            self.camera_action = True
            self.x_offset += mouse_dx
            self.y_offset += mouse_dy
            

    def handle_zoom(self):
        for event in self.app.events:
            if event.type == pg.MOUSEWHEEL:
                self.camera_action = True
                self.zoom += event.y * ZOOM_SPEED
