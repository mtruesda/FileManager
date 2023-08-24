import os
import tkinter as tk
from FileManagement import *
from pydot_graph_util import *
from TreeItems.SplayTree import *

def treeBuilder(path, tree):
    # starting from the outside
    for name in os.listdir(path):
        new_path = path + '/' + name
        if os.path.isdir(new_path):
            tree = treeBuilder(new_path, tree)
    # add the ends
    for name in os.listdir(path):
        new_path = path + '/' + name
        if not os.path.isdir(new_path):
            tree = insert1(tree, path + '/' + name)
    return tree

def fill_listbox(path):
    listbox.delete(0, tk.END)
    for name in os.listdir(path):
        listbox.insert1(tk.END, name)

def on_close():
    # file = open('TreeItems/TreeStorage.txt', 'w') 
    # file.write(dump_tree(tree)) 
    root.destroy()

def on_click(event, tree):
    # If user double clicks on directory, open it
    index = listbox.curselection()
    file = listbox.get(index)
    new_path = os.path.join(current_directory.get(), file)

    if os.path.isdir(new_path):
        current_directory.set(new_path)
        fill_listbox(new_path)
    else:
        open_file(new_path)
        tree = splay(tree, new_path)
        construct_graph(tree).write_png('Images/TreeBuilderTest.png')

def go_back():
    current_path = current_directory.get()
    parent_path = os.path.dirname(current_path)
    if parent_path != current_path:
        current_directory.set(parent_path)
        fill_listbox(parent_path)

def new_file():
    print("new file")

def new_directory():
    print("new directory")

root = tk.Tk()


# creating the current directory variable
current_directory = tk.StringVar(root)
initial_directory = home()  # Replace with your path

# determining the tree existance
file = open('TreeItems/TreeStorage.txt', 'r')
line = file.readline().strip()
tree = load_tree(line)
file.close()

if tree is None:
    tree = treeBuilder(initial_directory, None)
    construct_graph(tree).write_png('Images/TreeBuilderTest.png')

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(fill="x")

back_button = tk.Button(button_frame, text="Back", command=go_back)
back_button.pack(side="left")

new_file_button = tk.Button(button_frame, text="New File")
new_file_button.pack(side="left")

new_folder_button = tk.Button(button_frame, text="New Folder")
new_folder_button.pack(side="left")

# Left frame
left_frame = tk.Frame(root)
left_frame.pack(side="left", fill="y")

# Add documents button
documents_button = tk.Button(left_frame, text="Documents")#,command=lambda: open_folder(docs_path))
documents_button.pack(fill="x")

# Add downloads button
downloads_button = tk.Button(left_frame, text="Downloads")#, command=lambda: open_folder(downloads_path))
downloads_button.pack(fill="x")

recents_button = tk.Button(left_frame, text="Recents").pack(fill="x")

# building the listbox to list files
listbox = tk.Listbox(root)
listbox.pack(fill="both", expand=True)

# Set initial directory
current_directory.set(initial_directory)

# Fill listbox with initial directory contents
fill_listbox(initial_directory)

# Handle double click on listbox items
listbox.bind('<Double-1>', lambda event: on_click(event, tree))
# makes the window delete save the tree
root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()

