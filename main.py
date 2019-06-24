from side import *
from cube import *


topSide = Side(Color.BLUE)
bottomSide = Side(Color.GREEN)
frontSide = Side(Color.RED)
backSide = Side(Color.ORANGE)
leftSide = Side(Color.WHITE)
rightSide = Side(Color.YELLOW)

rubik = Cube(topSide, bottomSide, leftSide, rightSide, frontSide, backSide)
print(rubik)
