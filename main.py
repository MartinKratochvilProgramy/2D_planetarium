import pygame as pg
import sys
from clock import Clock
from scene import Scene
from camera import Camera
from info import Info
from colors import WHITE, BLACK

class GraphicsEngine:
    def __init__(self, WIDTH=1200, HEIGHT=650) -> None:
        pg.init()
        self.FPS = 60
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        
        self.font = pg.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render('GeeksForGeeks', True, WHITE, BLACK)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.WIDTH // 2, self.HEIGHT // 2)

        self.events = pg.event.get()

        self.clock = Clock(time_scale=1, t0 = 0)
        self.scene = Scene(self)
        self.camera = Camera(self)
        self.info = Info(self)

    def check_events(self):
        self.events = pg.event.get()
        for event in self.events:
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    self.clock.increase_time_scale() 
                if event.key == pg.K_a:
                    self.clock.decrease_time_scale() 

    def get_time(self):
        # update time only when camera is not camera_action
        delta_t = pg.time.Clock().tick(self.FPS) * self.clock.time_scale         # to seconds
        if not self.camera.camera_action:
            self.clock.dt = delta_t
            self.clock.update_time()
        else:
            # don't update on camera action
            self.clock.dt = 0

    def render(self):
        self.screen.fill((20, 41, 46))
        self.scene.render()
        image = pg.Surface([640,480], pg.SRCALPHA, 32)
        image.fill((255, 255, 255))
        image = image.convert_alpha()

        self.info.display()

        pg.display.flip()

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()

if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()
