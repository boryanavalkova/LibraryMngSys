from database import *
from tkinter import *

# GUI
checkOutLabelMID = Label(checkoutTab, bg="#fad390", text="Enter member ID:")  # header
checkOutLabelMID.grid(column=5, row=0)  # header coordinates

checkOutBarMID = Entry(checkoutTab, width=20)  # input for member ID
checkOutBarMID.grid(column=5, row=1)  # input for member ID coordinates

checkOutLabelBID = Label(checkoutTab, bg="#fad390", text="Enter book ID:")  # header
checkOutLabelBID.grid(column=5, row=2)  # header coordinates

checkOutBarBID = Entry(checkoutTab, width=20)  # input for book ID
checkOutBarBID.grid(column=5, row=3)  # input for book ID coordinates

checkOutResultLabel = Label(checkoutTab, bg="#fad390", text="")  # output
checkOutResultLabel.grid(column=7, row=2)  # output coordinates


# this function generates an output depending what check out result is
def checkOutOutput():
    try:
        text1 = checkOutBarMID.get()  # gets member ID input
        text2 = checkOutBarBID.get()  # gets book ID input
        resultMemberID = checkMemberID(text1)  # validates member ID
        resultBookID = checkbookID(text2)  # searches for book by ID
        if resultMemberID is not None and resultBookID is not None:
            resultCheck = checkOut(text2)  # triggers the check out function from database module
            if not resultCheck:
                checkOutResultLabel.configure(text="This book is not available.")
            else:
                checkOutResultLabel.configure(text="The book has been checked out.")
                changeMemberID(resultBookID, resultMemberID)  # generates date for log file
        else:
            checkOutResultLabel.configure(text="Not a valid book ID or member ID.")
    except:
        checkOutResultLabel.configure(text="Not a valid book ID or member ID.")


# For testing
if __name__ == '__menu__':
    text1 = "1029"
    text2 = "1"
    checkOutOutput()
    print(text1)
    print(text2)
