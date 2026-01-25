# testing space 
print ("enter password")
password = input()

a = [ord(x) for x in password]

for i,s in enumerate(a):

    if i == 0:
        s += a[-1]
    else: s += a[i-1]

    return a

print(a)

# ideas for encryption

# convert to ascii
# shift numbers by original length of password
# shift number to the right by the orignal ascii of the letter to its left, wrap around for end/start chars

# e.g

# password = beans

# ascii = 02 05 01 15 22

# shifted by 5 = 07 10 06 20 27

# shifted right = 29 12 11 21 42


