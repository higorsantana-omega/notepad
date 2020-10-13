from tkinter import *
import os
from tkinter import filedialog

root = Tk()


class Notepad:

    def __init__(self, master=None):
        self.root = root
        self.menubar = Menu(self.root)
        root.config(menu=self.menubar)
        self.window()
        self.button()
        root.mainloop()

    def window(self):
        self.root.geometry('500x600')
        self.root.title('Notepad')

    def button(self):
        self.filemenu = Menu(self.menubar)
        self.menubar.add_cascade(label='Arquivo', menu=self.filemenu)
        self.filemenu.add_command(label='Abrir...', command=self.open_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Salvar como', command=self.save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Sair', command=self.quit_file)

        self.editmenu = Menu(self.menubar)
        self.menubar.add_cascade(label='Editar', menu=self.editmenu)
        self.editmenu.add_command(label='Cortar', command=self.cut, accelerator="Ctrl+R")
        self.editmenu.add_command(label='Copiar', command=self.copy, accelerator="Ctrl+C")
        self.editmenu.add_command(label='Colar', command=self.paste, accelerator="Ctrl+V")
        self.editmenu.add_separator()
        self.editmenu.add_command(label='Limpar', command=self.clear)


        self.entry = Text(self.root, height=33, width=58, wrap=WORD)
        self.entry.place(x=10, y=50)


    def cut(self):
        self.entry.event_generate("<<Cut>>")
    def paste(self):
        self.entry.event_generate("<<Paste>>")
    def copy(self):
        self.entry.event_generate("<<Copy>>")
    
    # Save file
    def save_file(self):
        # asks if you want to save the location
        self.open_file = filedialog.asksaveasfile(
            mode='w', defaultextension=".txt"
            )
        if self.open_file is None:
            return
        self.text = str(entry.get(1.0, END))
        self.open_file.write(text)
        self.open_file.close()

    def clear(self):
        self.entry.delete(1.0, END)

    def open_file(self):
        self.file = filedialog.askopenfile(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
            )

        if self.file is not None:
            self.content= file.read()
        self.entry.insert(INSERT, content)

    def quit_file(self):
        self.root.destroy()

Notepad(root)
