import datetime

def errorlog(errormsg):

    with open("log.txt","a") as file:
        date = datetime.datetime.now().strftime("%y-%m-%d_%H-%M-%S")
        file.write("\n"+date+": "+errormsg)
