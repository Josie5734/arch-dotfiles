from tkinter import *


window_width = 480
window_height = 640

root = Tk() # root window
root.grid_columnconfigure(0,weight=1) # automatically horizontally center grid modules

root.title("Jomie Metronome") # window title
root.geometry("480x640") # window size

# title text
title = Label(root, text = "Metronome")
title.grid(column = 0, row = 0)

# subtitle text




# speed output


# speed input


# speed +/- buttons 




# timing markers

# example of circle drawing
canvas = Canvas(root, width=400, height=400)
canvas.grid(column=0,row=4)

canvas.create_oval(100, 100, 300, 300, outline="black", fill="white", width=2)







# #text entry field
# txt = Entry(root, width=10)
# txt.grid(column=1,row=1)

# # display text when button clicked
# def clicked():
#     res = "you wrote " + txt.get()
#     title.configure(text = res)

# # button widget with red text
# btn = Button(root, text = "click", fg = "red", command=clicked)
# btn.grid(column=2,row=1)


root.mainloop() # execute



# design layout

####### title ########
### sub title ########
######################
## buttons +/- speed #
### circles        ###
### circles        ###
### circles        ###
### circles        ###
######################
###time sig   ########
######################