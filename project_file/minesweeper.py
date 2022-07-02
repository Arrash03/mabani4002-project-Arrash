from tkinter import *
from cell import Cell
from settings import Width, Height, Gridsize_width, Gridsize_height
from utils import width_percent, height_percent

window = Tk()
# base info
window.title("Minesweeper Game")
window.resizable(False, False)
window.geometry(f"{Width}x{Height}")
window.config(bg="black")

# main part of window
frame1 = Frame(window, width=width_percent(15), height=Height, bg="#18191a")
frame1.place(x=0, y=0)

frame2 = Frame(window, width=width_percent(70), height=Height, bg="#1f2123")
frame2.place(x=width_percent(15), y=0)

frame2_1 = Frame(frame2, width=width_percent(70), height=Height, bg="burlywood", highlightbackground="#c88a3b", highlightthickness=2)
frame2_1.grid(padx=18, pady=6)

frame3 = Frame(window, width=width_percent(15), height=Height, bg="#18191a")
frame3.place(x=width_percent(85), y=0)

# creating cells
for i in range(Gridsize_width):
    for j in range(Gridsize_height):
        c = Cell()
        cell = c.createcell(frame2_1)
        cell.grid(column=i, row=j, padx=1, pady=1)

# frame1
Cell.create_lbl(Cell, frame1)

# frame2
Button(frame3, text="Play Again", command=None, bg="burlywood", fg="white",
       font=("Times New Roman", 15)).place(x=10, y=height_percent(85))


window.mainloop()