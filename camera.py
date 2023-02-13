import pygame as pg
from settings import ZOOM_SPEED
from colors import WHITE, BLACK

class Camera:
    def __init__(self, app):
        self.app = app
        
        self.zoom = 800
        self.x_offset = -self.app.WIDTH / 2 * self.zoom - 680
        self.y_offset = -self.app.HEIGHT / 2 * self.zoom

        self.x_start_pan = 0
        self.y_start_pan = 0

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

            self.x_offset -= mouse_dx * self.zoom
            self.y_offset -= mouse_dy * self.zoom

            self.x_start_pan = new_mouse_x
            self.y_start_pan = new_mouse_y

    def handle_zoom(self):
        for event in self.app.events:
            if event.type == pg.MOUSEWHEEL:
                self.camera_action = True
                x_prev, y_prev = self.screen_to_world_transform(self.mouse_x, self.mouse_y)
                if (event.y > 0):
                    self.zoom *= 1 + ZOOM_SPEED
                if (event.y < 0):
                    self.zoom *= 1 - ZOOM_SPEED

                x_post, y_post = self.screen_to_world_transform(self.mouse_x, self.mouse_y)

                self.x_offset += (x_post - x_prev) * (self.zoom / 400)
                self.y_offset += (y_post - y_prev) * (self.zoom / 400)

    def world_to_screen_transform(self, x_world, y_world):
        x_screen = (x_world - self.x_offset) / self.zoom
        y_screen = (y_world - self.y_offset) / self.zoom
        return x_screen, y_screen
    
    def screen_to_world_transform(self, x_screen, y_screen):
        x_world = x_screen / self.zoom + self.x_offset
        y_world = y_screen / self.zoom + self.y_offset
        return x_world, y_world
