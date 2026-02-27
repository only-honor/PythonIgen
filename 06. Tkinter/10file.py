import tkinter as tk
from tkinter import messagebox
ws = tk.Tk()

ws.title("Python")
ws.geometry("200x200")

def viewselected():
    choice = var.get()
    if choice == 1:
        output = "science"
    elif choice == 2:
        output = "maths"
    elif choice == 3:
        output = "english"
    else:
        messagebox.showinfo('Python', "Invalid choice")
    return messagebox.showinfo('Pyth', "You Selected: " + output) #Here we can pass only 2 args, one is titile and 2nd is output

var = tk.IntVar()
tk.Radiobutton(ws, text = "Science", variable = var, value = 1, command = viewselected).pack()
tk.Radiobutton(ws, text = "Maths", variable = var, value = 2, command = viewselected).pack()
tk.Radiobutton(ws, text = "English", variable = var, value = 3, command = viewselected).pack()
ws.mainloop()