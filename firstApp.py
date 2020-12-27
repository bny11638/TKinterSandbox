from tkinter import *

root = Tk()

#Creating a Label Widget
myLabel = Label(root, text="Hello World")
#Pushing it into the screen
myLabel.pack() #Packs it in as big as the widgets are -- why the window starts small

#Starting main loop for root
root.mainloop()
