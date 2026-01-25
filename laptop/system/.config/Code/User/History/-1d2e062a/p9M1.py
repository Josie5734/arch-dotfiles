from tkinter import *

# variables

window_width = 480
window_height = 640

# speed
bpm = 120

# time signatures
note_val = 4 # beats length
bar = 4 # beats in bar


# setup window
root = Tk() # root window
root.grid_columnconfigure(0,weight=1) # automatically horizontally center grid modules

root.title("Jomie Metronome") # window title
root.geometry("{}x{}".format(window_width,window_height)) # window size



# draw window stuff

# title text
title = Label(root, text = "Metronome", font=("JetBrains Mono Nerd",25))
title.grid(column = 0, row = 0)

# subtitle text
subtitle = Label(root, text = "By Josie5734", font=("JetBrains Mono Nerd",15))
subtitle.grid(column = 0, row = 1)



# speed output
speed = Label(root, text = bpm, font = ("JetBrains Mono",13))


# speed input


# speed +/- buttons 




# timing markers

# example of circle drawing
# canvas = Canvas(root, width=400, height=400)
# canvas.grid(column=0,row=4)

# canvas.create_oval(100, 100, 300, 300, outline="black", fill="white", width=2)







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