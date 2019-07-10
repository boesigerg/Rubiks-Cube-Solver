import numpy as np


class Cube:
    def __init__(self, top, bottom, left, right, front, back):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.front = front
        self.back = back

    def flatten(self):
        flattened = np.empty((12, 9), np.int8)
        flattened.fill(6)
        for row in range(3):
            flattened[0+row, 3:6] = self.top.grid[row]
        for row in range(3):
            flattened[3+row, 0:3] = self.left.grid[row]
        for row in range(3):
            flattened[3+row, 3:6] = self.front.grid[row]
        for row in range(3):
            flattened[3+row, 6:9] = self.right.grid[row]
        for row in range(3):
            flattened[6+row, 3:6] = self.bottom.grid[row]
        for row in range(3):
            flattened[9+row, 3:6] = self.back.grid[row]
        return flattened

    def turn_side(self, side, clockwise):
        # For a given side:
        # Turn itself using side.turn()
        # Swap edges of surrounding sides
        # Ensure translated rows are oriented properly
        if side == "TOP":
            self.top.turn(clockwise)
            self.back.grid[2], self.right.grid[0], self.front.grid[0], self.left.grid[0] = turn_helper(
                self.back.grid[2], self.right.grid[0], self.front.grid[0], self.left.grid[0], clockwise)
            self.back.grid[2] = np.flip(self.back.grid[2])
            if clockwise:
                self.right.grid[0] = np.flip(self.right.grid[0])
            else:
                self.left.grid[0] = np.flip(self.left.grid[0])
        elif side == "BOTTOM":
            self.bottom.turn(clockwise)
            self.front.grid[2], self.right.grid[2], self.back.grid[0], self.left.grid[2] = turn_helper(
                self.front.grid[2], self.right.grid[2], self.back.grid[0], self.left.grid[2], clockwise)
            self.back.grid[0] = np.flip(self.back.grid[0])
            if clockwise:
                self.left.grid[2] = np.flip(self.left.grid[2])
            else:
                self.right.grid[2] = np.flip(self.right.grid[2])
        elif side == "LEFT":
            self.left.turn(clockwise)
            self.top.grid[:, 0], self.front.grid[:, 0], self.bottom.grid[:, 0], self.back.grid[:, 0] = turn_helper(
                self.top.grid[:, 0], self.front.grid[:, 0], self.bottom.grid[:, 0], self.back.grid[:, 0], clockwise)
        elif side == "RIGHT":
            self.right.turn(clockwise)
            self.top.grid[:, 2], self.back.grid[:, 2], self.bottom.grid[:, 2], self.front.grid[:, 2] = turn_helper(
                self.top.grid[:, 2], self.back.grid[:, 2], self.bottom.grid[:, 2], self.front.grid[:, 2], clockwise)
        elif side == "FRONT":
            self.front.turn(clockwise)
            self.top.grid[2], self.right.grid[:, 0], self.bottom.grid[0], self.left.grid[:, 2] = turn_helper(
                self.top.grid[2], self.right.grid[:, 0], self.bottom.grid[0], self.left.grid[:, 2], clockwise)
            if clockwise:
                self.top.grid[2] = np.flip(self.top.grid[2])
                self.bottom.grid[0] = np.flip(self.bottom.grid[0])
            else:
                self.left.grid[:, 2] = np.flip(self.left.grid[:, 2])
                self.right.grid[:, 0] = np.flip(self.right.grid[:, 0])
        elif side == "BACK":
            self.back.turn(clockwise)
            self.bottom.grid[2], self.right.grid[:, 2], self.top.grid[0], self.left.grid[:, 0] = turn_helper(
                self.bottom.grid[2], self.right.grid[:, 2], self.top.grid[0], self.left.grid[:, 0], clockwise)
            if clockwise:
                self.left.grid[:, 0] = np.flip(self.left.grid[:, 0])
                self.right.grid[:, 2] = np.flip(self.right.grid[:, 2])
            else:
                self.top.grid[0] = np.flip(self.top.grid[0])
                self.bottom.grid[2] = np.flip(self.bottom.grid[2])


# turn_helper, for lack of a better name, contains the logic for swapping
# single rows of the four sides affected by a given sides turn
def turn_helper(up, right, down, left, clockwise):
    temp = []
    temp[:] = up
    if clockwise:
        up[:] = left
        left[:] = down
        down[:] = right
        right[:] = temp
    else:
        up[:] = right
        right[:] = down
        down[:] = left
        left[:] = temp
    return up, right, down, left

