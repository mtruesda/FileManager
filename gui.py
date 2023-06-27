import tkinter as tk
# from tkinter import *
from FileManagement import *

class gui():
    def __init__(self):
        self.path = ''
        self.tree = None

        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title('File Manager')

        nmenu = tk.Menu(self.root)

        fileMenu = tk.Menu(nmenu, tearoff=0)
        # The fact that I needed to put lambda in here to make this work is ABSOLUTELY WILD
        fileMenu.add_command(label='New File', command=lambda: self.miniFile())
        fileMenu.add_command(label='New Folder', command=lambda: self.miniFolder)

        nmenu.add_cascade(label='File',  menu=fileMenu)

        self.root.config(menu=nmenu)

        self.root.mainloop()
    # allows user to name a file
    def miniFile(self):
        mini = tk.Tk()
        mini.geometry("300x100")
        mini.title('Add File')
        tk.Label(mini, text='Name the file').pack()
        text = tk.Text(mini, height=1, width=15).pack()
        tk.Button(mini, text='Submit', command=lambda: self.handleMiniFile(text, mini)).pack()
    # allows user to name a folder
    def miniFolder(self):
        mini = tk.Tk()
        mini.geometry("300x300")
        mini.title('Add Folder')
        tk.Label(mini, text='Name the folder').pack()
        text = tk.Text(mini, height=1, width=15).pack()
        tk.Button(mini, text='Submit', command=lambda: self.handleMiniFolder(text, mini)).pack()
    # handles submitting the button for a filename
    def handleMiniFile(self, text, mini):
        mini.destroy()
        self.tree = create_file(self.path, text.get(), self.tree)
        self.refresh()
    # handles submitting the button for a foldername
    def handleMiniFolder(self, text, mini):
        mini.destroy()
        create_folder(self.path, text.get())
        self.refresh()
    
    def refresh(self):
        return None

def func():
    print("hi")

gui()
