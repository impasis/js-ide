from tkinter import *
from tkinter import filedialog
from run_js import run_js
from editor import Editor

from vscode_theme_sett import *
from vscode_light_theme_sett import *
from monokai_theme_sett import *
from github_theme_sett import *
from github_dark_theme_sett import *

import re


class ThemeMultiButton:
    def __init__(self, text, x, y, win: Tk, btn_width, btn_height):
        self.text = text
        self.x = x
        self.y = y
        self.win = win
        self.btn_width = btn_width
        self.btn_height = btn_height
        self.multi_button = Menubutton(self.win,
                                       text=self.text,
                                       relief="flat")
        self.menu = Menu(self.multi_button, tearoff=False)
        self.themes = {"Dark (Visual Studio)": vscode_colors,
                       "Light (Visual Studio)": vscode_light_colors,
                       "Monokai": monokai_colors,
                       "Dark (GitHub)": github_dark_colors,
                       "Light (GitHub)": github_colors}
        self.themes_syntax = {"Dark (Visual Studio)": js_syntax_vscode,
                              "Light (Visual Studio)": js_syntax_vscode_light,
                              "Monokai": js_syntax_monokai,
                              "Dark (GitHub)": js_syntax_github_dark,
                              "Light (GitHub)": js_syntax_github}

    def change_theme(self, theme):
        app.main_theme = self.themes_syntax[theme]
        __editor = Editor(self.win, self.themes[theme])
        app.editor.main_entry.destroy()
        app.editor.label.destroy()
        app.editor = __editor
        app.editor.draw()
        app.editor.main_entry.bind('<KeyRelease>', app.syntax)

    def show(self):
        self.multi_button.place(x=self.x, y=self.y)
        self.multi_button.configure(menu=self.menu)
        # self.multi_button.config(width=self.btn_width, height=self.btn_height)
        options = ["Dark (Visual Studio)",
                   "Light (Visual Studio)",
                   "Monokai",
                   "Dark (GitHub)",
                   "Light (GitHub)"]

        for el in options:
            self.menu.add_command(label=el, command=lambda opt=el: self.change_theme(opt))


class Main:
    def __init__(self, width, height, title, screen, local_editor, local_name):
        self.width = width
        self.height = height
        self.title = title
        self.screen = screen
        self.editor = local_editor
        self.name = local_name
        self.cmd_win = None
        self.command_text = ""
        self.cmd_entry = None
        self.cmd_directory = None
        self.prev_text = ""
        self.main_theme = js_syntax_vscode

    def open_file(self, event=None):
        filepath = filedialog.askopenfilename()
        if filepath != "":
            self.name = filepath
            st = filepath.split('/')
            new = ''
            for el in st[:-1]:
                new += el + '\\'
            self.cmd_directory = new
            with open(filepath, "r") as file:
                text = file.read()
                self.editor.main_entry.delete("1.0", END)
                self.editor.main_entry.insert("1.0", text)
            self.syntax(self.main_theme)

    # Глобальное сохранение
    def save_file(self, event=None):
        filepath = filedialog.asksaveasfilename()
        if filepath != "":
            st = filepath.split('/')
            new = ''
            for el in st[:-1]:
                new += el + '\\'
            self.cmd_directory = new

            self.name = filepath

            text = self.editor.main_entry.get("1.0", END)
            with open(filepath, "w") as file:
                file.write(text)

    def fast_save_file(self, event=None):
        if self.name != "":
            text = self.editor.main_entry.get("1.0", END)
            with open(self.name, "w") as file:
                file.write(text)

    def syntax(self, event=None):
        if self.editor.main_entry.get('1.0', END) == self.prev_text:
            return

        for st in self.editor.main_entry.tag_names():
            self.editor.main_entry.tag_remove(st, '1.0', 'end')

        i = 0
        for syms, color in self.main_theme:
            for start, end in self.search(syms):
                self.editor.main_entry.tag_add(f"{i}", start, end)
                self.editor.main_entry.tag_config(f"{i}", foreground=color)

                i += 1
        self.prev_text = self.editor.main_entry.get('1.0', END)

    def search(self, syms, groupid=0):
        matches = []

        text = self.editor.main_entry.get('1.0', END).splitlines()

        for i, line in enumerate(text):
            for match in re.finditer(syms, line):
                matches.append(
                    (f"{i + 1}.{match.start()}", f"{i + 1}.{match.end()}")
                )

        return matches

    # Запуск
    def run(self, cmd):
        if cmd == "OK":
            self.screen.title(self.title)
            self.screen.state("zoomed")
            self.screen.geometry(f"{self.width}x{self.height}")
            choose_theme.show()
            self.editor.draw()
            self.editor.main_entry.bind('<KeyRelease>', self.syntax)

            self.screen.mainloop()


win = Tk()
editor = Editor(win, vscode_colors)
name = ""
choose_theme = ThemeMultiButton("Color Theme", 2, 0, win, 12, 1)

_w = win.winfo_screenwidth()  # размер по горизонтали
_h = win.winfo_screenheight()  # размер по вертикали
app = Main(_w, _h, "???", win, editor, name)

if __name__ == "__main__":
    app.run("OK")
