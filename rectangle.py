import pyglet
from pyglet import shapes
from pyglet.window import key
import time

class Rectangle():
    def __init__(self, app, *args, **kwargs) -> None:
        self.app = app
        print(self.app.window)
        self.app.window.push_handlers(
            on_mouse_press = self.on_mouse_press,
            on_key_press = self.on_key_press
        )
        # super(Rectangle, self).__init__(app.WIDTH, app.HEIGHT, *args, **kwargs)
        self.blue_square = shapes.Rectangle(200, 200, 100, 20, color=(100, 100, 100), batch=self.app.batch)

    def on_key_press(self, symbol, modifiers):
        print("key")

    def on_mouse_press(self, x, y, button, modifiers):
        print("mouse!!!!!!!!!")
