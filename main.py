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

    def update(self, dt):
        if not self.camera.camera_action:
            self.clock.update_time()
            print(self.clock.dt)
            for obj in self.scene.objects:
                obj.update()
            # print(self.clock.elapsed_time)
        else:
            self.clock.tick()

    def on_draw(self):
        self.clear()
        self.batch.draw()


if __name__ == '__main__':
    app = GraphicsEngine()
    pyglet.app.run()
