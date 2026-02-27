import tkinter as tk
root = tk.Tk()
expression = ""

root.configure(background='skyblue')
root.title("Calc")
root.geometry("270x150")
equation = tk.StringVar()
expression_field = tk.Entry(root, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)


def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":


    button1 = tk.Button(root, text='1', command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)
    button2 = tk.Button(root, text='2', command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)
    button3 = tk.Button(root, text='3', command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)
    button4 = tk.Button(root, text='4', command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)
    button5 = tk.Button(root, text='5', command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)
    button6 = tk.Button(root, text='6', command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)
    button7 = tk.Button(root, text='7', command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)
    button8 = tk.Button(root, text='8', command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)
    button9 = tk.Button(root, text='9', command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)


    button0 = tk.Button(root, text='0', command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)
    button_clear = tk.Button(root, text='C', command=clear, height=1, width=7)
    button_clear.grid(row=5, column=1)
    button_equal = tk.Button(root, text='=', command=equalpress, height=1, width=7)
    button_equal.grid(row=5, column=2)


    button_add = tk.Button(root, text='+', command=lambda: press('+'), height=1, width=7)
    button_add.grid(row=2, column=3)
    button_sub = tk.Button(root, text='-', command=lambda: press('-'), height=1, width=7)
    button_sub.grid(row=3, column=3)
    button_mul = tk.Button(root, text='*', command=lambda: press('*'), height=1, width=7)
    button_mul.grid(row=4, column=3)
    button_div = tk.Button(root, text='/', command=lambda: press('/'), height=1, width=7)
    button_div.grid(row=5, column=3)



    
    

    

#temperature Converter 



root.mainloop()