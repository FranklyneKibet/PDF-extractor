from os import read
from tkinter import *
from tkinter.filedialog import askopenfile
import PyPDF2
from PIL import Image,ImageTk


root = Tk()
root.title("PDF Extractor")

canvas = Canvas(root, width = 600, height = 300)
canvas.grid(columnspan=3, rowspan=3,)

#Logo
logo = PhotoImage(file = "./logo.png")
label = Label(root, image=logo)
label.grid(column=1,row=0)

#Instructions
instructions = Label(root, text="Select a PDF file on your computer to extract all its text." , font = "Raleway")
instructions.grid(columnspan=3, column=0,row=1)

def open_file():
    browse_text.set("Loading.....")
    file = askopenfile(parent = root, mode="rb", filetype=[("Pdf file", "*.pdf")])
    if file is not None: 
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        
        #text box
        text_box =  Text(root, width=50, height=10, pady=15,padx=15)
        text_box.insert(1.0,page_content)
        text_box.tag_configure("center",justify="center")
        text_box.tag_add("center",1.0,"end")
        text_box.grid(column=1,row=3)
        
        browse_text.set("Browse")

#Browse Button
browse_text = StringVar()
browse_btn = Button(root, textvariable = browse_text, command = lambda:open_file(),  font = "Raleway", bg = "#20bebe", fg="white", width=15, height=2)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = Canvas(root, width=600, height = 300)
canvas.grid(columnspan=3)

root.mainloop()