from tkinter import *


class Editor:
    def __init__(self, window, theme):
        self.win = window
        self.theme = theme
        self.label = Label(self.win, text='', font=("Arial", 6), height=2)
        self.main_entry = Text(master=self.win, width=200, height=100, font=('Consolas', 15),
                               background=self.theme["background"], foreground=self.theme["txt_color"],
                               insertbackground=self.theme["txt_color"],
                               relief=FLAT, borderwidth=30, tabs=56)
        self.main_entry.tag_configure('sel', background=self.theme['sel_color'])
        self.__class = None

    def draw(self):
        self.label.pack()
        self.main_entry.pack(fill=BOTH, expand=1)
