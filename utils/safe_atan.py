import numpy as np
import math

def safe_atan(d1, d2):
    if (d1 == 0):
        return 0
    if (d2 == 0): 
        if (d1 > 0):
            return math.pi / 2 * 180 / math.pi
        if (d1 < 0):
            return -math.pi / 2 * 180 / math.pi
    
    return np.arctan(d1 / d2) * 180 / math.pi