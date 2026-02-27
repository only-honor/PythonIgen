import tkinter as tk
root = tk.Tk()

root.title("My Tkinter App")
#label = tk.Label(root,text = "Hello Tkinter")
label = tk.Label(root)

#Grid() & Pack()
# Label is acting like label in html
# Entry us acting like input in html
l1 = tk.Label(root, text = "Name").grid(row = 0)
l2 = tk.Label(root, text = "Class").grid(row = 1)
e1 = tk.Entry(root).grid(row = 0, column = 1)
e2 = tk.Entry(root).grid(row = 1, column = 1)

label.grid()
root.mainloop()