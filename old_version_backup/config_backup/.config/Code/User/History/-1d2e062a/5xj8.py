from tkinter import *

root = Tk() # root window

root.title("Jomie Metronome") # window title
root.geometry("480x640") # window size

# label module
title = Label(root, text = "Metronome")
title.grid(column = 0, row = 0, rowspan=1)

#text entry field
txt = Entry(root, width=10)
txt.grid(column=1,row=1)

# display text when button clicked
def clicked():
    res = "you wrote " + txt.get()
    title.configure(text = res)

# button widget with red text
btn = Button(root, text = "click", fg = "red", command=clicked)
btn.grid(column=2,row=1)

canvas = Canvas(root, width=400, height=400)
canvas.grid(column=0,row=4)

canvas.create_oval(100, 100, 300, 300, outline="black", fill="white", width=2)


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
###other stuff ########
######################