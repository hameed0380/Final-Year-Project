#To import everything from tkinter
from tkinter import *
from tkinter import font
import tkinter.messagebox

from TSPGA_application import *

#Creating the class, Window, and inheriting from the Frame which is a class from tkinter
#class. Frame is a class from the tkinter module 
class Window(Frame):

    # Define settings upon initialization. At this point you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class 
        Frame.__init__(self, master)   

        #reference to the master widget created, which is the tk window                 
        self.master = master

        #To run init_window, which does not exist yet
        self.init_window()

    #Creation of init_window
    def init_window(self):

        #changing the title of the master widget to Survival Rate Application     
        self.master.title("TSP Genetic Algorithm")

        '''allowing the widget to take the full space of the root window
        so widgit is continuously shown even when root window has been changed
        in size'''
        self.pack(fill=BOTH, expand=1)

        #creating a menu instance
        menu = Menu(self.master, tearoff=False)
        self.master.config(menu=menu)


        #create the Simulator object
        Simulator = Menu(menu)
        #added "Simulator" to the menu created
        menu.add_command(label="Run", command=self.Run)

        #create the help_centre object
        help_centre = Menu(menu)
        #added "Help Centre" to the menu that has been created
        menu.add_cascade(label="Help Centre", menu=help_centre)
        '''When the help centre button is clicked the Help object should be
        shown, carry out its command in the function Help'''
        help_centre.add_command(label="Help", command=self.Help)

    def Help(self): 
        root = tkinter.Tk()
        T = tkinter.Text(root, height=2, width=30)
        T.pack()
        T.insert(tkinter.END, "Just a text Widget\nin two lines\n")
        tkinter.mainloop() 


    def info():
        tkinter.messagebox.showinfo('About', 'SAP is an application dedicated to finding \nthe survival rate of organisms and storing \nthem in a database')
        # Create the title about for the messagebox


		#window.mainloop()

    def Run(self):
    	main()




''' root window created. Here, that would be the only window, but
 you can later have windows within windows.'''

root = Tk()# Creating the window
root.geometry("400x300")# Defining and setting the dimesions of the window/client

#creation of an instance
app = Window(root)


#mainloop 
root.mainloop()  
