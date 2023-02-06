# Import everything from tkinter and the font module
from tkinter import *
import tkinter.messagebox
import pygame


# Import the TSPGA_application module
from TSPGA_application import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # Initialize the window with widgets
    def init_window(self):
        self.master.title("TSP Genetic Algorithm")

        '''allowing the widget to take the full space of the root window
        so widgit is continuously shown even when root window has been changed
        in size'''

        self.pack(fill=BOTH, expand=1)

        title_label = Label(self, text="Travelling Salesman Problem", font=("Helvetica", 16))
        title_label.pack(pady=20)

        # Creating a menu instance
        menu = Menu(self.master, tearoff=False)
        self.master.config(menu=menu)

        # Create the Simulator object
        Simulator = Menu(menu)
        menu.add_command(label="Simulator", command=self.Run)

        # Create the help_centre object
        help_centre = Menu(menu)
        menu.add_command(label="Info", command=self.Help)

        # Button to close the window
        button_1 = Button(root, text="Force Quit", command=root.destroy)
        button_1.pack(pady=50)

    # Show information about the TSP Genetic Algorithm
    def Help(self): 
        root = tkinter.Tk()
        root.geometry("400x250")
        root.config(bg="#856ff8")
        T = tkinter.Text(root, height=10, width=40, font=("Helvetica", 12), bg="#856ff8", fg="white")
        T.pack()
        T.insert(tkinter.END, "Genetic Algorithm TSP\n\nThis is an application demonstrating\nhow the travelling salesman problem\nworks. To run it, select the Simulator\noption in the menu.")
        tkinter.mainloop()


    # Run the main function from the TSPGA_application module
    def Run(self):
        main()

''' root window created. Here, that would be the only window, but
 you can later have windows within windows.'''

# Create the root GUI window
root = Tk()
root.geometry("400x250")
app = Window(root)
root.mainloop()
