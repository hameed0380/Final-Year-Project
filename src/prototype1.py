# Import everything from tkinter and the font module
import tkinter
import tkinter.messagebox
import pygame
from TSPGA_application import main

class TSPGAGUI(tkinter.Frame):
    """Class representing the GUI for the TSPGA simulation"""

    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.master = master
        self._init_window()
    
    def _init_window(self):
        """Initialize the GUI window with widgets"""
        self.master.title("TSP Genetic Algorithm")
        self.pack(fill=tkinter.BOTH, expand=1)
        
        # Add a title label
        title_label = tkinter.Label(
            self, text="Travelling Salesman Problem", font=("Helvetica", 16)
        )
        title_label.pack(pady=20)

        # Add a menu bar
        menu = tkinter.Menu(self.master, tearoff=False)
        self.master.config(menu=menu)

        # Create the Simulator object
        simulator_menu = tkinter.Menu(menu)
        menu.add_command(label="Simulator", command=self.run)

        # Create the help_centre object
        help_menu = tkinter.Menu(menu)
        menu.add_command(label="Info", command=self.help)

        # Button to close the window
        button = tkinter.Button(self.master, text="Force Quit", command=self.quit)
        button.pack(pady=50)

    # Show information about the TSP Genetic Algorithm
    def help(self):
        """Open a window with information about TSPGA"""
        help_window = tkinter.Tk()
        help_window.geometry("400x250")
        help_window.config(bg="#856ff8")
        text = tkinter.Text(
            help_window, height=10, width=40, font=("Helvetica", 12),
            bg="#856ff8", fg="white")
        text.pack()
        text.insert(
            tkinter.END, 
            "Genetic Algorithm TSP\n\nThis is an application demonstrating\n"
            "how the travelling salesman problem\nworks. To run it, select the "
            "Simulator\noption in the menu."
        )
        help_window.mainloop()

    def run(self):
        """Run the main function from the TSPGA_application module"""
        main()

''' root window created. Here, that would be the only window, but
 you can later have windows within windows.'''

# Create the root GUI window
if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry("400x250")
    app = TSPGAGUI(root)
    root.mainloop()
