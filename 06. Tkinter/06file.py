#Message:-
import tkinter as tk
root = tk.Tk()

# t = tk.Text(root, height=2, width=30)
# #t.pack()
# #Now if we use anchor = 'w' , the text will be displayed at start unlike in middle(Default)
# t.pack(anchor='w')
# t.insert(tk.END,"Hello Friends \n Are you ready for the Party \n")


#Spinbox
# w = tk.Spinbox(root, from_=0, to=42)
# #w.pack()
# w.pack(anchor='w')
# #w.grid(row =0, column=3)



#Scale:

# w = tk.Scale(root, from_=0, to = 42)
# w.pack()

# w = tk.Scale(root, from_=0, to=200, orient='horizontal')
# w.pack()


#LIstBox
# lb = tk.Listbox(root)
# lb.insert(1, 'Python')
# lb.insert(2, 'CPP')
# lb.pack()





#Scrollbar
s = tk.Scrollbar(root)
s.pack(side= 'right', fill = 'y')
mylist = tk.Listbox(root, yscrollcommand=s.set)

for line in range(100):
    mylist.insert(tk.END, "This is line no. " + str(line))

mylist.pack(side='left', fill="both")
#s.config(command = mylist.yview)

root.mainloop()