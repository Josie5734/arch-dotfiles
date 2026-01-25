with open("log.txt", "w") as file:
    file.write("this is the log \n")
    file.write("the log stuff goes here")

with open("log.txt","r") as file:
    print(file.read())

with open("log.txt","a") as file:
    file.write("error, invalid thingy")

with open("log.txt","r") as file:
    print(file.read())
