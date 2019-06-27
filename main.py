from side import *
from cube import *


topSide = Side(Color.BLUE)
bottomSide = Side(Color.GREEN)
frontSide = Side(Color.RED)
backSide = Side(Color.ORANGE)
leftSide = Side(Color.WHITE)
rightSide = Side(Color.YELLOW)

rubik = Cube(topSide, bottomSide, leftSide, rightSide, frontSide, backSide)

rubik.turn_side("FRONT", True)
print("FRONT CW")
print(rubik)
rubik.turn_side("TOP", True)
print("TOP CW")
print(rubik)
rubik.turn_side("BACK", True)
print("BACK CW")
print(rubik)
rubik.turn_side("BOTTOM", True)
print("BOTTOM CW")
print(rubik)
rubik.turn_side("LEFT", True)
print("LEFT CW")
print(rubik)
rubik.turn_side("RIGHT", True)
print("RIGHT CW")
print(rubik)

rubik.turn_side("FRONT", False)
print("FRONT CCW")
print(rubik)
rubik.turn_side("TOP", False)
print("TOP CCW")
print(rubik)
rubik.turn_side("BACK", False)
print("BACK CCW")
print(rubik)
rubik.turn_side("BOTTOM", False)
print("BOTTOM CCW")
print(rubik)
rubik.turn_side("LEFT", False)
print("LEFT CCW")
print(rubik)
rubik.turn_side("RIGHT", False)
print("RIGHT CCW")
print(rubik)