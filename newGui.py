import tkinter as tk

def retrieve_text():
    value = text_widget.get("1.0", "end-1c")
    print("Value in Text widget:", value)

root = tk.Tk()

# Create a Text widget
text_widget = tk.Text(root)
text_widget.pack()

# Create a Button
button = tk.Button(root, text="Retrieve", command=retrieve_text)
button.pack()

root.mainloop()