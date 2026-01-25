# TODO

### current objective:

    # add in rest of menus 
        # will need to generate some test data for all of them
        # then build them using existing employees menu template
        # make specific changes where necessary
        # try to generalise as much as possible into its own functions to use across all menus

    # potentially make a quick sort for the equipment file since that will have the most data to sort



    # at some point, the output for the menus could probably be sent to its own global function that every menu can use
        # currently the only menu specific thing it uses is the title/table-name, which is already stored menu specific so could just be passed in
        # data table has been made into a function, can just be called after printing the tables title, includes the options list

    # consider "error messages" for things like typing in a wrong input, e.g when trying to remove an entry and typing an ID that doesnt exist



# import modules
import os # used for system commands e.g clear
from time import sleep # sleep for x seconds
import sqlite3 # SQL database 
import sys # sys.exit to kill program

# import other files/functions
import db_functions # all database functions
import password.password as password # password functions
import log # error logging 
import dummydata # generating dummy data
import sort # sorts, searches, filters



### globals ###

# database filename
database = "pestprof.db"

# connect to database
cursor,connection = db_functions.db_connect(database)

### globals ###






### util functions ###

# clear terminal 
def clear():
    name = os.name # get operating system
    if name == "nt": # if windows(nt), use 'cls'
        os.system("cls")
    else: # else use 'clear' for linux/mac
        os.system("clear")

# format strings to add whitespace to the end, can also take a list instead of a single string
def sformat(text, space): 

    fullstring = "" # store formatted text

    # format function, operates on individual string
    def do_format(t):
        mlen = space # target length of string
        character = " " # character used to fill in empty space
        mlen -= len(t) # take current length of string away to get required amount of space filler
        for i in range(mlen): # add character to fill remaining space
            t = t + character 
        return t

    inputtype = type(text) # get type of text input

    if inputtype == str: # if string
        fullstring = do_format(text) # format
    elif inputtype == int: # else if int
        fullstring = do_format(str(text)) # format with conversion to string
    elif inputtype == list: # else if list
        for txt in text: # check each item in list
            if isinstance(txt, int): # convert to string if int
                txt = str(txt) 
            elif not isinstance(txt, int) and not isinstance(txt, str): # if not int or string
                txt = "error" # set text to be an error
                log.errorlog("type error during text formatting") # log format error
            fullstring = fullstring + do_format(txt) # do the formating to item and add it to full string
    else: # else if not string, int or list
        txt = "error" # set text to be an error
        log.errorlog("type error during text formatting") # log format error

    return fullstring # return formatted string

# output a given record as a table of data, using the given spacing and headers
def table_output(data_table,headers,spacing): # default output for the menu
        print(sformat(headers, spacing)) # print headers
        
        for row in data_table: # print the table of data under the headers
            print(sformat(str(row[0]),spacing) + sformat(row[1],spacing) + sformat(row[2],spacing) + sformat(str(row[3]),spacing) + sformat(str(row[4]),spacing))

        print("\n")
        print("options: 1 - edit : 2 - add : 3 - remove : 4 - sort : 5 - filter/search : 9 - reset filters/searches : 0 - back")
    

### util functions ###



### menu functions ###

# homescreen menu #
def homescreen():

    clear() # clear screen

    def output():
        print("welcome to the pest professor")
        print()
        print("options:")
        print("1 - employees : 2 - customers : 8 - generate data : 9 - generate db : 0 - exit")
        print()
        print("type number to go to file")

    output() # print menu outout
    option = input() # get user input

    match option: # switch case for input
        case "1": # employees
            print("going to employees")
            sleep(0.5)
            employees()

        case "2": # customers
            print("going to customers")
            sleep(0.5)
            customers()

        case "0":
            cursor.close()
            connection.close()
            print("closing application")
            sleep(0.5)
            sys.exit()

        case _: # default, if not a listed option, give error, reload homescreen menu
            print("invalid option, retry after reload")
            sleep(2)
            clear()
            homescreen() # restart menu



# employee menu #
def employees(records = None): 
    clear() # clear screen

    spacing = 20 # menu spacing used for formatted prints
    table = "employees" # holds the table name for passing to functions

    # get data pieces
    headers = db_functions.get_headers(table,cursor,connection) # get headers of table
    
    if records == None: # if no record has been passed in
        records = db_functions.get_data(table,cursor,connection) # get the data for the current table

    # print title
    print("employees \n")
    # print data table
    table_output(records,headers,spacing) 

    # get user input
    option = input()

    # do stuff with input
    match option:
        case "1": # edit an entry
            print("enter employeeID to edit : q to quit") # get primary key of row to edit
            key = str(input()) # store as string

            if key == "q": # if input is q for quit
                employees() # just reload menu 

            # else do actual function
            print("enter column to edit") 
            headerstring = "" # empty string to be printed
            for i,h in enumerate(headers, start=1): # for each header
                temp = " " + str(i) + " - " + h + " :" # string with a number and corresponding header + formatting
                headerstring = headerstring + temp # add to initial string
            print(headerstring[:-2]) # print out which number is which header 
            
            choice = int(input()) # get column to edit as int

            column = headers[choice-1] # use that int to get the matching header

            print("enter new value")
            item = str(input()) # store it as string

            db_functions.edit_item(table,cursor,connection,item,column,key,headers) # call edit function 

            exec("{}()".format(table)) # dynamically reload menu, assuming table is the same as the menu function name

        case "2": # add an entry
            newrow = []

            # automatically iterate the ID and add to newrow
            id = records[-1][0] + 1
            newrow.append(id)
            
            for h in headers[1:]: # for each header in the current table, starting from the one after the ID
                print("enter new {} : q to quit".format(h)) # print message to ask for a new value or quit
                newval = str(input()) # take the user input as string

                if newval == "q": # if q for quit is entered
                    employees() # reload menu without doing anything
                else: # else continue with adding headers
                    newrow.append(newval) # add it to a list
            
            db_functions.add_row(table,cursor,connection,newrow,headers) # call function to add newrow to the table

            exec("{}()".format(table)) # dynamically reload menu, assuming table is the same as the menu function name

        case "3": # remove an entry
            print("enter EmployeeID to remove : q to quit") # get id to remove
            key = str(input()) # store it

            if key == "q": # if q for quit
                employees() # reload menu without doing anything

            else: # else do normal stuff, for some reason was getting an error where this stuff would be run when exiting the program
                    # if the program was run, employee file entered, remove command entered, but then quit with q, then exit employee file and exit program:
                        # got error where remove_row() was still called upon pressing 0 in home menu? no idea how but putting it in this else bracket fixed it for now

                # else do remove function
                db_functions.remove_row(table,cursor,connection,key,headers) # call remove function

                exec("{}()".format(table)) # dynamically reload menu, assuming table is the same as the menu function name

        case "4": # sort
            print("sort by which column number?")
            headerstring = "" # empty string to be printed
            for i,h in enumerate(headers, start=1): # for each header
                temp = " " + str(i) + " - " + h + " :" # string with a number and corresponding header + formatting
                headerstring = headerstring + temp # add to initial string
            print(headerstring[:-2]) # print out which number is which header 

            colnum = input()
            colnum = int(colnum) - 1 # get user input for which column to sort by, as int, -1 to account for user being shown headers starting from 1

            sort_recs = None # empty value used for putting sorted records in 

            item = records[0][colnum] # get the piece of data in the first row of the specific column for type checking

            if type(item) == str: # if item is string
                sort_recs = sort.bubblesort_str_row(records,colnum) # get sorted version of data

            elif type(item) == int: # else if item is int
                sort_recs = sort.bubblesort_int_row(records,colnum) # get sorted version of data 

            exec("{}(sort_recs)".format(table)) # dynamically reload menu, assuming table is the same as the menu function name
            
        case "5": # filter
            print("enter data to filter by:")
            filter = str(input().lower()) # get input as lowercase string

            filter_recs = [] # filtered records

            for row in records: # for every row in records
                found = False # if filter string is found in data item
                for column in row: # for every column in row
                    if found != True and filter in str(column).lower(): # if not already found a match and filter string is in data item (as a lowercase string to match input)
                        found = True # set found 
                        filter_recs.append(row) # add row to filtered records

            employees(filter_recs) # update menu

        case "9": # reset filters and searches
            employees() # reload menu

        case "0": # go back home
            print("going to home menu")
            sleep(0.5)
            homescreen()

        case _: # default, reload the menu
            employees()

# employee menu



# customer menu

def customers(valid = False):
    clear() # clear screen

    if valid == False: # if correct password has not been given
        password.password_output(homescreen, customers, clear)
    else: # else password was given/correct
        print("employees menu not currently implemented \n press any button to continue")
        input() # rest of menu goes here, not implemented for now
        homescreen() # just returns home

#customer menu



### program execution ###

clear() # clear any previous stuff
homescreen() # run program, starting from homescreen, should all just branch out from here

### program execution ###