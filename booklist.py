from database import *
import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

# this function returns a 2D array containing the logfile information
def getLogFile():
    contentList = []  # empty list
    file = open("logfile.txt", "r")
    for line in file:  # loop that makes each line of the data a separate list
        dataList = (line.replace("  ", "").replace("\n", "").replace("\t", "").split("|"))  # makes each line list
        contentList.append(dataList)  # appends each list line to the list
    return (contentList)

# this function generates the graph of the books that have been checked out
def popularBook():
    popularListRep = []
    logs = getLogFile()
    counter = 0
    while counter < len(logs):  # generates a list containing the book IDs from log file
        popularListRep.append(logs[counter][0])
        counter = counter + 1
    popularListRep.pop(0)
    popularList = list(dict.fromkeys(popularListRep))  # sorts the list by removing duplicates and arranges each ID by popularity

    titleList = []
    file = open("database.txt", "r")
    for line in file:  # loop that makes each line of the data a separate list
        dataList = (line.replace("  ", "").replace("\n", "").replace("\t", "").split("|"))
        for item in popularList:
            if item == dataList[0]:  # checks the book by its ID
                titleList.append((dataList[1]))

    countList = []
    counter1 = 0
    while counter1 < len(popularList):  # counts how many times each book has been mentioned in the log file
        countList.append(popularListRep.count(popularList[counter1]))
        counter1 = counter1 + 1

    # creates the graph
    global yaxis
    figure = Figure(figsize=(10, 4), dpi=80)
    ax = figure.add_subplot(111)
    ax.set_facecolor("#fad390")
    figure.patch.set_facecolor("#fad390")

    title = ax.set_title("Popular books")

    width = 0.5
    graph = ax.barh(titleList, countList, width)

    global canvas
    canvas = FigureCanvasTkAgg(figure, popularTab)
    canvas.draw()
    canvas.get_tk_widget().grid(column=1, row=1)


