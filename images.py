from tkinter import *
from PIL import ImageTK, Image

root = Tk()
root.title('Images')
root.iconbitmap('@resources/pika.xbm')

myImg = ImageTk.PhotoImage(Image.open("resources/pika.jpeg"))


buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonQuit.pack()

root.mainloop()

