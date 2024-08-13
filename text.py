import cv2
import sklearn
print('done')

# from tkinter import *
# from tkinter.ttk import *
#
# # writing code needs to
# # create the main window of
# # the application creating
# # main window object named root
# root = Tk()
#
# # giving title to the main window
# root.title("First_Program")
#
# # Label is what output will be
# # show on the window
# label = Label(root, text="Hello World !").pack()
#
# # calling mainloop method which is used
# # when your application is ready to run
# # and it tells the code to keep displaying
# root.mainloop()

# ---------------------------
# # Creating button using Tkinter.
# # import everything from tkinter module
# from tkinter import *
# # create a tkinter window
# root = Tk()
# # Open window having dimension 100x100
# root.geometry('100x100')
# # Create a Button
# btn = Button(root, text = 'Click me !', bd = '5', command = root.destroy)
#
# # Set the position of button on the top of window.
# btn.pack(side = 'top')
# root.mainloop()

# # -----------------
# # Import Module
# from tkinter import *
# # create root window
# root = Tk()
# # root window title and dimension
# root.title("Welcome ")
# # Set geometry (widthxheight)
# root.geometry('350x200')
# # all widgets will be here
# # Execute Tkinter
# root.mainloop()

# -----------Checkbutton Widget------------------
# from tkinter import *
# root = Tk()
# root.geometry("300x200")
# w = Label(root, text ='SMEC', font = "50")
# w.pack()
#
# Checkbutton1 = IntVar()
# Checkbutton2 = IntVar()
# Checkbutton3 = IntVar()
#
# Button1 = Checkbutton(root, text = "Tutorial",
#                       variable = Checkbutton1,
#                       onvalue = 1,
#                       offvalue = 0,
#                       height = 2,
#                       width = 10)
#
# Button2 = Checkbutton(root, text = "Student",
#                       variable = Checkbutton2,
#                       onvalue = 1,
#                       offvalue = 0,
#                       height = 2,
#                       width = 10)
#
# Button3 = Checkbutton(root, text = "Courses",
#                       variable = Checkbutton3,
#                       onvalue = 1,
#                       offvalue = 0,
#                       height = 2,
#                       width = 10)
#
# Button1.pack()
# Button2.pack()
# Button3.pack()
# mainloop()

# # -------------------------------
# # Combobox Widget in tkinter
# # python program demonstrating
# # Combobox widget using tkinter
# import tkinter as tk
# from tkinter import ttk
#
# # Creating tkinter window
# window = tk.Tk()
# window.title('Combobox')
# window.geometry('500x250')
#
# # label text for title
# ttk.Label(window, text = "GFG Combobox Widget",
#           background = 'green', foreground ="white",
#           font = ("Times New Roman", 15)).grid(row = 0, column = 1)
#
# # label
# ttk.Label(window, text = "Select the Month :",
#           font = ("Times New Roman", 10)).grid(column = 0,
#           row = 5, padx = 10, pady = 25)
#
# # Combobox creation
# n = tk.StringVar()
# monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)
#
# # Adding combobox drop down list
# monthchoosen['values'] = (' January',
#                           ' February',
#                           ' March',
#                           ' April',
#                           ' May',
#                           ' June',
#                           ' July',
#                           ' August',
#                           ' September',
#                           ' October',
#                           ' November',
#                           ' December')
#
# monthchoosen.grid(column = 1, row = 5)
# monthchoosen.current()
# window.mainloop()



# # ------------------------------
# # Python Tkinter – Entry Widget
# # Program to make a simple
# # login screen
#
# import tkinter as tk
#
# root=tk.Tk()
#
# # setting the windows size
# root.geometry("600x400")
#
# # declaring string variable
# # for storing name and password
# name_var=tk.StringVar()
# passw_var=tk.StringVar()
#
# # defining a function that will
# # get the name and password and
# # print them on the screen
# def submit():
#
#     name=name_var.get()
#     password=passw_var.get()
#
#     print("The name is : " + name)
#     print("The password is : " + password)
#
#     name_var.set("")
#     passw_var.set("")
#
#
# # creating a label for
# # name using widget Label
# name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
#
# # creating a entry for input
# # name using widget Entry
# name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
#
# # creating a label for password
# passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
#
# # creating a entry for password
# passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
#
# # creating a button using the widget
# # Button that will call the submit function
# sub_btn=tk.Button(root,text = 'Submit', command = submit)
#
# # placing the label and entry in
# # the required position using grid
# # method
# name_label.grid(row=0,column=0)
# name_entry.grid(row=0,column=1)
# passw_label.grid(row=1,column=0)
# passw_entry.grid(row=1,column=1)
# sub_btn.grid(row=2,column=1)
#
# # performing an infinite loop
# # for the window to display
# root.mainloop()

# # --------------------------
# from tkinter import *
#
# root = Tk()
# root.geometry("300x200")
#
# w = Label(root, text ='SMEC', font = "50")
# w.pack()
#
# msg = Message( root, text = "A computer science portal")
#
# msg.pack()
#
# root.mainloop()

# # -------------------------------
# # importing only  those functions
# # which are needed
# from tkinter import *
# from tkinter.ttk import *
# from time import strftime
#
# # creating tkinter window
# root = Tk()
# root.title('Menu Demonstration')
#
# # Creating Menubar
# menubar = Menu(root)
#
# # Adding File Menu and commands
# file = Menu(menubar, tearoff = 0)
# menubar.add_cascade(label ='File', menu = file)
# file.add_command(label ='New File', command = None)
# file.add_command(label ='Open...', command = None)
# file.add_command(label ='Save', command = None)
# file.add_separator()
# file.add_command(label ='Exit', command = root.destroy)
#
# # Adding Edit Menu and commands
# edit = Menu(menubar, tearoff = 0)
# menubar.add_cascade(label ='Edit', menu = edit)
# edit.add_command(label ='Cut', command = None)
# edit.add_command(label ='Copy', command = None)
# edit.add_command(label ='Paste', command = None)
# edit.add_command(label ='Select All', command = None)
# edit.add_separator()
# edit.add_command(label ='Find...', command = None)
# edit.add_command(label ='Find again', command = None)
#
# # Adding Help Menu
# help_ = Menu(menubar, tearoff = 0)
# menubar.add_cascade(label ='Help', menu = help_)
# help_.add_command(label ='Tk Help', command = None)
# help_.add_command(label ='Demo', command = None)
# help_.add_separator()
# help_.add_command(label ='About Tk', command = None)
#
# # display Menu
# root.config(menu = menubar)
# mainloop()

# --------------------------
# # !/usr/bin/python3
# from tkinter import *
# #creating the application main window.
# top = Tk()
# #Entering the event main loop
# top.mainloop()

