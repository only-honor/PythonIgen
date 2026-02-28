from tkinter import *
from tkinter import messagebox
tasks_list = []
counter = 1

def inpurError():
    if enterTaskField.get() == "":
        messagebox.showerror("Input Error", "Please enter a task")
        return 0
    return 1

def clear_taskEntry():
    enterTaskField.delete(0, END)

def add_task():
    global counter
    value = inpurError()
    if value == 0:
        return
    content = enterTaskField.get() + "\n"

    tasks_list.append(content)

    