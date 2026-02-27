import tkinter as tk
import customtkinter as ctk
import tkinter.messagebox as tkmb
#root = tk.Tk()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
 #Custom tkinter toolkit

app.title("Login Form")

def login():
    username = "Rahul"
    password = '12345'

    n = ctk.CTkToplevel(app)
    n.title("Main Window")

    if userentry.get() == username and userpass.get() == password:
        tkmb.showinfo(title = "Login Successful", message = "You have logged in")
    elif userentry.get() != username and userpass.get() == password:
        tkmb.showinfo(title = "Wrong USername", messsage = 'Check Your Username')
    elif userentry.get() == username and userpass.get() != password:
        tkmb.showinfo(title = "wrong password", message = "Enter correct password")
    else:
        tkmb.showerror(title = "Login failed", message="Invalid Username & Password")
    

l1 = ctk.CTkLabel(app, text = "Login Window")
l1.pack(pady = 20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady = 20, padx = 40, fill = "both", expand = True)

userentry = ctk.CTkEntry(frame, placeholder_text = "Username")
userentry.pack(pady = 12, padx = 10)
userpass = ctk.CTkEntry(frame, placeholder_text = "Password")
userpass.pack(pady = 12, padx = 10)

btn = ctk.CTkButton(frame, text = "Login", command = login)
btn.pack(pady = 12, padx = 10)





app.mainloop()