from tkinter import *

root = Tk() # root window

root.title("Jomie Metronome") # window title
root.geometry("720x360") # window size

# label module
label = Label(root, text = "hello")
label.grid()

# display text when button clicked
def clicked():
    label.configure(text = "clicked")

# button widget with red text
btn = Button(root, text = "click", fg = "red", command=clicked)
btn.grid(column=1,row=0)


root.mainloop() # execute