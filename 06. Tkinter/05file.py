import tkinter as tk
root = tk.Tk()

# label = tk.Label(root,text="hobbies")

# var1 = tk.IntVar()
# c = tk.Checkbutton(root, text = "Reading", variable = var1).grid(row = 0)

# var2 = tk.IntVar()
# c = tk.Checkbutton(root, text = "Cooking", variable = var2).grid(row = 1)

# var3 = tk.IntVar()
# c = tk.Checkbutton(root, text = "Coding", variable = var3).grid(row = 3)






#RADIO BUTTON
#Using Grid()

#label = tk.Label(root,text="State")


# var1 = tk.IntVar()
# c = tk.Radiobutton(root, text = "Punjab", variable = var1, value=1).grid(row = 0)


# c = tk.Radiobutton(root, text = "Haryana", variable = var1, value=2).grid(row = 1)


# c = tk.Radiobutton(root, text = "Karnataka", variable = var1, value=3).grid(row = 2)



#USING PACK()
var1 = tk.IntVar()
c = tk.Radiobutton(root, text = "Punjab", variable = var1, value=1).pack(anchor = 'w')
c = tk.Radiobutton(root, text = "Haryana", variable = var1, value=2).pack(anchor = 'w')
c = tk.Radiobutton(root, text = "Karnataka", variable = var1, value=3).pack(anchor = 'w')

root.mainloop()