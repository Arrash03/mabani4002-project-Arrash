from time import sleep
from tkinter import *
from cell import Cell
from settings import Width, Height, Gridsize_width, Gridsize_height
from utils import width_percent, height_percent

window = Tk()
# base info
window.title("Minesweeper Game")
window.resizable(False, False)
window.geometry(f"{Width}x{Height}")
window.config(bg="#4FA3A5")

# main part of window
frame1 = Frame(window, width=width_percent(15), height=Height, bg="#264248")
frame1.place(x=0, y=0)

frame2 = Frame(window, width=width_percent(70), height=Height, bg="#4FA3A5")
frame2.place(x=width_percent(15), y=0)

frame2_1 = Frame(frame2, width=width_percent(70), height=Height, bg="#FDAE38")
frame2_1.grid(padx=18, pady=6)

frame3 = Frame(window, width=width_percent(15), height=Height, bg="#264248")
frame3.place(x=width_percent(85), y=0)

# creating cells
for i in range(Gridsize_width):
    for j in range(Gridsize_height):
        c = Cell(i, j)
        c.createcell(frame2_1)
        frame2_1.update()

# frame1
Cell.create_lbl(frame1)

# frame2
def reset():
    Cell.mouse_click = 1
    for cell in Cell.all_cell:
        cell.cell_btn_object = None
        cell.is_opened = False
        cell.is_mine = False
        cell.is_flag = False
        cell.createcell(frame2_1)
        window.update()
    Cell.create_lbl(frame1)
    sleep(0.01)
    window.update()


Button(frame3, text="Play Again", command=reset, bg="#FDAE38", fg="#264248",
       font=("Cabinet Grotesk", 15, "bold")).place(x=10, y=height_percent(85))


window.mainloop()