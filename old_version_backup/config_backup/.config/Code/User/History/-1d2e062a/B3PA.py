from tkinter import *

root = Tk() # root window

root.title("Jomie Metronome") # window title
root.geometry("720x360") # window size

# label module
label = Label(root, text = "hello")
label.grid()

#text entry field
txt = Entry(root, width=10)
txt.grid(column=1,row=0)

# display text when button clicked
def clicked():
    res = "you wrote " + txt.get()
    label.configure(text = res)

# button widget with red text
btn = Button(root, text = "click", fg = "red", command=clicked)
btn.grid(column=2,row=0)



circle = Canvas.create_oval(10,10,80,80, outline="black",fill="red",width=2)
circle.grid(column=3,row=0)


root.mainloop() # execute