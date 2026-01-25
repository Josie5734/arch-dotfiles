# testing for sorting algorithms

import random # for list generation, not used in the sorting
import time # used for time taken for functions

# create a random list of numbers
def number_list():

    numbers = []

    for i in range(100):
        numbers.append(i+random.randint(1,100)) # adds a random amount to each number

    random.shuffle(numbers)

    return numbers

# read a list of random words from words.txt
def word_list():

    with open("words.txt") as word_text:
        words = word_text.read().splitlines()

    return words



# recursive bubble sort for a list of integers
# currently just used as a generic base to be adapted for specific uses

    # seems to have a limit of 1316 items before hitting some sort of RecursionError (maximum recursion depth exceeded)
    # it is hitting pythons stack overflow limit, which can be increased but i shouldnt ever need to since the dataset is not that big

def bubblesort_int(data):

    compared = False # whether or not a comparison has been made in this pass of the data 
    max = len(data) # the length of the data list, used to know when to stop

    for i,num in enumerate(data): # for all items in list, keeping track of index
        if i < max-1: # if not at the max length of the list
            if data[i] > data[i+1]: # if current item is bigger than the next
                temp = data[i] # put current in temp slot
                data[i] = data[i+1] # set next as current
                data[i+1] = temp # set temp stored current as next
                compared = True # set comparison made to true

    if compared == True: # if comparison made this pass, 
        bubblesort_int(data) # call the whole function again to do another pass
    else:
        print("list sorted") # else print sorted message and the sorted data, this part wouldnt need to be included in a real usage
        print(data)

# variation of the recursive integer bubble sort that takes in an entire table from the db and sorts the rows by the values in the given column
def bubblesort_int_row(records, column):

    compared = False # whether or not a comparison has been made in this pass of the data 
    max = len(records) - 1 # the length of the data list, used to know when to stop. -1 to prevent comparing last item to out of range

    for row,value in enumerate(records): # for all rows in records
        if row < max: # if not at the max length of the list
            if records[row][column] > records[row+1][column]: # if value at column in current row is bigger than item at column in next row
                temp = records[row] # store current row in a temp
                records[row] = records[row+1] # move next row down to current position
                records[row+1] = temp # move current row into the next position
                compared = True # set comparison made to true

    if compared == True: # if comparison made this pass, 
        bubblesort_int_row(records, column) # call the whole function again to do another pass
    
    return records

# bubblesort for strings, to sort rows within a table
def bubblesort_str_row(records, column):

    compared = False
    max = len(records) - 1

    letter = 0

    for row,value in enumerate(records): # for every row in records
        if row < max: # if not at the end of records
            maxlets = len(records[row]) # get the number of letters in the current word
            if len(records[row+1]) < maxlets: # check if the next word has less letters
                maxlets = len(records[row+1]) # if so, make the max count the smaller number

            for l in range(maxlets): # for every letter in the word (or upto the length of the next word if smaller)
                if ord(records[row][l].upper()) > ord(records[row+1][l].upper()): # if current letter of current word is bigger than next
                    temp = records[row] # store current
                    records[row] = records[row+1] # put next into current slot
                    records[row+1] = temp # put current into next slot
                    compared = True # mark compared
                    break # exit out of looping through each letter

                elif ord(records[row][letter].upper()) < ord(records[row+1][letter].upper()): # else if current letter is less than next
                    break # exit loop, no need to check the rest

                # if the current letter is the same in current and next words, for loop will go to the next letter and check,
                    # should also just do nothing for 2 words that are the same so avoids any errors there
                    
            
    if compared == True: # if comparison made
        bubblesort_str_row(records,column) # do another pass

    return records # sorted list




#TODO potentially at some point: comparisons like "use" and "useless" end up with "use" put 2nd
    # not inherently an issue i guess but it seems counterintuitive
    # also words that are 3 letters long means the maxrec can only be 2
    # need some way to deal with very short words like this
    # and also words that contain shorter words that are also in the list

# a version of the recurisve bubble sort that works on strings using ascii values 
def bubblesort_str(data):

    compared = False # comparison made this pass
    max = len(data) # length of data list

    for i,word in enumerate(data): # for each item
        if i < max-1: # when not at end

            # compares 2 strings to check if they are alphabetically in order, returns True if strings need swapping
            def compare(item1, item2, index):

                # max number of recursions to do
                maxrec = 2
 
                # make strings lowercase to be case-insensitive                
                item1 = item1.lower()
                item2 = item2.lower()

                if ord(item1[index]) == ord(item2[index]) and index < maxrec: # if letters in item1 and 2 are equal
                    return compare(item1, item2, index+1) # call function again with index+1 (next letter)
                elif ord(item1[index]) > ord(item2[index]): # if letter in item1 is bigger
                    return True # return True to signal for a swap 
                else:
                    return False
                
            # do comparison on letters
            result = compare(data[i],data[i+1],0)

            if result == True: # if result is to swap
                temp = data[i] # put current in temp slot
                data[i] = data[i+1] # set next as current
                data[i+1] = temp # set temp stored current as next
                compared = True # set comparison made to true
                result = False # reset result (just incase)
    
    if compared == True: # if comparison made this pass
        bubblesort_str(data) # recall sort
    else: # else no comparisons
        print("list sorted") # list sorted
        print(data)
                        

# run functions 

# read text file
records = []
with open("words.txt","r") as file:
    for f in file:
        records = [line.rstrip() for line in file]
sortedlist = bubblesort_str_row(records,2)
print(sortedlist)