class Clock:
    def __init__(self, t0 = 0):
        self.time = t0
        self.dt = 0

    def update_time(self):
        self.time += self.dt