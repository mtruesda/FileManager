import os
import tkinter as tk
from Utility.FileManagement import *

def fill_listbox(path):
    listbox.delete(0, tk.END)
    for name in os.listdir(path):
        listbox.insert(tk.END, name)

def on_click(event):
    # If user double clicks on directory, open it
    index = listbox.curselection()
    file = listbox.get(index)
    new_path = os.path.join(current_directory.get(), file)

    if os.path.isdir(new_path):
        current_directory.set(new_path)
        fill_listbox(new_path)
    else:
        open_file(new_path)

root = tk.Tk()

# creating the current directory variable
current_directory = tk.StringVar(root)

# determining the tree existance
file = open('TreeStorage.txt', 'r')

# building the listbox to list files
listbox = tk.Listbox(root)
listbox.pack(fill="both", expand=True)

# Set initial directory
initial_directory = home()  # Replace with your path
current_directory.set(initial_directory)

# Fill listbox with initial directory contents
fill_listbox(initial_directory)

# Handle double click on listbox items
listbox.bind('<Double-1>', on_click)

root.mainloop()