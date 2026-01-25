# file for all database related functions



import sqlite3



### connection ###

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

### connection ###



### retrieve data ###



### retrieve data ###



### editing db contents ###



### editing db contents ###



## creating db ###  TODO update this, for now is just copypasted from old create_db.py


# create the data base and setup up connections + cursors
def connection(database):

    #connect to database and make a cursor for executing commands (also creates database if it doesnt exist)
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    # return cursor and connection
    return cursor,connection

# create employees table
def employees(cursor,connection):
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            EMPLOYEEID INTEGER PRIMARY KEY,
            FNAME TEXT, 
            SNAME TEXT,
            START INTEGER, 
            END INTEGER
        )
    ''')

    connection.commit()

# create customers table
def customers(cursor,connection):

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            CUSTOMERID INTEGER PRIMARY KEY,
            FNAME TEXT, 
            SNAME TEXT,
            ADDRESS TEXT, 
            PHONE INTEGER,
            EMAIL TEXT
        )
    ''')

    connection.commit()

# create vehicles tables
def vehicles(cursor,connection):

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vehicles (
            VEHICLEID INTEGER PRIMARY KEY
        )
    ''') # needs more stuff i cant remember what else was in this one

    connection.commit()

# create equipment table
def equipment(cursor,connection):

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS equipment (
            ITEMID INTEGER PRIMARY KEY,
            NAME TEXT, 
            STOCK INTEGER,
            TARGET INTEGER
        )
    ''') # needs more stuff cant remember

    connection.commit()
    
# create jobs table
def jobs(cursor,connection):

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            JOBID INTEGER PRIMARY KEY
        )
    ''') # needs more stuff cant remember

    connection.commit()
    
# call create function for all tables at once
def create_full_db(cursor,connection):
    employees(cursor,connection)
    customers(cursor,connection)
    vehicles(cursor,connection)
    equipment(cursor,connection)
    jobs(cursor,connection)

## creating db