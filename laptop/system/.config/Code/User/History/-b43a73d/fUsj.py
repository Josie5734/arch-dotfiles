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

# get data from db. returns "records" which is a list of lists(rows from table)
def get_data(table):

    try:
    
        query = """SELECT * from {}""".format(table)
        cursor.execute(query) # query to select all items in the table 
        records = cursor.fetchall() # get all data at cursor
        #print("totals rows are: ", len(records)) # get number of rows - leaving commented incase needed
    except:
        print("could not get data from {}".format(table))
    else:
        records = None

    return records # return the list of row lists

# get the headers from a given table - should also be moved to a better place eventually
def get_headers(table):

    try:
        cursor.execute("SELECT * FROM {}".format(table)) # read table (next line needs an .execute() to have been done)
        headers = [i[0] for i in cursor.description] # gets .description() of the executed table and takes the first result(column name) from each column, puts into a list
    except:
        print("could not get headers from {}".format(table))
    else:
        headers = None
    
    return headers

### retrieve data ###



### editing db contents ###



### editing db contents ###



## creating db ###  TODO update this, for now is just copypasted from old create_db.py

# create the database and setup up connections + cursors
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

### creating db ###