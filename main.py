from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox


root = Tk()


class Notepad:

    def __init__(self, master=None):
        self.root = root
        self.menubar = Menu(self.root)
        root.config(menu=self.menubar)
        self.window()
        self.button()
        root.mainloop()

    def window(self, **kwargs):
        self.w_height = 460
        self.w_width = 650
        self.root.title('Notepad')

        try:
            self.w_width = kwargs['width']
        except KeyError:
            pass

        try:
            self.w_width = kwargs['height']
        except KeyError:
            pass

        self.screenWidht = self.root.winfo_screenmmwidth()
        self.screenHeight = self.root.winfo_screenheight()
        self.left = (self.screenWidht / 2) - (self.w_width / 2)
        self.top = (self.screenHeight / 2) - (self.w_height / 2)

        self.root.geometry('%dx%d+%d+%d' % (self.w_width,
                                            self.w_height,
                                            self.left, self.top))

    def button(self):
        self.filemenu = Menu(self.menubar)
        self.menubar.add_cascade(label='Arquivo', menu=self.filemenu)
        self.filemenu.add_command(
            label='Novo', 
            command=self.new_file,
            accelerator="Ctrl+N"
            )
        self.filemenu.add_command(label='Abrir...', command=self.open_file, accelerator="Ctrl+O")
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Salvar como', command=self.save_file, accelerator="Ctrl+S")
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Sair', command=self.quit_file, accelerator="Ctrl+Q")

        self.editmenu = Menu(self.menubar)
        self.menubar.add_cascade(label='Editar', menu=self.editmenu)
        self.editmenu.add_command(label='Cortar', command=self.cut, accelerator="Ctrl+R")
        self.editmenu.add_command(label='Copiar', command=self.copy, accelerator="Ctrl+C")
        self.editmenu.add_command(label='Colar', command=self.paste, accelerator="Ctrl+V")
        self.editmenu.add_separator()
        self.editmenu.add_command(label='Limpar', command=self.clear, accelerator="Ctrl+L")

        self.helpmenu = Menu(self.menubar)
        self.menubar.add_cascade(label='Ajuda', menu=self.helpmenu)
        self.helpmenu.add_command(label='Sobre', command=self.about)


        self.entry = Text(self.root, wrap=WORD, selectbackground='#4682B4')
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.entry.grid(sticky = N + E + S + W)

    def about(self):
        self.msg = ('1.0.6' + '\nLeve editor de texto')
        messagebox.showinfo(title='Sobre', message=self.msg)

    def cut(self):
        self.entry.event_generate("<<Cut>>")
    def paste(self):
        self.entry.event_generate("<<Paste>>")
    def copy(self):
        self.entry.event_generate("<<Copy>>")
    
    def new_file(self):
        self.root.title('Sem nome')
        self.file = None
        self.entry.delete(1.0, END)

    def open_file(self):
        self.file = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
            )
        if self.file == "":
            self.file = None
        else:
            self.root.title(os.path.basename(self.file))
            self.entry.delete(1.0, END)
            self.nfile = open(self.file, "r")
            self.entry.insert(INSERT, self.nfile.read())
            self.nfile.close()
    
    def save_file(self):
        self.file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
            )
        if self.file == "":
            self.file = None
        else:
            self.nfile = open(self.file, "w")
            self.text = str(self.entry.get(1.0, END))
            self.nfile.write(self.text)
            self.nfile.close()
            self.root.title(os.path.basename(self.file))

    def clear(self):
        self.entry.delete(1.0, END)

    def quit_file(self):
        self.root.destroy()

Notepad(root)
