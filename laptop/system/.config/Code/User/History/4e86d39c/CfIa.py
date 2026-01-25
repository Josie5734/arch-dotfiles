# create dummy data to test functions with

import random

# employee table dummy data
def dummy_employee(rows):
    for i in range(rows): # for as many rows as requested
        fname = ""
        with open("dummydata/fname.txt", "r") as file: # open the fname file
            num = random.randint(1,100) # generate a random line number
            for i, t in enumerate(file, start = 1): # go through the file 
                if i == num: # until getting to the random line number
                    fname = t.strip() # read the name

        
            

# execute

dummy_employee(10)
                


### currently doing:
# trying to create a system that generates random rows of data for the employees table to make sort implementation easier