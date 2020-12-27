from tkinter import Entry,Button, Tk, Label
root = Tk()

e = Entry(root, width=50, bg="white",borderwidth=5) #retrieve with e.get()
e.pack()
e.insert(0, "Enter Your Name: ") # little webform

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.pack()

root.mainloop()

