import pygame as pg
import sys
from scene import Scene
from view import View

class GraphicsEngine:
    def __init__(self, WIDTH=1200, HEIGHT=650) -> None:
        pg.init()
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))

        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        
        self.scene = Scene(self)
        self.view = View(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.scene_renderer.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        # clear framebuffer
        self.screen.fill((20, 41, 46))
        self.scene.render()
        # swap buffers
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() *0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.view.update()
            self.render()
            self.delta_time = self.clock.tick(60)

if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()
