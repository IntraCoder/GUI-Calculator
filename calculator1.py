from tkinter import *
from PIL import Image, ImageTk

# TODO -> Initialize Window
root = Tk()
root.geometry("600x520")
root.title("Intra Calculator")
root.resizable(width=False, height=False)
root.config(bg="grey20")

# TODO -> Setting up icon(not req)
icon = Image.open("calculator.png")
icon = ImageTk.PhotoImage(icon)
root.iconphoto(False, icon)


# TODO-> Function to insert operators
def operator(val):
    if input_var.get()[-1] not in ['+', "-", "/", "*"]:
        input_area.insert(END, val)


# TODO-> Funtion to insert number
def num(val):
    input_area.insert(END, val)


# TODO -> Function to get result
def equals():
    try:
        if input_var.get()=="0/0":
            result="Infinity"
        elif input_var.get()[1] in [:
            reult="0"
        elif input_var.get()[0] == "0" and input_var.get()[1] not in ["/","+","-","*"]:
            result = eval(input_var.get()[1:])
        else:
            result = eval(input_var.get())
        input_area.delete(0, END)
        input_area.insert(0, result)
    except:
        pass


# TODO -> Function to clear last input
def clear():
    inp = input_var.get()
    input_area.delete(0, END)
    input_area.insert(0, inp[:-1])


# TODO -> Function to clear complete input
def clearfull():
    input_area.delete(0, END)


# TODO-> Initialize Entry area
input_var = StringVar()
input_area = Entry(root, textvariable=input_var, font="None 20", width=40)
input_area.insert(0, "0")

# TODO -> Initialize Operator Buttons
plus = Button(root, text="+", bg="black", fg="white", font="None 17", command=lambda: operator("+"), width=10, height=3)
minus = Button(root, text="-", bg="black", fg="white", font="None 17", command=lambda: operator("-"), width=10,
               height=3)
multiply = Button(root, text="*", bg="black", fg="white", font="None 17", command=lambda: operator("*"), width=10,
                  height=3)
sash = Button(root, text="/", bg="black", fg="white", font="None 17", command=lambda: operator("/"), width=10, height=3)
equal = Button(root, text="=", bg="black", fg="white", font="None 17", command=equals, width=40, height=3)

# TODO-> Initialize Number Buttons
one = Button(root, text="1", bg="black", fg="white", font="None 17", command=lambda: num("1"), width=10, height=3)
two = Button(root, text="2", bg="black", fg="white", font="None 17", command=lambda: num("2"), width=10, height=3)
three = Button(root, text="3", bg="black", fg="white", font="None 17", command=lambda: num("3"), width=10, height=3)
four = Button(root, text="4", bg="black", fg="white", font="None 17", command=lambda: num("4"), width=10, height=3)
five = Button(root, text="5", bg="black", fg="white", font="None 17", command=lambda: num("5"), width=10, height=3)
six = Button(root, text="6", bg="black", fg="white", font="None 17", command=lambda: num("6"), width=10, height=3)
seven = Button(root, text="7", bg="black", fg="white", font="None 17", command=lambda: num("7"), width=10, height=3)
eight = Button(root, text="8", bg="black", fg="white", font="None 17", command=lambda: num("8"), width=10, height=3)
nine = Button(root, text="9", bg="black", fg="white", font="None 17", command=lambda: num("9"), width=10, height=3)
zero = Button(root, text="0", bg="black", fg="white", font="None 17", command=lambda: num("0"), width=10, height=3)

clean = Button(root, text="C", bg="black", fg="white", font="None 17", command=clear, width=10, height=3)
cleanfull = Button(root, text="CE", bg="black", fg="white", font="None 17", command=clearfull, width=10, height=3)

input_area.grid(row=0, columnspan=4)

# TODO -> Griding Operator Buttons
plus.grid(row=1, column=3)
minus.grid(row=2, column=3)
multiply.grid(row=3, column=3)
sash.grid(row=4, column=3)

# TODO-> griding Number buttons
one.grid(row=1, column=0)
two.grid(row=1, column=1)
three.grid(row=1, column=2)
four.grid(row=2, column=0)
five.grid(row=2, column=1)
six.grid(row=2, column=2)
seven.grid(row=3, column=0)
eight.grid(row=3, column=1)
nine.grid(row=3, column=2)
zero.grid(row=4, column=0)

# TODO-> Equal and clear buttons
equal.grid(row=5, columnspan=4)
clean.grid(row=4, column=2)
cleanfull.grid(row=4, column=1)

root.mainloop()
