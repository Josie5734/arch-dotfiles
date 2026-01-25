import os

### password stuff ###

# function to convert passwords into encrypted form
def password_encrypt(password):

    pass_ascii = [ord(x) for x in password] # convert to ascii 

    for i,s in enumerate(pass_ascii): # for each ascii value, add the value to the left

        if i == 0: # first value adds the last value
            pass_ascii[i] += pass_ascii[-1]
        else: pass_ascii[i] += pass_ascii[i-1] # everything else is the one to the left

    pass_str = ""
    for i in pass_ascii: # combine all ints into one string
        pass_str += str(i) 

    return pass_str

# function to handle the file stuff for the password. password inputted and operation is either "r" read or "w" write
def password_file(password, operation):

    if operation == "w": # writing new password
        with open("password/pass.txt","w") as file: # open file
            file.write(password) # write in password
    
    elif operation == "r": # reading/comparing password
        with open("password/pass.txt") as file: # open file
            value = file.read() # get written password
            if password == value: # compare
                return True # true if correct
            else: return False # else false

# output menu for the customer menu password
def password_output(homescreen, customers, clear):

    clear()

    # password stuff
    print("enter password to continue : enter ""reset"" to reset the password")
    password = str(input()) # get password input as string

    # if reset option was inputted
    if password == "reset":
        clear() # clear
        print("reset mode : enter new password")
        password = str(input()) # get input
        password = password_encrypt(password) # encrypt password
        password_file(password,"w") # write password to file
        password_output(homescreen, customers) # reload password menu
        clear() # clear screen
    
    # else just normal password checking
    password = password_encrypt(password) # encrypt password
    valid = password_file(password,"r") # compare

    if valid == False: # if password was incorrect
        print("password incorrect : r - retry : q - quit")
        option = input()

        if option == "r": # if retry selected
            password_output(homescreen,customers) # restart password function
        elif option == "q": # if quit selected
            homescreen() # go back to homescreen
    elif valid == True: # else if password was correct
        customers(valid) # call customers menu again with correct password marker

### password stuff ###