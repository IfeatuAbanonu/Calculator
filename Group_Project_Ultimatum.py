
# Create a calculator that can solve multiple simple arithmetic operations as well  as quadratic equations


# Tkinter is a GUI package that we use to build out an interface such as buttons, menus, labels, entry fields etc...
from tkinter import *
import tkinter as tk



# Create an instance of tkinter window
calculator_screen = Tk()
calculator_screen.title("Calculator Group Project")
calculator_screen.geometry("550x400")
equation_text = ""

# StringVar() is used to hold string data where we can set text value and retrieve it.
# The widget will get updated with whatever new value imputed whenever the value of the stringVar() gets updated
equation_label = StringVar()


operation_screen = Label(calculator_screen, textvariable=equation_label, font=30, bg="dark grey", width=50, height=4)
operation_screen.pack()


box = Frame(calculator_screen)
box.pack()


def buttons(symbols):

    # Global keyword is used to access the variable outside the function
    global equation_text
    equation_text += str(symbols)
    equation_label.set(equation_text)


def equals_to():

    global equation_text

    try:
        operation = str(eval(equation_text))
        equation_label.set(operation)
        equation_text = operation

    except SyntaxError:
        equation_label.set("Syntax Error")
        # equation_text = " "

    except ZeroDivisionError:
        equation_label.set("Arithmetic Error")
        # equation_text = " "

def clear():

    global equation_text
    equation_label.set("")
    equation_text = ""

def quadratic_formula(root, a, b, c):

    a = int(a.get())
    b = int(b.get())
    c = int(c.get())

    x = -b
    y = ((b ** 2) - (4 * a * c)) ** 0.5
    z = 2 * a

    f = (x + y) / z
    g = (x - y) / z

    formular1 = f
    formular2 = g


    # Label widget is a widget used to implement display boxes where you can place text or images
    Label(root, text=f"X= {formular1}  OR  X= {formular2}", font="consolas 12").place(x=145, y=182)

    # ImageTk.PhotoImage(Image.open("Image"))

def open_quad_window():
    root = tk.Toplevel()
    root.title("Almighty_Formula_Screen")
    root.geometry("500x350")

    a_val = Label(root, text="Enter a value for a: ", font="consolas 12")
    b_val = Label(root, text="Enter a value for b: ", font="consolas 12")
    c_val = Label(root, text="Enter a value for c: ", font="consolas 12")
    #

    a_val.place(x=50, y=20)
    b_val.place(x=50, y=70)
    c_val.place(x=50, y=120)

    answer = Label(root, text="answer =", font="consolas 14")
    answer.place(x=50, y=180)

    a_value = StringVar()
    b_value = StringVar()
    c_value = StringVar()



    # The entry widget is used to accept or display a single line of text from a user
    a_entry = Entry(root, textvariable=a_value, font="arial 20", width=10)
    a_entry.place(x=250, y=20)
    b_entry = Entry(root, textvariable=b_value, font="arial 20", width=10)
    b_entry.place(x=250, y=70)
    c_entry = Entry(root, textvariable=c_value, font="arial 20", width=10)
    c_entry.place(x=250, y=120)

    Button(root, text="Calculate", font="arial 17", command=lambda: quadratic_formula(root, a_entry,b_entry,c_entry)).place(x=200, y=230)
    Button(root, text="Exit", command=lambda: exit(), font="arial 17", width=5).place(x=400, y=290)



key1 = Button(box, height=3, width=8, text=1, font=40, command=lambda: buttons(1))
key1.grid(row=0, column=0)

key2 = Button(box, height=3, width=8, text=2, font=40, command=lambda: buttons(2))
key2.grid(row=0, column=1)

key3 = Button(box, height=3, width=8, text=3, font=40, command=lambda: buttons(3))
key3.grid(row=0, column=2)

key4 = Button(box, height=3, width=8, text=4, font=40, command=lambda: buttons(4))
key4.grid(row=1, column=0)

key5 = Button(box, height=3, width=8, text=5, font=40, command=lambda: buttons(5))
key5.grid(row=1, column=1)

key6 = Button(box, height=3, width=8, text=6, font=40, command=lambda: buttons(6))
key6.grid(row=1, column=2)

key7 = Button(box, height=3, width=8, text=7, font=40, command=lambda: buttons(7))
key7.grid(row=2, column=0)

key8 = Button(box, height=3, width=8, text=8, font=40, command=lambda: buttons(8))
key8.grid(row=2, column=1)

key9 = Button(box, height=3, width=8, text=9, font=40, command=lambda: buttons(9))
key9.grid(row=2, column=2)

key0 = Button(box, height=3, width=8, text=0, font=40, command=lambda: buttons(0))
key0.grid(row=3, column=1)

decimal_key = Button(box, height=3, width=8, font=40, text=".", command=lambda: buttons("."))
decimal_key.grid(row=3, column=2)

equals_key = Button(box, height=3, width=8, text="=", font=40, command=equals_to)
equals_key.grid(row=3, column=4)

division_key = Button(box, height=3, width=8, text="/", font=40, command=lambda: buttons("/"))
division_key.grid(row=0, column=3)

floor_division_key = Button(box, height=3, width=8, text="//", font=40, command=lambda: buttons("//"))
floor_division_key.grid(row=0, column=4)

clear = Button(box, height=3, width=8, text="A/C", font=40,fg='dark red', command=clear)
clear.grid(row=3, column=0)

multiplication_key = Button(box, height=3, width=8, text="x", font=40, command=lambda: buttons("*"))
multiplication_key.grid(row=1, column=3)

sqrt = Button(box, height=3, width=8, text="sqrt", font=40, command=lambda: buttons(" ** 0.5"))
sqrt.grid(row=1, column=5)

minus_key = Button(box, height=3, width=8, text="-", font=40, command=lambda: buttons("-"))
minus_key.grid(row=2, column=3)

addition_key = Button(box, height=3, width=8, text="+", font=40, command=lambda: buttons("+"))
addition_key.grid(row=3, column=3)

parenthesis_key = Button(box, height=3, width=8, text="(", font=40, command=lambda: buttons("("))
parenthesis_key.grid(row=1, column=4)

parenthesis_key = Button(box, height=3, width=8, text=")", font=40, command=lambda: buttons(")"))
parenthesis_key.grid(row=2, column=4)

square_key = Button(box, height=3, width=8, text="exp", font=40, command=lambda: buttons("**"))
square_key.grid(row=0, column=5)

quadratic_formula_key = Button(box, height=3, width=8, fg="dark red", text="QUAD \n EQUA", font=40, command=open_quad_window)
quadratic_formula_key.grid(row=3, column=5)

MOD_key = Button(box, height=3, width=8, text="mod", font=40, command=lambda: buttons("%"))
MOD_key.grid(row=2, column=5)






calculator_screen.mainloop()