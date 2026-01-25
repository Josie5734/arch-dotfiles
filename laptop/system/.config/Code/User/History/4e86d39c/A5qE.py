# create dummy data to test functions with

import random

# employee table dummy data
def dummy_employee(rows):
    newrecs = []
    for i in range(rows): # for as many rows as requested
        row = []
        #id
        row.append(str(i+10))
        #fname
        with open("dummydata/fname.txt", "r") as file: # open the fname file
            num = random.randint(1,100) # generate a random line number
            for i, t in enumerate(file, start = 1): # go through the file 
                if i == num: # until getting to the random line number
                    fname = t.strip() # read the name
                    row.append(fname)
        #sname
        with open("dummydata/sname.txt","r") as file:
            num = random.randint(1,100)
            for i, t in enumerate(file, start = 1):
                if i == num:
                    sname = t.strip()
                    row.append(sname)
        #start
        row.append(str(random.randint(0,24)))
        #end
        row.append(str(random.randint(0,24)))
        
        #add to newrecs
        newrecs.append(row)
    return newrecs
    

### currently doing:
# trying to create a system that generates random rows of data for the employees table to make sort implementation easier