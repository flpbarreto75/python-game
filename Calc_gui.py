from tkinter import *
import keyboard
import string
from threading import *

root = Tk()
root.geometry("300x360")

# Define the entry for the calculator
v = StringVar()
e1 = Entry(root, bg="light blue", font="Ariel 30",textvariable=v)
e1.place(height=60, width=300)

# Define the reset button
def erase():
    e1.delete(first=0, last="end")
    e1.place(height=60, width=300)


# Define the functions for the calculator
def dev():
    e1.insert(END,"/")

def times():
    e1.insert(END, "*")

def minus():
    e1.insert(END,"-")

def plus():
    e1.insert(END,"+")

def dot():
    e1.insert(END,".")


# Defines the Enter key and evaluation
def equals():
    result = eval(e1.get())
    erase()
    e1.insert(END,result)





# Defining the number bindings
def b1():
    e1.insert(END,"1")

def b2():
    e1.insert(END,"2")

def b3():
    e1.insert(END,"3")

def b4():
    e1.insert(END,"4")

def b5():
    e1.insert(END,"5")

def b6():
    e1.insert(END,"6")

def b7():
    e1.insert(END,"7")

def b8():
    e1.insert(END,"8")

def b9():
    e1.insert(END,"9")

def b0():
    e1.insert(END,"0")

# Define the action Buttons and its places
C = Button(root, text="C",  command=erase).place(height=60, width=80, x=0, y=60,)
dev = Button(root, text="/", command=dev).place(height=60, width=80, x=160, y=60)
times = Button(root, text="*", command=times).place(height=60, width=80, x=80, y=60)
minus = Button(root, text="-", command=minus).place(height=60, width=60, x=240, y=60)
plus = Button(root, text="+", command=plus).place(height=120, width=60, x=240, y=120)
equals = Button(root, text="=", command=equals).place(height=120, width=60, x=240, y=240)
dot = Button(root, text=".", command=dot).place(height=60, width=80, x=160, y=300)

# Defining the number buttons and its places
b1 = Button(root, text="1", command=b1).place(height=60, width=80, x=0, y=120)
b2 = Button(root, text="2", command=b2).place(height=60, width=80, x=80, y=120)
b3 = Button(root, text="3", command=b3).place(height=60, width=80, x=160, y=120)
b4 = Button(root, text="4", command=b4).place(height=60, width=80, x=0, y=180)
b5 = Button(root, text="5", command=b5).place(height=60, width=80, x=80, y=180)
b6 = Button(root, text="6", command=b6).place(height=60, width=80, x=160, y=180)
b7 = Button(root, text="7", command=b7).place(height=60, width=80, x=0, y=240)
b8 = Button(root, text="8", command=b8).place(height=60, width=80, x=80, y=240)
b9 = Button(root, text="9", command=b9).place(height=60, width=80, x=160, y=240)
b0 = Button(root, text="0", command=b0).place(height=60, width=160, x=0, y=300)

root.mainloop()