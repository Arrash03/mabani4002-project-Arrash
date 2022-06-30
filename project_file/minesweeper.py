from tkinter import *
from settings import Width, Height

window = Tk()
# base info
window.title("Minesweeper Game")
window.resizable(False, False)
window.geometry(f"{Width}x{Height}")
window.config(bg="black")



window.mainloop()