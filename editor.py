from tkinter import *


class Editor:
    def __init__(self, window, theme):
        self.win = window
        self.main_entry = Text(master=self.win, width=200, height=100, font=('Consolas', 15),
                               background=theme["background"], foreground=theme["txt_color"],
                               insertbackground=theme["txt_color"],
                               relief=FLAT, borderwidth=30, tabs=56)
        self.main_entry.tag_configure('sel', background=theme['sel_color'])

    def draw(self):
        self.main_entry.pack(fill=BOTH, expand=1)
