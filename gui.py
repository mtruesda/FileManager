#import tkinter as tk
from tkinter import *
from FileManagement import *

# class gui():
#     def __init__(self):
#         print("gui initialization")
#         window = tk.Tk()
#         window.mainloop

# gui()

class gui():
    def __init__(self):
        # tree
        tree = None

        # initialize
        print("gui initialization")
        window = Tk()
        window.geometry('800x500')
        
        # mentu
        m = Menu(window)
        m.add_command(label = 'forward', command=forward(''))
        m.add_command(label = 'back', command=back(''))
        m.add_command(label = 'Add File', command=create_file(''))
        m.add_command(label = 'Add Folder', command=create_folder(''))
        m.add_command(label = 'Delete', command=delete_path(''))

        window.config(menu=m)

        # Frames
        outer = Frame(window, bg = 'blue').pack()
        left = Frame(outer, width = 200).pack(side = 'left')
        right = Frame(outer, width = 600).pack(side = 'right')
        topRight = Frame(right).pack(side = 'top')
        topLeft = Frame(left).pack(side = 'top')
        bottomRight = Frame(right).pack(side = 'bottom')
        bottomLeft = Frame(left).pack(side = 'bottom')
        
        # Labels
        #nameLabel = Label(topLeft, text="File Manager").place(x = 5, y = 5)
        #secondLabel = Label(topRight, text = "Second label").place(x = 105, y = 5)

        

        #label3 = Label(topLeft, text ='test 2').pack()
        
        # Buttons
        #addFile = Button(topRight, text='New File').grid(column = 0, row = 0)
        #addFolder = Button(topRight, text='Folder').grid(column = 1, row = 0)

        # Pane
        pane = PanedWindow(bottomRight).pack()
        locationsPane = PanedWindow(bottomLeft).pack()

        # looping
        window.mainloop()

gui()