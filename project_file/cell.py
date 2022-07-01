from tkinter import *

class Cell:
    def __init__(self, is_mine=False, is_opened=False, is_flag=False):
        self.is_mine = False
        self.is_opened = False
        self.is_flag = False

    def createcell(self, frame):
        return Button(frame, text="", width=4, height=2)

