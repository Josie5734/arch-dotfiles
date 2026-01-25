


def enter():
    print ("enter password")
    password = input()

    a = [ord(x) for x in password] # convert each char to ascii 

    for i,s in enumerate(a): # for each ascii value, add the value to the left

        if i == 0: # first value adds the last value
            a[i] += a[-1]
        else: a[i] += a[i-1] # everything else is the one to the left

    x = ""
    for z in a: # combine all ints into one string
        x += str(z) 

    with open("pass.txt","w") as file: # write to file
        file.write(x)

    print("pass written")


def test():
    print("enter password")
    password = input()

    a = [ord(x) for x in password] # convert to ascii

    for i,s in enumerate(a): # for each ascii value, add the value to the left

        if i == 0: # first value adds the last value
            a[i] += a[-1]
        else: a[i] += a[i-1] # everything else is the one to the left

    x = ""
    for z in a: # combine all ints into one string
        x += str(z) 

    with open("pass.txt","r") as file:
        rats = file.readline().rsplit()




# testing space 

print("1 - enter, 2 - open")

match input():
    case "1":
        enter()
    case "2":
        test()

# ideas for encryption

# convert to ascii
# shift numbers by original length of password
# shift number to the right by the orignal ascii of the letter to its left, wrap around for end/start chars

# e.g

# password = beans

# ascii = 02 05 01 15 22

# shifted by 5 = 07 10 06 20 27

# shifted right = 29 12 11 21 42


