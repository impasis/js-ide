from tkinter import *
from tkinter import filedialog


class FileMultiButton:
    def __init__(self, __class, text, x, y):
        self.__class = __class
        self.text = text
        self.x = x
        self.y = y
        self.win = __class.screen
        self.multi_button = Menubutton(self.win,
                                       text=self.text,
                                       relief="flat")
        self.menu = Menu(self.multi_button, tearoff=False)
        self.type = None

    def open_file(self, event=None):
        filepath = filedialog.askopenfilename()
        if filepath != "":
            try:
                with open(filepath, "r") as file:
                    file.read()
            except UnicodeDecodeError:
                return

            self.__class.name = filepath
            self.__class.screen.title(filepath)
            st = filepath.split('/')[-1].split('.')
            with open(filepath, "r") as file:
                text = file.read()
                self.__class.editor.main_entry.delete("1.0", END)
                self.__class.editor.main_entry.insert("1.0", text)

            if len(st) == 2:
                self.type = st[-1]
                if st[-1] == "js":
                    self.__class.editor.main_entry.bind('<KeyRelease>', self.__class.js_syntax)
                    self.__class.prev_text += " "
                    self.__class.js_syntax(self.__class.main_theme)

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
            self.__class.screen.title(filepath)

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

        options = ["New File  (Ctrl+N)",
                   "Open File  (Ctrl+O)",
                   "Save  (Ctrl+S)",
                   "Save As  (Ctrl+G)"]

        self.menu.add_command(label=options[0])
        self.menu.add_command(label=options[1], command=self.open_file)
        self.menu.add_command(label=options[2], command=self.fast_save_file)
        self.menu.add_command(label=options[3], command=self.save_file)

        # ENG.
        self.__class.screen.bind("<Control-s>", self.fast_save_file)
        self.__class.screen.bind("<Control-g>", self.save_file)
        self.__class.screen.bind("<Control-o>", self.open_file)

        # command=lambda opt=el: self.change_theme(opt)
