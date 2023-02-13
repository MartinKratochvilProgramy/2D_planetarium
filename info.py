import pygame as pg
from colors import WHITE, BLACK

class Info:
    def __init__(self, app) -> None:
        self.app = app
        self.stats = []

    def display(self):
        font = pg.font.Font('freesansbold.ttf', 22)

        time_scale = font.render(f'Time scale: {self.app.clock.time_scale}x', True, WHITE, BLACK)
        time_scale_rect = time_scale.get_rect()
        left = 0 + time_scale.get_width() / 2
        top = 0 + time_scale.get_height() / 2
        time_scale_rect.center = (left, top)
        self.app.screen.blit(time_scale, time_scale_rect)

        elapsed_time = font.render(f'Elapsed time: {round(self.app.clock.time)} days', True, WHITE, BLACK)
        elapsed_time_rect = elapsed_time.get_rect()
        left = 0 + elapsed_time.get_width() / 2
        top = time_scale.get_height() + elapsed_time.get_height() / 2
        elapsed_time_rect.center = (left, top)
        self.app.screen.blit(elapsed_time, elapsed_time_rect)

        zoom = font.render(f'Zoom: {round(self.app.camera.zoom, 1)}', True, WHITE, BLACK)
        zoom_rect = zoom.get_rect()
        left = 0 + zoom.get_width() / 2
        top = zoom.get_height() + elapsed_time.get_height() + zoom.get_height() / 2
        zoom_rect.center = (left, top)
        self.app.screen.blit(zoom, zoom_rect)

        fps = font.render(f'FPS: {round(1 / self.app.clock.dt_engine * self.app.clock.time_scale)}', True, WHITE, BLACK)
        fps_rect = fps.get_rect()
        left = 0 + fps.get_width() / 2
        top = fps.get_height() + elapsed_time.get_height() + zoom.get_height() + fps.get_height() / 2
        fps_rect.center = (left, top)
        self.app.screen.blit(fps, fps_rect)