import sqlite3

# filename for the database
database = "pestprof.db"

# create the data base and setup up connections + cursors
def create_db(database):

    #connect to database and make a cursor for executing commands (also creates database if it doesnt exist)
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

def employees(cursor,connection):
    
    # create employees table
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
    
    def customers():
        # create customers table

    def vehicles():
        # create vehicles tables

    def equipment():
        # create equipment table

    def jobs():
        # create jobs table

    # plan for this module
    # create each table required with required fields
    # maybe split each table into its own function so they can all be called and created individually
    # should also have default data inputted? not sure what that would be 
