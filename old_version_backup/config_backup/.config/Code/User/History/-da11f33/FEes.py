import datetime

    # this file just has a function to write given error messages to a log file
    # this may be moved later on, is fine here for now

# log an error message in the log file
def errorlog(errormsg):

    try: # if file exists, log

        with open("log.txt","a") as file:
            date = datetime.datetime.now().strftime("%y-%m-%d_%H-%M-%S")
            file.write("\n"+date+": "+errormsg)

    except: # if file doesnt exist, create it, log its creation

        print("error, could not access log file")
            