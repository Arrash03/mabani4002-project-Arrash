from tkinter import *
from settings import Width, Height
from utils import width_percent, height_percent

window = Tk()
# base info
window.title("Minesweeper Game")
window.resizable(False, False)
window.geometry(f"{Width}x{Height}")
window.config(bg="black")

# main part of window
frame1 = Frame(window, width=width_percent(15), height=Height, bg="black")
frame1.place(x=0, y=0)

frame2 = Frame(window, width=width_percent(70), height=Height, bg="black")
frame2.place(x=width_percent(15), y=0)

frame3 = Frame(window, width=width_percent(15), height=Height, bg="black")
frame3.place(x=width_percent(85), y=0)


window.mainloop()