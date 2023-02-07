import time

class Clock:
    def __init__(self) -> None:
        self.time = time.time()
        self.elapsed_time = 0

    def tick(self):
        # this should run every game tick
        self.time = time.time()

    def update_time(self):
        # this should run only when update is needed (no panning or zooming)
        current_time = time.time()
        
        dt = current_time - self.time
        
        self.elapsed_time += dt
        # print(self.elapsed_time)
        self.time = current_time