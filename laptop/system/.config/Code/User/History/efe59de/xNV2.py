import sqlite3

# module for functions to edit the database
# add/remove/edit etc
# not entirely sure what this will look like
# just making it to separate everything out from the start

# example for later
'''
def add_with_variables():

    # store some of the data pieces in variables
    name = 'rubber rat'
    target = 90

    # command to add a new row of data, using .format to insert the data stored in variables
    cursor.execute("INSERT INTO equipment (STOCKID, ITEM, STOCK, TARGET, PRICE) VALUES (3, '{}', 2, {}, 6)".format(name, target))

    connection.commit() # commit changes
'''
