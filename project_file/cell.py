from tkinter import *
from tkinter import messagebox
from random import sample
from settings import mine_number, Gridsize_width, Gridsize_height
from utils import height_percent
# import ctypes

class Cell:
    mouse_click = 1
    flag_number = mine_number
    flag_lbl = None
    cell_number = Gridsize_width*Gridsize_height
    cell_lbl = None

    all_cell = []

    def __init__(self, i, j, is_opened=False, is_mine=False, is_flag=False):
        self.is_opened = False
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

    def randomize_mines(self):
        un_mine_cells=[self.surrounded_cells(self.i+i, self.j+j) for i in [-1, 0, 1] for j in [-1, 0, 1]
                       if self.surrounded_cells(self.i+i, self.j+j)!= None]
        candidate_cells = [cell for cell in Cell.all_cell if cell not in un_mine_cells]
        mines_li = sample(candidate_cells, 31)
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
            # self.empty_cell()
        self.is_opened = True
        self.cell_btn_object.config(state=DISABLED)
        self.cell_btn_object.unbind("<Button-1>")
        self.cell_btn_object.unbind("<Button-3>")

    def show_mine(self):
        self.cell_btn_object.config(text="mine", bg="red", fg="white")
        for cell in Cell.all_cell:
            cell.cell_btn_object.config(state=DISABLED)
            cell.cell_btn_object.unbind("<Button-1>")
            cell.cell_btn_object.unbind("<Button-3>")
            if cell.is_mine:
                cell.cell_btn_object.config(text="mine", bg="red", fg="white")
        # ctypes.windll.user32.MessageBoxW(0, "You clicked on a Mine!!", "Game Over", 0)
        messagebox.showinfo(message="You clicked on a Mine!!", title="Game Over")

    @staticmethod
    def surrounded_cells(x, y):
        for cell in Cell.all_cell:
            if cell.i==x and cell.j==y:
                return cell

    def left_click(self, event):
        if Cell.mouse_click != 1:
            Cell.cell_number -= 1
            Cell.cell_lbl.config(text=f"Cell : {Cell.cell_number}")
            if self.is_mine:
                self.show_mine()
            else:
                self.show_cell()
                if self.cell_btn_object.cget("text") == "":
                    self.empty_cell()
                if Cell.cell_number == mine_number:
                    messagebox.showinfo(title="Win", message="Congratulations!!You Won the Game!!")
                    # ctypes.windll.user32.MessageBoxW(0, "Congratulations!!You Won the Game!!", "The End", 0)
        else:
            self.first_click()
            Cell.cell_number -= 1
            Cell.cell_lbl.config(text=f"Cell : {Cell.cell_number}")

    def right_click(self, event):
        if not self.is_flag:
            if Cell.flag_number>0:
                self.is_flag = True
                Cell.flag_number -= 1
                Cell.flag_lbl.config(text=f"Flag : {Cell.flag_number}")
                self.cell_btn_object.config(text="F", bg="orange", fg="white", state=DISABLED)
                self.cell_btn_object.unbind("<Button-1>")
        else:
            self.is_flag = False
            Cell.flag_number += 1
            Cell.flag_lbl.config(text=f"Flag : {Cell.flag_number}")
            self.cell_btn_object.config(text="", bg="SystemButtonFace", fg="black", state=NORMAL)
            self.cell_btn_object.bind("<Button-1>", self.left_click)

    def first_click(self):
        self.randomize_mines()
        self.show_cell()
        self.empty_cell()
        Cell.mouse_click += 1

    def empty_cell(self):
        picked_cells = [self]
        while picked_cells != []:
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if i!=0 or j!=0:
                        picked_cell = picked_cells[0].surrounded_cells(picked_cells[0].i+i, picked_cells[0].j+j)
                        if picked_cell != None and not picked_cell.is_opened:
                            picked_cell.show_cell()
                            Cell.cell_number -= 1
                            Cell.cell_lbl.config(text=f"Cell : {Cell.cell_number}")
                            if picked_cell.cell_btn_object.cget("text") == "":
                                picked_cells.append(picked_cell)
            picked_cells.pop(0)


    @classmethod
    def create_lbl(cls, frame):
        Cell.cell_lbl = Label(frame, text=f"Cell : {Gridsize_width*Gridsize_height}", bg="#18191a", fg="burlywood", font=("Times New Roman", 15))
        Cell.cell_lbl.place(x=5, y=height_percent(10))
        Cell.cell_number = Gridsize_width * Gridsize_height
        Cell.flag_lbl = Label(frame, text=f"Flag : {mine_number}", bg="#18191a", fg="burlywood", font=("Times New Roman", 15))
        Cell.flag_lbl.place(x=8, y=height_percent(18))
        Cell.flag_number = mine_number

    def __repr__(self):
        return f"cell({self.i}, {self.j})"

