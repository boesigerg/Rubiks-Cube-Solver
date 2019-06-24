class Cube:
    def __init__(self, top, bottom, left, right, front, back):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.front = front
        self.back = back

    def __str__(self):
        return ("FRONT\n"
                + str(self.front)
                + "\nTOP\n"
                + str(self.top)
                + "\nBACK\n"
                + str(self.back)
                + "\nBOTTOM\n"
                + str(self.bottom)
                + "\nLEFT\n"
                + str(self.left)
                + "\nRIGHT\n"
                + str(self.right))

    def turn_side(self, side, clockwise):
        pass

