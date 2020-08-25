== Library Management System ==

Requires: python 3.7 and matplotlib
Uses: tkinter for the system's GUI and datetime module

== Description ==

Library Management System is a program that helps a librarian to manage the book database and log file of the library.

The program has options to search for a book by title, to return a book and to check out a book which are placed in different tabs.
It also keeps a log of all books and generates a chart which are most popular.

== Search function ==

The search function takes an user input (book title) and loops through the database to find a match.
The loop through the database is done by reading the whole file and creating 2D array containing each line of the database file.
Depending on the result another function generates the output, displaying a message of all the information connected to the book/books or "No result if found".

== Return function ==

The return function takes an user input (book ID) so that a book can be returned.
A similar search function as the title search loops through the database, however it uses the book ID to find the book and checks if the column for member ID is 0.
Depending on the result another function generates the output, displaying a message of not valid book ID or that the book is already available.
If the book is returned another function rewrites the database so that the member ID can be reset to 0 and make the selected book available again.
A new line in the log file is written displaying the book ID, the date that it has been checked out and the return date.

== Check out function ==

The check out function takes user inputs (book ID) and (member UD) so that a book can be checked out.
A similar search function as the title search loops through the database, however it uses the book ID to find the book and checks if the column for member ID is not 0.
Depending on the result another function generates the output, displaying a message of "not valid book ID or member ID" or "the book is already checked out" or "the book has been checked out".
If the book is checked out another function rewrites the database so that the member ID can be set to the member ID input and make the selected book unavailable.
A function gets the check out date and it is displayed in the log file when the chosen book is returned.

== Popular book function ==

The popular book function takes all the data from log file and loops through it to get every book ID that is in it.
The list containing all the IDs with repetition is filtered and the repetitions are by (using count) sorted, the duplicating ones are removed.
Then this list loops through the database to get the titles representing the each ID.
All this data is passed to a graph that appears by clicking the button that generates it.

== Reset/set member ID ==

This function loops through the database and finds the chosen book by its ID and changes/resets the value for the selected line in the member ID column.
Value 0 means that the book is available and a 4-digit number means that it is on loan.

== Create check out/return date ==

This function loops through the login file and gets all the data from it into a 2D list.
Then it appends new data to the list and writes it to the file and formats it as the previous.
It uses the datetime module to detect the exact date when a book is being checked out/returned.

== Check member ID/book ID ==

This function defines the range of possible inputs for member ID and book ID and validates the user input. If it is not correct it throws an error.

It uses the datetime module to detect the exact date when a book is being checked out/returned.

== Assignment restrictions ==
1)	Must NOT include any Class type. 
2)	Must NOT have any SQL statements.
3)	Use Python v3.7 or above.
4)	Must use only standard python libraries and Mathplotlib.
