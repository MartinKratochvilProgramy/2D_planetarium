import numpy as np
import math
import pyglet
from pyglet import shapes

window = pyglet.window.Window(960, 540)
batch = pyglet.graphics.Batch()

# circle = shapes.Circle(700, 150, 100, color=(50, 225, 30), batch=batch)
# square = shapes.Rectangle(200, 200, 200, 200, color=(55, 55, 255), batch=batch)
# rectangle = shapes.Rectangle(250, 300, 400, 200, color=(255, 22, 20), batch=batch)
# rectangle.opacity = 128
# rectangle.rotation = 33
# line = shapes.Line(100, 100, 100, 200, width=19, batch=batch)
# line2 = shapes.Line(150, 150, 444, 111, width=4, color=(200, 20, 20), batch=batch)
# star = shapes.Star(800, 400, 60, 40, num_spikes=20, color=(255, 255, 0), batch=batch)

N = 2
x = 700
y = 150
radius = 100

d_fi = math.pi / N
for n in range(N):
    start_fi = d_fi * n * 180 / math.pi
    end_fi = d_fi * (n + 1) * 180 / math.pi

    x_start = x + radius * np.cos(start_fi)
    y_start = y + radius * np.sin(start_fi)

    x_end =  x + radius * np.cos(end_fi)
    y_end =  y + radius * np.sin(end_fi)

    print(x_start, y_start)
    print(x_end, y_end)

    line = shapes.Line(x_start, y_start, x_end, y_end, width=1, color=(50, 225, 30), batch=batch)

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()