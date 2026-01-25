# create dummy data to test functions with

import random

# employee table dummy data
def dummy_employee(rows):
    for i in range(rows): # for as many rows as requested
        with open("dummydata/fname.txt", "r") as file:
            name = random.randint(1,100)
            for i, t in enumerate(file, start = 1):
                if i == name:
                    name = t.strip()
                    print(name)

# execute

dummy_employee(10)
                
