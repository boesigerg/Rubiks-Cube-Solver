import numpy as np

class Side:
    def __init__(self, color):
        self.grid = np.empty((3,3), np.int8)
        self.grid.fill(color)

    def __str__(self):
        return str(self.grid)

    def turn(self, clockwise):
        if clockwise:
            self.grid = np.rot90(self.grid, -1)
        else:
            self.grid = np.rot90(self.grid, 1)
