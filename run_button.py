from run_js import run_js
from tkinter import *


class RunJsButton:
    def __init__(self, __class, x, y, relief, symbol, color):
        self.x = x
        self.y = y
        self.relief = relief
        self.symbol = symbol
        self.color = color
        self.__class = __class

    def run(self):
        ...


