# file for all database related functions



import sqlite3



### connection ###

# currently unused connect and disconnect functions, hoping to make the connections more of a modular thing with these rather than always open, seems more safe

# make a connection to the database
def db_connect(database):


    # connect to database and make a cursor for executing commands (also creates database if it doesnt exist)
    connection = sqlite3.connect(database)
    cursor = connection.cursor()


    # return cursor and connection
    return cursor,connection

# close the connection to the database
def db_disconnect(cursor, connection):

    cursor.close()
    cursor = None

    connection.close()
    connection = None


    return cursor, connection
    

### connection ###



### retrieve data ###


### retrieve data ###



### editing db contents ###

# function to add a new row, takes the table to add to, a list of the row data in order, and the headers of the table
def add_row(table,cursor,connection,row,headers):

    try:
        # create new row with the primary key
        statement = """INSERT INTO {}({}) \n VALUES('{}')""".format(table,headers[0],row[0])
        cursor.execute(statement)
        
        # update that row with the rest of the values
        for i,value in enumerate(row[1:],1): # go through each piece of data in row, starting from the one after the primary key
            statement = """UPDATE {} SET {} = "{}" \n WHERE {}='{}'""".format(table,headers[i],value,headers[0],row[0])
            cursor.execute(statement) # set the current value into the table at the matching header 

        connection.commit()
    except:
        print("could not add data to {}".format(table))
    

# function to edit a specific item at the given column and row
def edit_item(table,cursor,connection,item,column,key,headers): 
    
    try:
        # update the value in the given column in the row with the given primary key
        statement = """UPDATE {} SET {} = "{}" WHERE {}='{}'""".format(table,column,item,headers[0],key)
        cursor.execute(statement)
        connection.commit()
    except:
        print("could not edit data in {}".format(table))

# function to remove a row from a given table, key is the primary key of the row to be removed, headers used for the primary key column
def remove_row(table,cursor,connection,key,headers):

    try:
        # sql statement
        statement = """DELETE FROM {} WHERE {} = {}""".format(table,headers[0],key)

        # execute and commit
        cursor.execute(statement)
        connection.commit()
    except:
        print("could not remove data from {}".format(table))


### editing db contents ###



## creating db ###  

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