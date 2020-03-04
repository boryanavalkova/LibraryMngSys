# Boryana Valkova
# Introduction to programming coursework
# Library Management System

from tkinter import *
from tkinter import ttk
from booksearch import *
from bookreturn import *
from bookcheckout import *
from booklist import *

# GUI
menu.title("Library management system")
menu.geometry("800x400")

searchButton = Button(searchTab, text="Search", command=searchOutput)
searchButton.grid(column=3, row=1)

returnButton = Button(returnTab, text="Return", command=searchOutputID)
returnButton.grid(column=4, row=1)

checkOutButton = Button(checkoutTab, text="Check out", command=checkOutOutput)
checkOutButton.grid(column=6, row=2)

popularButton = Button(popularTab, text="Generate popular books", command=popularBook)
popularButton.grid(column=1, row=0)

menu.mainloop()
