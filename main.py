import pygame as pg
import sys
from scene import Scene
from camera import Camera
from clock import Clock

class GraphicsEngine:
    def __init__(self, WIDTH=1200, HEIGHT=650) -> None:
        pg.init()
        self.FPS = 60
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))

        self.events = pg.event.get()

        self.clock = Clock(t0 = 0)
        self.scene = Scene(self, time_scale=1)
        self.camera = Camera(self)

    def check_events(self):
        self.events = pg.event.get()
        for event in self.events:
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    self.scene.increase_time_scale() 
                if event.key == pg.K_d:
                    self.scene.decrease_time_scale() 

    def render(self):
        # clear framebuffer
        self.screen.fill((20, 41, 46))
        self.scene.render()
        image = pg.Surface([640,480], pg.SRCALPHA, 32)
        image.fill((255, 255, 255))
        image = image.convert_alpha()
        # swap buffers
        pg.display.flip()

    def get_time(self):
        # update time only when camera is not camera_action
        delta_t = pg.time.Clock().tick(self.FPS) * self.scene.time_scale         # to seconds
        if not self.camera.camera_action:
            self.clock.dt = delta_t
            self.clock.update_time()
        else:
            # don't update on camera action
            self.clock.dt = 0

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()

if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()
