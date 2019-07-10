from side import *
from cube import *
from tkinter import *

# # # # # # # # # # # # # # # # # # # # GLOBALS # # # # # # # # # # # # # # # # # # # #
rows = 12
cols = 9
cell_size = 50

# Dictionaries to hold color/number pair for translation between cube object and UI
color_dict = dict({"RED": 0, "ORANGE": 1, "YELLOW": 2, "GREEN": 3, "BLUE": 4, "WHITE": 5, "BLACK": 6})
inv_color = {val: key for key, val in color_dict.items()}


# # # # # # # # # # # # # # # # # # # # METHODS # # # # # # # # # # # # # # # # # # # #
def update_colors(grid):
    for i in range(rows):  # Rows
        for j in range(cols):  # Columns
            cells[(i, j)].config(bg=inv_color[grid[i, j]])


def button_turn(cube, side, clockwise):
    cube.turn_side(side, clockwise)
    update_colors(cube.flatten())


# # # # # # # # # # # # # # # # # # # # SETUP # # # # # # # # # # # # # # # # # # # #
topSide = Side(color_dict["BLUE"])
bottomSide = Side(color_dict["GREEN"])
frontSide = Side(color_dict["RED"])
backSide = Side(color_dict["ORANGE"])
leftSide = Side(color_dict["WHITE"])
rightSide = Side(color_dict["YELLOW"])

rubik = Cube(topSide, bottomSide, leftSide, rightSide, frontSide, backSide)

# UI Initializations
window = Tk()
window.title("Rubik's Cube Solver")
window.geometry('670x600')
window.resizable(False, False)

rubik_frame = Frame(window, bg="black")
rubik_frame.grid_propagate(0)
button_frame = Frame(window, bg="grey", height=600, width=150)
rubik_frame.pack(side=LEFT, fill=BOTH, expand=True)
button_frame.pack(side=RIGHT, fill=BOTH)

cells = {}
for i in range(rows):  # Rows
    for j in range(cols):  # Columns
        cell = Frame(rubik_frame, bg="BLACK", height=cell_size, width=cell_size, bd=1, relief="solid")
        cell.grid(row=i, column=j)
        cells[(i, j)] = cell

lblcw = Label(button_frame, text="Clockwise", width=15)
lblcw.grid(row=0, column=0)
lblccw = Label(button_frame, text="Counter-Clockwise")
lblccw.grid(row=0, column=1)
tcw = Button(button_frame, height=2, width=14, text="TOP", command=lambda: button_turn(rubik, "TOP", True))
tcw.grid(row=1, column=0)
tccw = Button(button_frame, height=2, width=14, text="TOP", command=lambda: button_turn(rubik, "TOP", False))
tccw.grid(row=1, column=1)
bcw = Button(button_frame, height=2, width=14, text="BOTTOM", command=lambda: button_turn(rubik, "BOTTOM", True))
bcw.grid(row=2, column=0)
bccw = Button(button_frame, height=2, width=14, text="BOTTOM", command=lambda: button_turn(rubik, "BOTTOM", False))
bccw.grid(row=2, column=1)
fcw = Button(button_frame, height=2, width=14, text="FRONT", command=lambda: button_turn(rubik, "FRONT", True))
fcw.grid(row=3, column=0)
fccw = Button(button_frame, height=2, width=14, text="FRONT", command=lambda: button_turn(rubik, "FRONT", False))
fccw.grid(row=3, column=1)
bcw = Button(button_frame, height=2, width=14, text="BACK", command=lambda: button_turn(rubik, "BACK", True))
bcw.grid(row=4, column=0)
bccw = Button(button_frame, height=2, width=14, text="BACK", command=lambda: button_turn(rubik, "BACK", False))
bccw.grid(row=4, column=1)
lcw = Button(button_frame, height=2, width=14, text="LEFT", command=lambda: button_turn(rubik, "LEFT", True))
lcw.grid(row=5, column=0)
lccw = Button(button_frame, height=2, width=14, text="LEFT", command=lambda: button_turn(rubik, "LEFT", False))
lccw.grid(row=5, column=1)
rcw = Button(button_frame, height=2, width=14, text="RIGHT", command=lambda: button_turn(rubik, "RIGHT", True))
rcw.grid(row=6, column=0)
rccw = Button(button_frame, height=2, width=14, text="RIGHT", command=lambda: button_turn(rubik, "RIGHT", False))
rccw.grid(row=6, column=1)

rubik.turn_side("FRONT", True)
update_colors(rubik.flatten())
window.mainloop()
