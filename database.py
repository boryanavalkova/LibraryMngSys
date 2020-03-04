from tkinter import *
from tkinter import ttk
from datetime import date

# GUI
menu = Tk()

operateTabs = ttk.Notebook(menu)

style = ttk.Style()
settings = {"TNotebook.Tab": {"configure": {"padding": [4, 2], "background": "#f6b93b", "foreground": "#0a3d62"}}}
style.theme_create("style", parent="alt", settings=settings)
style.theme_use("style")

# creates the tabs
searchTab = ttk.Frame(operateTabs)
operateTabs.add(searchTab, text="Search")

returnTab = ttk.Frame(operateTabs)
operateTabs.add(returnTab, text="Return")

checkoutTab = ttk.Frame(operateTabs)
operateTabs.add(checkoutTab, text="Check out")

popularTab = ttk.Frame(operateTabs)
operateTabs.add(popularTab, text="Top books")

popularTab = Canvas(popularTab)
popularTab.pack(side=RIGHT, expand=1)

operateTabs.pack(expand=1, fill="both")


# this function searches for a book by its title and returns the whole line of information corresponding to that title
def searchTitle(title):
    contentList = []  # empty array where all the data is stored
    file = open("database.txt", "r")
    for line in file:  # loop that makes each line of the data a separate list
        dataList = (line.replace("  ", "").replace("\n", "").replace("\t", "").split("|"))
        if title == dataList[1]:  # checks if the title is in the second column of database
            contentList.append(dataList)  # adds the data in one big list
    return (contentList)  # returns the line in which the title appears


# this function searches for a book by its ID and returns the whole line of information corresponding to that title
def searchID(bookID):
    contentList = []  # empty array where all the data is stored
    file = open("database.txt", "r")
    for line in file:  # loop that makes each line of the data a separate list
        dataList = (line.replace("  ", "").replace("\n", "").replace("\t", "").split("|"))
        contentList.append(dataList)  # adds the data in one big list
        if bookID in dataList[0] and dataList[4] != '0':  # checks the book by its ID and if it is on loan
            return (dataList)  # returns the line in which the unavailable book appears


# this function searches for a book by its ID and returns the whole line of information corresponding to that book ID
def checkOut(bookID):
    contentList = []  # empty array where all the data is stored
    file = open("database.txt", "r")
    for line in file:  # loop that makes each line of the data a separate list
        dataList = (line.replace("  ", "").replace("\n", "").replace("\t", "").split("|"))
        if bookID == dataList[0] and dataList[4] == '0':  # checks the book by its ID and if it is not on loan
            contentList.append(dataList)  # adds the data in one big list
    return (contentList)  # returns the line in which the available book appears


# this function resets the member ID to 0 when a book is returned
def resetMemberID(bookID):
    contentList = []  # empty array where all the data is stored
    file = open("database.txt", "r")
    for line in file:  # loop that makes each line of the data a separate list
        dataList = (line.replace("  ", "").replace("\n", "").replace("\t", "").split("|"))
        contentList.append(dataList)  # adds the data in one big list
        correctLine = int(bookID)  # selects the line of the chosen book
    contentList[correctLine][4] = '0'  # selects the correct line and element and rewrites the member ID to 0
    file = open("database.txt", "w")
    for ID in contentList:
        file.write("|".join(ID))  # formats string for output
        file.write("\n")
    file.close()
    return contentList[correctLine]


# this function changes the member ID to the typed member ID when a book is checked out
def changeMemberID(bookID, memberID):
    contentList = []  # empty array where all the data is stored
    file = open("database.txt", "r")
    for line in file:  # loop that makes each line of the data a separate list
        dataList = (line.replace("  ", "").replace("\n", "").replace("\t", "").split("|"))
        contentList.append(dataList)  # adds the data in one big list
        correctLine = int(bookID)  # selects the line of the chosen book
    contentList[correctLine][4] = memberID  # selects the correct line and element and rewrites the member ID to the current
    file = open("database.txt", "w")
    for ID in contentList:
        file.write("|".join(ID)) # formats string for output
        file.write("\n")
    file.close()
    return (contentList[correctLine])


# this function creates the return date
def returnDate(partly):
    contentList = []  # empty array where all the data is stored
    file = open("logfile.txt", "r")
    for line in file:  # loop that makes each line of the data a separate list
        dataList = (line.replace("  ", "").replace("\n", "").replace("\t", "").split("|"))
        contentList.append(dataList)  # adds the data in one big list
    partList = partly.split("|")
    if partList in contentList: # generates date and writes it in logfile
        today = date.today()
        todayFormat = today.strftime("%d.%m.%y")
        file = open("logfile.txt", "a")
        completeLine = file.write("|" + todayFormat)
        file.close()
        return completeLine


# this function creates the check out date
def checkoutDate(bookID):
    contentList = []  # empty array where all the data is stored
    file = open("logfile.txt", "r")
    for line in file:  # loop that makes each line of the data a separate list
        dataList = (line.replace("  ", "").replace("\n", "").replace("\t", "").split("|"))
        contentList.append(dataList)  # adds the data in one big list
    today = date.today()
    todayFormat = today.strftime("%d.%m.%y")
    fileChange = open("logfile.txt", "a")
    newLine = [bookID, todayFormat]
    newLineStr = "|".join(newLine)
    fileChange.write("\n" + newLineStr) # generates date and writes it in logfile
    fileChange.close()
    return (newLineStr)


# this function validates the input for member ID
def checkMemberID(memberID):
    if int(memberID) == 0:  # checks if the number is 0
        raise ValueError()
    elif int(memberID) in range(1000, 10000):  # checks if the number is in the acceptable range
        return memberID
    else:
        return None


# this function validates the input for book ID
def checkbookID(bookID):
    if int(bookID) not in range(1, 12):  # checks if the output ii not in the acceptable range
        raise ValueError()
    elif int(bookID) in range(1, 12):  # checks if the number is in the acceptable range
        return bookID
    else:
        return None


# For testing - title search
if __name__ == '__menu__':
    text = "IT"
    searchTitle(text)
    print(text)

# For testing - book ID search
if __name__ == '__menu__':
    text = "1"
    searchID(text)
    print(text)

# For testing - checkout
if __name__ == '__menu__':
    text = "1"
    checkOut(text)
    print(text)

# For testing - reset member ID
if __name__ == '__menu__':
    text = "1"
    resetMemberID(text)
    print(text)

# For testing - change member ID
if __name__ == '__menu__':
    text1 = "1"
    text2 = "1923"
    changeMemberID(text1, text2)
    print(text1)
    print(text2)
