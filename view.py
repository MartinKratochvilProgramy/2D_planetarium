import pygame as pg

PAN_SPEED = 0.1
ZOOM_SPEED = 0.1

class View:
    def __init__(self, app):
        self.app = app
        
        self.zoom = 1.
        self.x_offset = self.app.WIDTH / 2 * self.zoom
        self.y_offset = self.app.HEIGHT / 2 * self.zoom

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
            self.x_offset = (self.x_offset + mouse_dx / self.zoom)
            self.y_offset = (self.y_offset + mouse_dy / self.zoom)
            

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

                self.x_offset += x_post - x_prev
                self.y_offset += y_post - y_prev

                print(self.zoom)


    def world_to_screen_transform(self, x, y):
        transformed_x = (self.x_offset - x) * self.zoom
        transformed_y = (self.y_offset - y) * self.zoom
        return transformed_x, transformed_y
    
    def screen_to_world_transform(self, x, y):
        transformed_x_offset = x / self.zoom + self.x_offset
        transformed_y_offset = y / self.zoom + self.x_offset
        return transformed_x_offset, transformed_y_offset
