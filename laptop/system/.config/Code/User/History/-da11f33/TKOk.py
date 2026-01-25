import datetime

with open("log.txt", "w") as file:
    file.write("this is the log \n")
    file.write("the log stuff goes here")

with open("log.txt","a") as file:
    steve = "\n"
    date = datetime.datetime.now()
    file.write(steve+date+": error, invalid thingy")

with open("log.txt","r") as file:
    print(file.read())
