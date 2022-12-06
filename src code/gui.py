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

        #changing the title of the master widget to TSP Genetic Algorithm
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
        menu.add_command(label="Info", command=self.Help)
        
        
        #This button can close the window
        button_1 = Button(root, text =" Force Quit", command = root.destroy)
        button_1.pack(pady = 50)


    def Help(self): 
        root = tkinter.Tk()
        T = tkinter.Text(root, height=10, width=40)
        T.pack()
        T.insert(tkinter.END, "Genetic Algorithm TSP\n\nThis is an application demonstrating\nhow the travelling salesman problem\nworks to run it select the run button\nin the menu.")
        tkinter.mainloop() 


		#window.mainloop()


    def Run(self):
    	main()




''' root window created. Here, that would be the only window, but
 you can later have windows within windows.'''

root = Tk()# Creating the window
root.geometry("400x250")# Defining and setting the dimesions of the window/client
#root['background']='#856ff8'
#creation of an instance
app = Window(root)


#mainloop 
root.mainloop()  
