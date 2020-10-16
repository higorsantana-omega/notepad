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
        self.filemenu.add_command(label='Novo', command=self.new_file)
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


        self.entry = Text(self.root, wrap=WORD)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.entry.grid(sticky = N + E + S + W)


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
        

    # Save file
    def save_file(self):
        # asks if you want to save the location
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

    def open_file(self):
        # self.file = filedialog.askopenfile(
        #     defaultextension=".txt",
        #     filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
        #     )
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

    def quit_file(self):
        self.root.destroy()

Notepad(root)
