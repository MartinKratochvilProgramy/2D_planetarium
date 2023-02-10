from settings import TIME_SCALE_SPEED

class Clock:
    def __init__(self, time_scale = 1, t0 = 0):
        self.time_scale = time_scale
        self.time = t0
        self.dt = 0

    def update_time(self):
        self.time += self.dt * self.time_scale
        
    def increase_time_scale(self):
        self.time_scale = round(self.time_scale * (1 + TIME_SCALE_SPEED), 4)
    
    def decrease_time_scale(self):
        self.time_scale = round(self.time_scale * (1 - TIME_SCALE_SPEED), 4)


    