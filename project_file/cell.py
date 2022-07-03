from tkinter import *
from random import sample
from settings import mine_number, Gridsize_width, Gridsize_height
from utils import height_percent
import ctypes

class Cell:
    flag_number = mine_number
    flag_lbl = None
    cell_number = Gridsize_width*Gridsize_height
    cell_lbl = None

    all_cell = []

    def __init__(self, i, j, is_mine=False, is_flag=False):
        self.is_mine = False
        self.is_flag = False
        self.i = i
        self.j = j

        Cell.all_cell.append(self)

        self.cell_btn_object = None


    def createcell(self, frame):
        btn = Button(frame, text="", width=4, height=2)
        btn.bind("<Button-1>", self.left_click)
        btn.bind("<Button-3>", self.right_click)
        self.cell_btn_object = btn
        self.cell_btn_object.grid(column=self.i, row=self.j, padx=1, pady=1)

    @staticmethod
    def randomize_mines():
        mines_li = sample(Cell.all_cell, 31)
        for mine in mines_li:
            mine.is_mine = True

    def show_cell(self):
        counter = 0
        surround = [self.surrounded_cells(self.i+i, self.j+j) for i in [-1, 0, 1] for j in [-1, 0, 1]
                    if self.surrounded_cells(self.i+i, self.j+j)!=None]
        for surr_cell in surround:
            if surr_cell.is_mine:
                counter += 1
        if counter!=0:
            self.cell_btn_object.config(text=f"{counter}")
        else:
            self.cell_btn_object.config(bg="burlywood")
        self.cell_btn_object.config(state=DISABLED)
        self.cell_btn_object.unbind("<Button-1>")
        self.cell_btn_object.unbind("<Button-3>")

    def show_mine(self):
        self.cell_btn_object.config(text="mine", bg="red", fg="white")
        for cell in Cell.all_cell:
            if cell.is_mine:
                cell.cell_btn_object.config(text="mine", bg="red", fg="white")
        ctypes.windll.user32.MessageBoxW(0, "You clicked on a Mine!!", "Game Over", 0)

    @staticmethod
    def surrounded_cells(x, y):
        for cell in Cell.all_cell:
            if cell.i==x and cell.j==y:
                return cell

    def left_click(self, event):
        self.is_opened = True
        Cell.cell_number -= 1
        Cell.cell_lbl.config(text=f"Cell Numbers: {Cell.cell_number}")
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    def right_click(self, event):
        if not self.is_flag:
            self.is_flag = True
            Cell.flag_number -= 1
            Cell.flag_lbl.config(text=f"Flag Numbers: {Cell.flag_number}")
            # self.flag_cell()

    @classmethod
    def create_lbl(cls, frame):
        Cell.cell_lbl = Label(frame, text=f"Cell Numbers: {Cell.cell_number}", bg="#18191a", fg="burlywood", font=("Times New Roman", 12))
        Cell.cell_lbl.place(x=5, y=height_percent(10))
        Cell.flag_lbl = Label(frame, text=f"Flag Numbers: {Cell.flag_number}", bg="#18191a", fg="burlywood", font=("Times New Roman", 12))
        Cell.flag_lbl.place(x=8, y=height_percent(18))

    def __repr__(self):
        return f"cell({self.i}, {self.j})"
        

