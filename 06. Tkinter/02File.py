import tkinter as tk
root = tk.Tk()

C = tk.Canvas(root, bg = 'yellow', height = 250, width = 300)
l = C.create_line(108, 120, 320, 40, fill='green')
a = C.create_arc(180,150,80,210,start=0,extent = 220, fill = 'red')
o = C.create_oval(80,30,140,150,fill = 'blue')


C.pack()
root.mainloop()