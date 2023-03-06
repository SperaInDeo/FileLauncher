import os
from tkinter import *
from PIL import Image,ImageTk

num_rows = 1
num_columns = 1
bg_color = '#f0f0f0'
image_file = 'TexasStar.ico'
file_path = None

def entry_return(event):
    outputButtonInitial.destroy()
    entry_text = inputBox.get().replace('\\','\\\\').replace('\"', '')
    with open('FileLauncher_file_list.csv', 'w', encoding='UTF-8') as update_file_doc:
        update_file_doc.write(entry_text) 
    def execute_file():
        try:
            os.startfile(entry_text)
        except:
            print('file not found')
    global file_image
    file_image = ImageTk.PhotoImage(Image.open('TexasStar.ico'))
    outputButton = Button(root, text=entry_text, image=file_image,compound=TOP, state=NORMAL, command=execute_file, bd=1, bg=bg_color)
    outputButton.grid(row=3, column=0)

def input_add_button():
    inputBox.grid(row=1, column=1)

def execute_file_initial():
    try:
        os.startfile(file_path)
    except:
        print('file not found')

root = Tk()
root.title('File Launcher')
root.iconbitmap('TexasStar.ico')
root.geometry('400x400')
root.configure(bg=bg_color)

file_image = ImageTk.PhotoImage(Image.open(image_file))
try:
    with open('FileLauncher_file_list.csv', 'r', encoding='UTF-8') as read_file_doc:
        file_path = read_file_doc.read()
except:
    print('There is currently no list file. Update the program to create file to launch program.')

if file_path != None:
        outputButtonInitial = Button(root, text=file_path, image=file_image, compound=TOP, state=NORMAL, command=execute_file_initial, bd=1, bg=bg_color)
        outputButtonInitial.grid(row=3, column=0)

bannerLabel = Label(root, text='Welcome to the File Launcher', bg=bg_color)
inputBox = Entry(root, text='input filepath here', bg=bg_color, borderwidth=5)
inputBox.bind('<Return>', entry_return)
inputButton = Button(root, text='Update File', state=NORMAL, padx=5, pady=5, command=input_add_button, bg=bg_color)

bannerLabel.grid(row=0, column=num_columns//2)
inputButton.grid(row=1, column=0)

root.mainloop()