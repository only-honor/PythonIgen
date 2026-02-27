# Label and list in tkinter
import tkinter as tk
root = tk.Tk()

# W = tk.Label(root, text = 'courses')
W = tk.Label(root, text = 'courses', bg = 'grey', fg = 'brown')
W.pack()

# lb = tk.Listbox(root)
# lb.insert(1, 'Python')
# lb.insert(2, 'CPP')
# lb.insert(3, "JAVA")

lb = tk.Listbox(root, bg = 'green', fg = 'white') #bg & fg attributes are available in Listbox() but not in insert()
lb.insert(1, 'Python')
lb.insert(2, 'CPP')
lb.insert(3, "JAVA")

lb.pack()
root.mainloop()