import datetime

# log an error message in the log file
def errorlog(errormsg):

    try: # if file exists, log

        with open("log.txt","a") as file:
            date = datetime.datetime.now().strftime("%y-%m-%d_%H-%M-%S")
            file.write("\n"+date+": "+errormsg)

    except: # if file doesnt exist, create it, log its creation

        with open("log.txt","w") as file:
            date = datetime.datetime.now().strftime("%y-%m-%d_%H-%M-%S")
            #file.write("\n"+date+": log file created")
            file.write("\n"+date+": "+errormsg)
            

errorlog("hello")
errorlog("test")