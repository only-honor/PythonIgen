import tkinter as tk
root = tk.Tk() #Tkinter toolkit


button = tk.Menubutton(root, text = "Courses")
button.grid()

button.menu = tk.Menu(button, tearoff=0)
button["menu"] = button.menu

var1 = tk.IntVar()
var2 = tk.IntVar()

button.menu.add_checkbutton(label="BCA", variable=var1)
button.menu.add_checkbutton(label="BTech", variable=var2)

button.pack()
root.mainloop()