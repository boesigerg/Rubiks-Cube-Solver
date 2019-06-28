from side import *
from cube import *


topSide = Side(Color.BLUE)
bottomSide = Side(Color.GREEN)
frontSide = Side(Color.RED)
backSide = Side(Color.ORANGE)
leftSide = Side(Color.WHITE)
rightSide = Side(Color.YELLOW)

rubik = Cube(topSide, bottomSide, leftSide, rightSide, frontSide, backSide)

rubik.turn_side("TOP", True)
rubik.turn_side("BOTTOM", True)
print(">>>>>>>>>>>>>>>START")
print(rubik)
rubik.turn_side("LEFT", True)
rubik.turn_side("RIGHT", True)
print(">>>>>>>>>>>>>>>TURN 1")
print(rubik)
rubik.turn_side("LEFT", True)
rubik.turn_side("RIGHT", True)
print(">>>>>>>>>>>>>>>TURN 2")
print(rubik)
rubik.turn_side("LEFT", False)
rubik.turn_side("RIGHT", False)
print(">>>>>>>>>>>>>>>TURN 3")
print(rubik)
rubik.turn_side("LEFT", False)
rubik.turn_side("RIGHT", False)
print(">>>>>>>>>>>>>>>TURN 4")
print(rubik)
