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



# recursive bubble sort (for integers, could probably be modified fairly easily for text)

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

def bubblesort_str(data):

    compared = False # comparison made this pass
    max = len(data) # length of data list

    for i,word in enumerate(data): # for each item
        if i < max-1: # when not at end

            # compares 2 strings to check if they are alphabetically in order, returns 1 if strings need swapping, 2 if nothing needs to be done
            def compare(item1, item2, index):
 
                # make strings lowercase to be case-insensitive                
                item1 = item1.lower()
                item2 = item2.lower()

                if ord(item1[index]) == ord(item2[index]): # if letters in item1 and 2 are equal
                    compare(item1, item2, index+1) # call function again with index+1 (next letter)
                elif ord(item1[index]) > ord(item2[index]): # if letter in item1 is bigger
                    print("working")
                    return True # return a 1 (swap) 
                
            # do comparison on letters
            result = compare(data[i],data[i+1],0)

            # TODO error - this if statement is seemingly skipped for words that are swapped from letters after index 0?
                # the 'result' var is returned as none, even though it says 'return "swap" and also it works for swapping from index 0
                # so i have no idea what is happening here
                # currently it does sort the list alphabetically but only to the first letter

            if result == True: # if result is to swap
                temp = data[i] # put current in temp slot
                data[i] = data[i+1] # set next as current
                data[i+1] = temp # set temp stored current as next
                compared = True # set comparison made to true
                result = False
    
    if compared == True: # if comparison made this pass
        bubblesort_str(data) # recall sort
    else: # else no comparisons
        print("list sorted") # list sorted
        print(data)
                        



# call functions and stuff

start = time.time() # time measurement 

#bubblesort_int(number_list()) # calls the sort for the first pass, calling the number list generator as a data input
# number list would be replaced with the actual data to be sorted in real application 

bubblesort_str(word_list())

end = time.time() # time measurement 

print("took " + str(end - start) + " seconds") # time measurement output