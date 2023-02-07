import pyglet
from pyglet import shapes
from pyglet.window import key

PAN_SPEED = 0.1
ZOOM_SPEED = 0.05

class Camera():
    def __init__(self, app, *args, **kwargs) -> None:
        self.app = app
        self.app.window.push_handlers(
            on_mouse_drag = self.on_mouse_drag,
            on_mouse_scroll = self.on_mouse_scroll,
        )
        
        self.zoom = 1.
        self.x_offset = -self.app.WIDTH / 2 * self.zoom
        self.y_offset = -self.app.HEIGHT / 2 * self.zoom

        self.x_start_pan = 0
        self.y_start_pan = 0

        # self.mouse_x, self.mouse_y = (0, 0) #pg.mouse.get_pos()
        self.camera_action = False
        print(6969)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if (buttons == 2):  
            self.handle_pan(dx, dx)
        pass

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.handle_zoom(x, y, scroll_y)

    # def update(self):
    #     self.camera_action = False
    #     self.handle_pan()
    #     self.handle_zoom()

    def handle_pan(self, dx, dy):
        self.camera_action = True

        self.x_offset -= dx * self.zoom
        self.y_offset -= dy * self.zoom

        print(self.x_offset, self.y_offset)

    def handle_zoom(self, mouse_x, mouse_y, scroll):
                x_prev, y_prev = self.screen_to_world_transform(mouse_x, mouse_y)
                if (scroll > 0):
                    self.zoom *= 1 + ZOOM_SPEED
                if (scroll < 0):
                    self.zoom *= 1 - ZOOM_SPEED

                x_post, y_post = self.screen_to_world_transform(mouse_x, mouse_y)

                self.x_offset += (x_post - x_prev)
                self.y_offset += (y_post - y_prev)

    def world_to_screen_transform(self, x_world, y_world):
        x_screen = (x_world - self.x_offset) / self.zoom
        y_screen = (y_world - self.y_offset) / self.zoom
        return x_screen, y_screen
    
    def screen_to_world_transform(self, x_screen, y_screen):
        x_world = x_screen / self.zoom + self.x_offset
        y_world = y_screen / self.zoom + self.y_offset
        return x_world, y_world
