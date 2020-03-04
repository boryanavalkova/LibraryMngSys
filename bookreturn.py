from database import *
from tkinter import *

# GUI
returnLabel = Label(returnTab, bg="#fad390", text="Enter book ID:")  # header
returnLabel.grid(column=3, row=0)  # header coordinates

returnBar = Entry(returnTab, width=20)  # input for book ID
returnBar.grid(column=3, row=1)  # input for book ID coordinates

returnResultLabel = Label(returnTab, bg="#fad390", text="")  # output
returnResultLabel.grid(column=5, row=1)  # output coordinates


# this function generates an output depending what the return search result is
def searchOutputID():
    try:
        text = returnBar.get()  # gets book ID
        ID = searchID(text)  # searches for book by its ID
        checkbookID(text)  # validates book ID
        if ID is None:
            returnResultLabel.configure(text="This book is already available.")
        else:
            returnResultLabel.configure(text="The book has been returned.")
            returnDate(checkoutDate(text))  # writes the checkout and return date in the log file
            resetMemberID(text)  # writes the member ID to 0
    except ValueError:
        returnResultLabel.configure(text="Not a valid book ID.")


# For testing
if __name__ == '__menu__':
    text = "1"
    searchOutputID()
    print(text)
