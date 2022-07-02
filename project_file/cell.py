from tkinter import *
from settings import mine_number, Gridsize_width, Gridsize_height
from utils import height_percent

class Cell:
    flag_number = mine_number
    flag_lbl = None
    cell_number = Gridsize_width*Gridsize_height
    cell_lbl = None

    def __init__(self, is_mine=False, is_opened=False, is_flag=False):
        self.is_mine = False
        self.is_opened = False
        self.is_flag = False

    def createcell(self, frame):
        btn = Button(frame, text="", width=4, height=2)
        btn.bind("<Button-1>", self.left_click)
        btn.bind("<Button-3>", self.right_click)
        return btn

    def left_click(self, event):
        if not self.is_opened:
            self.is_opened = True
            Cell.cell_number -= 1
            Cell.cell_lbl.config(text=f"Flag Numbers: {Cell.cell_number}")

    def right_click(self, event):
        if not self.is_flag:
            self.is_flag = True
            Cell.flag_number -= 1
            Cell.flag_lbl.config(text=f"Flag Numbers: {Cell.flag_number}")

    def create_lbl(self, frame):
        Cell.cell_lbl = Label(frame, text=f"Cell Numbers: {Cell.cell_number}", bg="#18191a", fg="burlywood",font=("Times New Roman", 12))
        Cell.cell_lbl.place(x=5, y=height_percent(10))
        Cell.flag_lbl = Label(frame, text=f"Flag Numbers: {Cell.flag_number}", bg="#18191a", fg="burlywood",font=("Times New Roman", 12))
        Cell.flag_lbl.place(x=8, y=height_percent(18))


        

