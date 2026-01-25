# file for all database related functions

import sqlite3



### connection and data retrieval ###

# currently unused connect and disconnect functions, hoping to make the connections more of a modular thing with these rather than always open, seems more safe

# make a connection to the database
def db_connect(database):

    try:
        # connect to database and make a cursor for executing commands (also creates database if it doesnt exist)
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
    except:
        print("failed to connect to database")
    else:
        connection = None 
        cursor = None

    # return cursor and connection
    return cursor,connection

# close the connection to the database
def db_disconnect(cursor, connection):

    try:
        cursor.close()
        connection.close()
    except:
        print("failed to disconnect from databse")


### connection and data retrieval ###



### editing db contents ###



### editing db contents ###



## creating db ###



## creating db