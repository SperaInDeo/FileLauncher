import os
from tkinter import *
from PIL import Image,ImageTk

#def my_command():
    #os.startfile(r"TestText.txt")
num_rows = 5
num_columns = 5
bg_color = '#f0f0f0'
image_file = 'Untitled.gif'

def input_button_click():
    entry_text = inputBox.get().replace('\\','\\\\')
    def execute_file():
        os.startfile(entry_text)
    # buttLabel1 = Label(root, text='button clicked', bg=bg_color)
    # buttLabel1.grid(row=2, column=2)
    global file_image
    file_image = ImageTk.PhotoImage(Image.open('TexasStar.ico'))
    outputButton = Button(root, text=entry_text, image=file_image,compound=TOP, state=NORMAL, command=execute_file, bd=1, bg=bg_color)
    outputButton.grid(row=3, column=0)
    return image_file

root = Tk()
root.title('File Launcher')
root.iconbitmap('TexasStar.ico')
root.geometry('800x600')
root.configure(bg=bg_color)

file_image = ImageTk.PhotoImage(Image.open(image_file))

bannerLabel = Label(root, text='Hello world', bg=bg_color)
inputBox = Entry(root, text='input filepath here', bg=bg_color, borderwidth=5)
#inputBox.bind('<Return>', input_button_click)
inputButton = Button(root, text='Update File', state=NORMAL, padx=25, pady=25, command=input_button_click, bg=bg_color)

bannerLabel.grid(row=0, column=(num_columns+1)//2)
inputBox.grid(row=1, column=1)
inputButton.grid(row=1, column=0)


root.mainloop()