import numpy as np
from enum import Enum

class Color(Enum):
    RED = 0
    ORANGE = 1
    YELLOW = 2
    GREEN = 3
    BLUE = 4
    WHITE = 5

class Side:
    def __init__(self, color):
        self.grid = np.empty((3,3), np.int8)
        self.grid.fill(color.value)

    def __str__(self):
        return str(self.grid)

    def turn(self, clockwise):
        #some magic happens here, thanks to stackoverflow
        #Gist:Alter list as though it were a 3x3 matrix being turned 90 degrees
        if clockwise:
            self.grid = np.rot90(self.grid, -1)
        else:
            self.grid = np.rot90(self.grid, 1)

    def get_row(self, isCol, element):
        if isCol:
            val = self.grid[:,element]
        else:
            val = self.grid[element]
        return val

    def set_row(self, isCol, element, val):
        if isCol:
            self.grid[:,element] = val
        else:
            self.grid[element] = val