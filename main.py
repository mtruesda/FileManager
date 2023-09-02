import os
import tkinter as tk
from FileManagement import *
from pydot_graph_util import *
from TreeItems.SplayTree import *

# Builds the tree from what exists in the directory
def treeBuilder(path, splayTree):
    # starting from the outside
    for name in os.listdir(path):
        new_path = os.path.join(path, name)
        if os.path.isdir(new_path):
            treeBuilder(new_path, splayTree)
        else:
            splayTree.insert(new_path)
    return splayTree

# V2
def fill_listbox(path, listbox):
    listbox.delete(0, tk.END)
    try:
        for name in os.listdir(path):
            listbox.insert(tk.END, name)
    except FileNotFoundError:
        print('Folder not found.')
    except PermissionError:
        print('Permission denied.')

# for saving the tree when the file manager is closed--UPDATE TO SAVE
# realizing that this may happen automatically as when the file manager is opened, it loads from existing files--making saving unnecessary
def on_close():
    # file = open('TreeItems/TreeStorage.txt', 'w') 
    # file.write(dump_tree(tree)) 
    root.destroy()

#V2
def on_click(event, tree, listbox, current_directory):
    index = listbox.curselection()
    file = listbox.get(index)
    new_path = os.path.join(current_directory.get(), file)
    if os.path.isdir(new_path):
        current_directory.set(new_path)
        fill_listbox(new_path, listbox)
    else:
        open_file(new_path)
        tree.search(new_path)
        construct_graph(tree.root).write_png('Images/ActiveUse/TreeBuilderTest.png')

def go_back(current_directory, listbox):
    current_path = current_directory.get()
    parent_path = os.path.dirname(current_path)
    if parent_path != current_path:
        current_directory.set(parent_path)
        fill_listbox(parent_path, listbox)

# adds a file to the directory =================================================================
def new_file(current_directory, splayTree, listbox):
    def create_new_file():
        filename = file_entry.get()
        file_path = os.path.join(current_directory.get(), filename)
        create_file(current_directory.get(), filename, splayTree)
        fill_listbox(current_directory.get(), listbox)
        # need to figure out why it's not inserting new files
        popup.destroy()
        
    popup = tk.Toplevel()
    popup.title("New File")
    
    file_label = tk.Label(popup, text="File Name:")
    file_label.pack(side="left")
    
    file_entry = tk.Entry(popup)
    file_entry.pack(side="left")
    
    create_button = tk.Button(popup, text="Create", command=create_new_file)
    create_button.pack(side="right")

def new_directory():
    print("new directory")

# ----------------------------------------------------------------

def delete_item(event, listbox, current_directory, splayTree):
    index = listbox.nearest(event.y)
    file = listbox.get(index)
    file_path = os.path.join(current_directory.get(), file)
    delete_path(file_path, splayTree)  # Your existing delete_path function
    fill_listbox(current_directory.get(), listbox)
    # need to delete from the splay tree -- hmmmm
    construct_graph(splayTree.root).write_png('Images/ActiveUse/TreeBuilderTest.png')

# place commands for effects in here on rightclicking the listbox items
def show_context_menu(event, listbox, current_directory, splayTree):
    context_menu = tk.Menu(root, tearoff=0)
    context_menu.add_command(label="Delete", command=lambda: delete_item(event, listbox, current_directory, splayTree))
    context_menu.post(event.x_root, event.y_root)

# ----------------------------------------------------------------


root = tk.Tk()

# creating the current directory variable
current_directory = tk.StringVar(root)
initial_directory = home()  # Replace with your path

# determining the tree existance
with open('TreeItems/TreeStorage.txt', 'r') as file:
    line = file.readline().strip()
tree = SplayTree(load_tree(line))

# checks that files that exist in the directory are added to the tree
if tree.root is None:
    tree = treeBuilder(initial_directory, tree)
    construct_graph(tree.root).write_png('Images/ActiveUse/TreeBuilderTest.png') # to show us the resulting tree

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(fill="x")

back_button = tk.Button(button_frame, text="Back", command=lambda: go_back(current_directory, listbox))
back_button.pack(side="left")

new_file_button = tk.Button(button_frame, text="New File", command=lambda: new_file(current_directory, tree, listbox))
new_file_button.pack(side="left")

new_folder_button = tk.Button(button_frame, text="New Folder", command=new_directory)
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
fill_listbox(initial_directory, listbox)

# Listbox item handling
listbox.bind('<Double-1>', lambda event: on_click(event, tree, listbox, current_directory))          # double click to open
listbox.bind("<Button-2>", lambda event: show_context_menu(event, listbox, current_directory, tree)) # rightclick menu

# makes the window delete save the tree
root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()

