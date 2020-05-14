from functions import *

root.title("GUI")

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
viewmenu = Menu(menubar, tearoff=0)
importmenu = Menu(menubar, tearoff=0)
editmenu = Menu(menubar, tearoff=0)

#File menu
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=create_window)
filemenu.add_command(label="Save as...", command=save_file)
filemenu.add_command(label="Exit", command=root.destroy)

#Edit menu
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Copy", command=None)
editmenu.add_command(label="Paste", command=None)
editmenu.add_command(label="Cut", command=None)
editmenu.add_command(label="Undo", command=None)

#View menu
menubar.add_cascade(label="View", menu=viewmenu)
viewmenu.add_command(label="Fullscreen", command=fullscreen)
viewmenu.add_command(label="Fill screen", command=max_screen)
viewmenu.add_command(label="Small screen", command=small_screen)

#Import menu
menubar.add_cascade(label="Import", menu=importmenu)
importmenu.add_command(label="File", command=None)

root.mainloop()
