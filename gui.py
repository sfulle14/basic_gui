import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *

#function used to create new windows
def create_window():
    win = Toplevel(root)

#function used to open files
def open_file():
    file = askopenfile(mode ='r')
    if file is not None:
        content = file.read()

#function to save files
def save_file():
    name=asksaveasfile(mode='w')

root = Tk()
root.title("GUI")
#scrollbar = Scrollbar(root)
#scrollbar.pack(side = "right", fill="y")

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
viewmenu = Menu(menubar, tearoff=0)
importmenu = Menu(menubar, tearoff=0)
editmenu = Menu(menubar, tearoff=0)

#File menu
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=create_window)
filemenu.add_command(label="Save", command=None)
filemenu.add_command(label="Save as...", command=None)
filemenu.add_command(label="Exit", command=root.destroy)

#Edit menu
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Copy", command=None)
editmenu.add_command(label="Paste", command=None)
editmenu.add_command(label="Cut", command=None)
editmenu.add_command(label="Undo", command=None)

#View menu
menubar.add_cascade(label="view", menu=viewmenu)
viewmenu.add_command(label="Zoom in", command=root.state('zoomed'))
viewmenu.add_command(label="Zoom out", command=None)
viewmenu.add_command(label="Fullscreen", command=None)

#Import menu
menubar.add_cascade(label="Import", menu=importmenu)
importmenu.add_command(label="File", command=None)

root.mainloop()
