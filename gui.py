from tkinter import *

# creating window
mywindow = Tk() #Created a main window


mywindow.title("Simple GUI") #Title of the current window
mywindow.geometry("780x640") #Size of the window
mywindow.minsize(540,420) #Set a limit for the windows minimum size
mywindow.configure(bg="grey") #The colour of the background


message_label = Label(mywindow, text="Genetic Algorithm")
message_label.pack()


# widgets




mywindow.mainloop() #Show the end of every window