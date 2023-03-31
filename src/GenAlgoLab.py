# Import everything from tkinter and the font module
import tkinter
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.messagebox
from tkinter import ttk, PhotoImage
import subprocess


class TSPGAGUI(tkinter.Frame):
    """Class representing the GUI for the TSPGA simulation"""

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master, style="TFrame") # add style to frame
        self.master = master
        self.image = PhotoImage(file="noun-genetic-algorithm(CCBY3.0).png") # Genetic algorithm by Symbolon from <a href="https://thenounproject.com/browse/icons/term/genetic-algorithm/" target="_blank" title="Genetic algorithm Icons">Noun Project</a>
        self._init_window()
    
    def _init_window(self):
        """Initialize the GUI window with widgets"""
        self.master.title("Genetic Algorithm")
        self.pack(fill=tkinter.BOTH, expand=1)

        title_label = ttk.Label(
            self, text="GenAlgoLab", font=("Helvetica", 16)
        )
        title_label.pack(pady=20)

        # Add image
        image_label = ttk.Label(self, image=self.image)
        image_label.pack(pady=10)

        # Add a menu bar
        menu = tkinter.Menu(self.master, tearoff=False)
        self.master.config(menu=menu)

        # Create the CSP dropdown menu
        csp_menu = tkinter.Menu(menu, tearoff=False)
        menu.add_cascade(label="CSP", menu=csp_menu)

        # Add options to the CSP menu
        csp_menu.add_command(label="TSP", command=self.run_tsp)
        csp_menu.add_command(label="Knapsack", command=self.run_knapsack)
        csp_menu.add_command(label="Nqueen", command=self.run_nqueen)

        # Create the interactive gui object
        interactiveGA = tkinter.Menu(menu)
        menu.add_command(label="Interactive GA", command=self.run_interactiveGA)

        # Create the help_centre object
        help_menu = tkinter.Menu(menu)
        menu.add_command(label="Info", command=self.help)


        # Button to close the window
        button = ttk.Button(self.master, text="Force Quit", command=self.quit)
        button.pack(pady=50)


    def help(self):
        """Open a window with information about TSPGA"""
        # Create the root window
        help_window = tkinter.Tk()
        help_window.title("Instructions")

        # Add a Text widget with text
        instructions = (
            "Using the Program\n\n"
            "In the main window, click on the \"CSP\" menu item in the menu bar.\n"
            "A dropdown menu will appear with the following options: TSP, Knapsack, and Nqueen. Click on the desired option to run the corresponding genetic algorithm application.\n"
            "- TSP: Traveling Salesman Problem\n"
            "- Knapsack: Knapsack Problem\n"
            "- Nqueen: N-Queens Problem\n"
            "Each option will open a separate window running the selected genetic algorithm application.\n"
            "\n"
            "To run the Interactive Genetic Algorithm application, click on the \"Interactive GA\" menu item in the menu bar. A separate window will open running the interactive genetic algorithm application.\n"
            "\n"
            "For more information about the GenAlgoLab project and the Traveling Salesman Problem Genetic Algorithm, click on the \"Info\" menu item in the menu bar. A help window will open displaying information about the project.\n"
            "To close the main window and all open application windows, click on the \"Force Quit\" button in the main window."
        )
        text_widget = tkinter.Text(help_window, wrap=tkinter.WORD)
        text_widget.insert(tkinter.END, instructions)
        text_widget.config(state=tkinter.DISABLED)  # Make the text read-only
        text_widget.pack(padx=10, pady=10)

        # Run the main event loop
        help_window.mainloop()


    # By using the subprocess module I managed to stop the programs opening automatically as this was an ongoing issue

    def run_interactiveGA(self):
        """Run the main function from the TSPGA_application module"""
        subprocess.Popen(['python', 'gui.py'])

    def run_tsp(self):
        """Run the main function from the TSPGA_application module"""
        subprocess.Popen(['python', 'TSPGA_application.py'])

    def run_knapsack(self):
        """Run the main function from the Knapsack_application module"""
        subprocess.Popen(['python', 'Knapsackga.py'])

    def run_nqueen(self):
        """Run the main function from the Nqueen_application module"""
        subprocess.Popen(['python', 'queen_ga.py'])

def run_gui():
    # Create the root GUI window
    root = ThemedTk(theme="arc")
    root.geometry("600x400")
    app = TSPGAGUI(root)
    root.mainloop()


''' root window created'''

# Create the root GUI window
if __name__ == "__main__":
    run_gui()

# The structure of the GUI is a little bit different to other programs as I worked on it first to get an idea of how I wanted the program to work.
