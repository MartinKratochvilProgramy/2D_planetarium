import pyglet
from pyglet.window import key
from scene import Scene
from camera import Camera
from clock import Clock
# from rectangle import Rectangle

# https://github.dev/earthastronaut/pyglet_projects/tree/master/projects/asteroids

class GraphicsEngine(pyglet.window.Window):
    def __init__(self, WIDTH=1200, HEIGHT=650, *args, **kwargs) -> None:

        self.FPS = 60
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        
        self.window = pyglet.window.Window(WIDTH, HEIGHT, caption="A python is a snake")
        self.window.push_handlers(
            on_key_press=self.on_key_press,
            on_draw=self.on_draw,
        )

        self.batch = pyglet.graphics.Batch()

        self.clock = Clock()
       
        self.scene = Scene(self)
        self.camera = Camera(self)

        pyglet.clock.schedule_interval(self.update, 1.0 / self.FPS)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            pyglet.app.exit()

    # def get_time(self):
    #     # update time only when camera is not camera_action
    #     if not self.view.camera_action:
    #         self.delta_time = self.clock.tick(self.FPS)
    #     else:
    #         self.clock.tick(self.FPS)
    #         self.delta_time = 0
        
    #     self.time += self.delta_time

    def update(self, dt):
        self.clock.tick()
        # if not self.view.camera_action:
        #     self.clock.update()

    def on_draw(self):
        self.clear()
        self.batch.draw()


if __name__ == '__main__':
    app = GraphicsEngine()
    pyglet.app.run()
