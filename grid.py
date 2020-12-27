from tkinter import *

root = Tk()

#Creating a Label Widget
myLabel = Label(root, text="Hello World")
label2 = Label(root, text="My Name is Brandon Yau")
label3 = Label(root, text="             ")


#Grid it into the screen
myLabel.grid(row=1,column=0)
label2.grid(row=1,column=2)
label3.grid(row=1,column=1)

Label(root, text="fancy boi").grid(row=2, column=1)

#Starting main loop for root
root.mainloop()
