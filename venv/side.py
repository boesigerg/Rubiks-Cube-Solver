import numpy

class Side:
    def __init__(self, color):
        self.grid = numpy.empty((3,3))
        self.grid.fill(color)

    def __str__(self):
        return self.grid

    def turn(self, clockwise):
        #some magic happens here, thanks to stackoverflow
        if clockwise:
            self.grid = list(zip(*self.grid[::-1]))
        else:
            self.grid = list(zip(*reversed(self.grid)))

    def get_row(self):
        pass

    def set_row(self):
        pass