from tkinter import *
from tkinter import filedialog


class FileMultiButton:
    def __init__(self, __class, text, x, y, win):
        self.__class = __class
        self.text = text
        self.x = x
        self.y = y
        self.win = win
        self.multi_button = Menubutton(self.win,
                                       text=self.text,
                                       relief="flat")
        self.menu = Menu(self.multi_button, tearoff=False)

    def open_file(self, event=None):
        filepath = filedialog.askopenfilename()
        if filepath != "":
            self.__class.name = filepath
            st = filepath.split('/')
            new = ''
            for el in st[:-1]:
                new += el + '\\'
            self.__class.cmd_directory = new
            with open(filepath, "r") as file:
                text = file.read()
                self.__class.editor.main_entry.delete("1.0", END)
                self.__class.editor.main_entry.insert("1.0", text)
            self.__class.syntax(self.__class.main_theme)

    # Глобальное сохранение
    def save_file(self, event=None):
        filepath = filedialog.asksaveasfilename()
        if filepath != "":
            st = filepath.split('/')
            new = ''
            for el in st[:-1]:
                new += el + '\\'
            self.__class.cmd_directory = new

            self.__class.name = filepath

            text = self.__class.editor.main_entry.get("1.0", END)
            with open(filepath, "w") as file:
                file.write(text)

    def fast_save_file(self, event=None):
        if self.__class.name != "":
            text = self.__class.editor.main_entry.get("1.0", END)
            with open(self.__class.name, "w") as file:
                file.write(text)

    def show(self):
        self.multi_button.place(x=self.x, y=self.y)
        self.multi_button.configure(menu=self.menu)

        options = ["New File", "Open File", "Save", "Save As"]

        # HOT KEYS - TESTS

        for el in options:
            self.menu.add_command(label=el)

            # command=lambda opt=el: self.change_theme(opt)
