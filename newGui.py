import tkinter as tk

def hello():
    print("Hello!")

def quit_app():
    root.quit()

root = tk.Tk()

# Create the main menu
menu_bar = tk.Menu(root)

# Create the "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit_app)

# Create the "Edit" menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

# Create the "Help" menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")

# Add the submenus to the main menu
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Attach the menu to the root window
root.config(menu=menu_bar)

root.mainloop()