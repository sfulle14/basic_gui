import matplotlib
import numpy as np
import math
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *

root = Tk()

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
    files = [('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('C++ Files', '*.cpp'),
             ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)

#function to go fullscreen
def fullscreen():
    root.attributes('-fullscreen',True)

#funciton to return to normal screen
def max_screen():
    root.attributes('-fullscreen',False)

def small_screen():
    root.geometry('200x200')