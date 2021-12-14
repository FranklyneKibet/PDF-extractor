from tkinter import *
import PyPDF2
from PIL import Image,ImageTk


root = Tk()

canvas = Canvas(root, width = 600, height = 300)
canvas.grid(columnspan=3)

#Logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image = logo)
logo_label.image = logo


root.mainloop()