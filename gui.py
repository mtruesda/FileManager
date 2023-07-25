import os
import tkinter as tk
from tkinter import filedialog

def fill_listbox(path):
    listbox.delete(0, tk.END)
    for name in os.listdir(path):
        listbox.insert(tk.END, name)

def on_click(event):
    # If user double clicks on directory, open it
    index = listbox.curselection()
    #print(index)
    file = listbox.get(index)
    
    new_path = os.path.join(current_directory.get(), file)

    if os.path.isdir(new_path):
        current_directory.set(new_path)
        fill_listbox(new_path)
    else:
        print("File: ", new_path)

root = tk.Tk()

current_directory = tk.StringVar(root)

# User can select directory with this button
button = tk.Button(root, text="Select directory", command=lambda: current_directory.set(filedialog.askdirectory()))
button.pack()

listbox = tk.Listbox(root)
listbox.pack(fill="both", expand=True)

# Update listbox whenever directory changes
current_directory.trace_add("write", lambda *args: fill_listbox(current_directory.get()))

# Handle double click on listbox items
listbox.bind('<Double-1>', on_click)

root.mainloop()