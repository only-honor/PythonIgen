from tkinter import Tk, Menu
root = Tk()

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = 'New')
filemenu.add_command(label = 'Open')
filemenu.add_command(label = 'Save As')
filemenu.add_command(label = 'Save')
filemenu.add_separator()
filemenu.add_command(label = 'Preferences')
filemenu.add_command(label = 'Auto Save')
filemenu.add_separator()
filemenu.add_command(label = 'Close Folder')
filemenu.add_command(label = 'Close Window')
filemenu.add_separator()
filemenu.add_command(label = 'Exit', command = root.quit)


editmenu = Menu(menu)
menu.add_cascade(label = 'Edit', menu = editmenu)
editmenu.add_command(label = 'Undo')
editmenu.add_command(label = 'Redo')
editmenu.add_command(label = 'Copy')
editmenu.add_command(label = 'Paste')
editmenu.add_separator()
editmenu.add_command(label = 'Cut')
editmenu.add_command(label = 'Find in File')
editmenu.add_separator()
editmenu.add_command(label = 'Replace')
editmenu.add_command(label = 'Toggle')
editmenu.add_separator()
editmenu.add_command(label = 'Exit', command = root.quit)



root.mainloop()