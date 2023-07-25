import tkinter as tk
# from tkinter import *
from pydot_graph_util import *
from FileManagement import *

class gui():
    def __init__(self):
        self.path = home()
        self.tree = None

        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title('File Manager')

        self.nmenu = tk.Menu(self.root)

        self.fileMenu = tk.Menu(self.nmenu, tearoff=0)
        # The fact that I needed to put lambda in here to make this work is ABSOLUTELY WILD
        self.fileMenu.add_command(label='New File', command=lambda: self.miniFile())
        self.fileMenu.add_command(label='New Folder', command=lambda: self.miniFolder)

        self.nmenu.add_cascade(label='File',  menu=self.fileMenu)

        ### Start the user with an alphabetical list of files

        #self.outer = tk.Frame(self.root)
        #self.text = tk.Text(self.outer).pack(side='left')
        #self.sb = tk.Scrollbar(self.root, command=self.text.yview).pack(side='right')
        #self.text.configure(yscrollcommand=self.sb.set)

        ###

        self.root.config(menu=self.nmenu)
        self.root.mainloop()
        
    # allows user to name a file
    def miniFile(self):
        self.mini = tk.Tk()
        self.mini.geometry("300x100")
        self.mini.title('Add File')
        tk.Label(self.mini, text='Name the file').pack()
        self.text = tk.Entry(self.mini)
        self.text.pack()
        tk.Button(self.mini, text='Submit', command=self.handleMiniFile).pack()
        self.mini.mainloop()
    # allows user to name a folder
    def miniFolder(self):
        self.mini = tk.Tk()
        self.mini.geometry("300x100")
        self.mini.title('Add Folder')
        tk.Label(self.mini, text='Name the folder').pack()
        self.text = tk.Entry(self.mini)
        self.text.pack()
        tk.Button(self.mini, text='Submit', command=self.handleMiniFolder).pack()
        self.mini.mainloop()
    # handles submitting the button for a filename
    def handleMiniFile(self):
        new_text = self.text.get()
        self.mini.destroy()
        self.tree = create_file(self.path, new_text, self.tree)
        self.refresh()
    # handles submitting the button for a foldername
    def handleMiniFolder(self):
        new_text = self.text.get()
        self.mini.destroy()
        create_folder(self.path, new_text)
        self.refresh()

    def refresh(self):
        construct_graph(self.tree).write_png('bigTest.png')
        for i in inorder(self.tree):
            print(i, "\n")

gui()
