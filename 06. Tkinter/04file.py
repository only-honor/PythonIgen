# Message in tkinter

import tkinter as tk
root = tk.Tk()

M = "Hello Friends"
#message = tk.Message(root, text = M)

message = tk.Message(root, text = M)
message.config(bg = 'light green', fg = 'brown',width=300)
message.pack()
root.mainloop()









#Config is updating the message or its like adding CSS/Designs to the message