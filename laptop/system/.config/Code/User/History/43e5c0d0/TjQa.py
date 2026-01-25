import sqlite3

    # plan for this module
    # create each table required with required fields
    # maybe split each table into its own function so they can all be called and created individually
    # should also have default data inputted? not sure what that would be 


# filename for the database
database = "pestprof.db"

# create the data base and setup up connections + cursors
def create_db(database):

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
            VEHICLEID INTEGER PRIMARY KEY,
            
        )
    ''')

    connection.commit()

# create equipment table
def equipment(cursor,connection):

    cursor.execute()

    connection.commit()
    
# create jobs table
def jobs(cursor,connection):

    cursor.execute()

    connection.commit()
    

