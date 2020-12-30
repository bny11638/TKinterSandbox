from tkinter import *

numbers = []

def buttonClick(number):
    #e.delete(0, END)
    e.insert(END, number)

def buttonClear():
    e.delete(0,END)

def buttonAdd():
    numbers.append(e.get())
    e.delete(0,END)
    print(numbers)

def buttonEqual():
    numbers.append(e.get())
    e.delete(0,END)
    sum = 0
    for x in numbers:
        if x is not None:
            sum += int(x)
    e.insert(0,sum)
    numbers.clear()
    print(numbers)

root = Tk()
root.title("Simple Calculator")
e = Entry(root, width = 35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3,padx=10, pady=10)

but1 = Button(root, text="1", padx=40, pady=20, command=lambda:buttonClick(1))
but2 = Button(root, text="2", padx=40, pady=20, command=lambda:buttonClick(2))
but3 = Button(root, text="3", padx=40, pady=20, command=lambda:buttonClick(3))
but4 = Button(root, text="4", padx=40, pady=20, command=lambda:buttonClick(4))
but5 = Button(root, text="5", padx=40, pady=20, command=lambda:buttonClick(5))
but6 = Button(root, text="6", padx=40, pady=20, command=lambda:buttonClick(6))
but7 = Button(root, text="7", padx=40, pady=20, command=lambda:buttonClick(7))
but8 = Button(root, text="8", padx=40, pady=20, command=lambda:buttonClick(8))
but9 = Button(root, text="9", padx=40, pady=20, command=lambda:buttonClick(9))
but0 = Button(root, text="0", padx=40, pady=20, command=lambda:buttonClick(0))
butAdd = Button(root, text="+", padx=38, pady=20, command=buttonAdd)
butEq = Button(root, text="=", padx=35, pady=20, command=buttonEqual)
butClear = Button(root, text="Clear", padx=120, pady=20, command=buttonClear)


#putting buttons on screen
but1.grid(row=3,column=0)
but2.grid(row=3,column=1)
but3.grid(row=3,column=2)

but4.grid(row=2,column=0)
but5.grid(row=2,column=1)
but6.grid(row=2,column=2)

but7.grid(row=1,column=0)
but8.grid(row=1,column=1)
but9.grid(row=1,column=2)

but0.grid(row=4,column=1)

butAdd.grid(row=4,column=0)
butEq.grid(row=4,column=2, columnspan=1)
butClear.grid(row=5, column=0, columnspan=3)

root.mainloop()