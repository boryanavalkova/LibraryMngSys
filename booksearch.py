from database import *
from tkinter import *

# GUI

searchLabel = Label(searchTab, bg="#fad390", text="Enter book title:")  # header
searchLabel.grid(column=1, row=0)  # header coordinates

searchBar = Entry(searchTab, width=20)  # input
searchBar.grid(column=1, row=1)  # input coordinates

searchResultLabel = Label(searchTab, bg="#fad390", text="", wraplength="170")  # output
searchResultLabel.grid(column=4, row=1)  # output coordinates


# this function generates an output depending what the search title result is
def searchOutput():
    try:
        text = searchBar.get()  # gets the input from the user
        book = searchTitle(text)  # searches for the title using a function from database module
        if book == []:
            searchResultLabel.configure(text="No result is found.")
        else:
            bookString = " | ".join(
                str(item) for dataList in book for item in dataList)  # turns the 2d array into a string
            searchResultLabel.configure(text=bookString)  # configures the label to print the search result
    except TypeError:
        searchResultLabel.configure(text="No result is found.")


# For testing
if __name__ == '__menu__':
    text = "IT"
    searchOutput()
    print(text)
