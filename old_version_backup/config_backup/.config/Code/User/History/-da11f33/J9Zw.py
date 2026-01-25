import datetime

def errorlog(errormsg):

    try:

        with open("log.txt","a") as file:
            date = datetime.datetime.now().strftime("%y-%m-%d_%H-%M-%S")
            file.write("\n"+date+": "+errormsg)

    except:

        with open("log.txt","w") as file:
            date = datetime.datetime.now().strftime("%y-%m-%d_%H-%M-%S")
            file.write(date+": log file created")