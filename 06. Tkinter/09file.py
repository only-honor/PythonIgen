import tkinter as tk
root = tk.Tk() #Tkinter toolkit

def show():
    label.Config(text = clicked.get())
options = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

clicked = tk.StringVar()
clicked.set('Monday')
drop = tk.OptionMenu(root, clicked, *options)
drop.pack()

#button = tk.Button(root, text = 'Click Me', command = show)
label = tk.Label(root, text = '')
label.pack()
root.mainloop()