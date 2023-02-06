import pygame as pg
import sys
from scene import Scene
from view import View

class GraphicsEngine:
    def __init__(self, WIDTH=1200, HEIGHT=650) -> None:
        pg.init()
        self.FPS = 60
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))

        self.events = pg.event.get()

        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        
        self.scene = Scene(self)
        self.view = View(self)

    def check_events(self):
        self.events = pg.event.get()
        for event in self.events:
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

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
        if not self.view.camera_action:
            self.delta_time = self.clock.tick(self.FPS)
        else:
            self.clock.tick(self.FPS)
            self.delta_time = 0
        
        self.time += self.delta_time

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.view.update()
            self.render()

if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()
