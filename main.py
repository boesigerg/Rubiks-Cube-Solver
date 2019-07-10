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

# UI Initializations
window = Tk()
rubik_frame = Frame(window, bg="black")
rubik_frame.grid_propagate(0)
button_frame = Frame(window, bg="grey", height=600, width=150)

cells = {}
for i in range(rows):  # Rows
    for j in range(cols):  # Columns
        cell = Frame(rubik_frame, bg="BLACK", height=cell_size, width=cell_size, bd=1, relief="solid")
        cell.grid(row=i, column=j)
        cells[(i, j)] = cell


# # # # # # # # # # # # # # # # # # # # METHODS # # # # # # # # # # # # # # # # # # # #
def update_colors(grid):
    for i in range(rows):  # Rows
        for j in range(cols):  # Columns
            cells[(i, j)].config(bg=inv_color[grid[i, j]])


# # # # # # # # # # # # # # # # # # # # SETUP # # # # # # # # # # # # # # # # # # # #
topSide = Side(color_dict["BLUE"])
bottomSide = Side(color_dict["GREEN"])
frontSide = Side(color_dict["RED"])
backSide = Side(color_dict["ORANGE"])
leftSide = Side(color_dict["WHITE"])
rightSide = Side(color_dict["YELLOW"])

rubik = Cube(topSide, bottomSide, leftSide, rightSide, frontSide, backSide)

window.title("Rubik's Cube Solver")
window.geometry('600x600')
window.resizable(False, False)

rubik_frame.pack(side=LEFT, fill=BOTH, expand=True)
button_frame.pack(side=RIGHT, fill=BOTH)

rubik.turn_side("FRONT", True)
update_colors(rubik.flatten())
window.mainloop()
