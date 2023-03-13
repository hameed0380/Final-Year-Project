# imports
from tkinter import *
import tkinter as tk
from tkinter import ttk

class GUI:
    """Class for the GUI process"""

    def __init__(self):
        self.root= tk.Tk()
        self.text = StringVar(self.root, "")
        self.root.geometry("800x600")
        self.root.title("Genetic algorithm Program")

        # Problem selection part
        self.problems = ['TSP']

        self.problem_frame = LabelFrame(self.root, text="Problems", width=260, height=190)
        self.define_label = Label(self.root, text='Choose problem:', justify='left')
        self.enter_prob = ttk.Combobox(self.root, values=self.problems)

        # Starting and stopping the process
        self.state = True
        self.start_button = Button(self.root, text='Start', width=10, height=2, command=self.start_genetic)
        self.stop_button = Button(self.root, text='Stop', width=10, height=2, command=self.stopping)

        # Population section
        self.population_frame = LabelFrame(self.root, text="Population", width=190, height=100)
        self.population_label = tk.Label(self.root, text='Population size:')
        self.population_num = IntVar()
        self.population_number = Spinbox(self.root, from_=0, to=100, textvariable=self.population_num)

        # Crossover section
        self.crossover_frame = LabelFrame(self.root, text="Crossover", width=190, height=100)
        self.crossover_label = Label(self.root, text="Crossover rate")
        self.crossover_probability = DoubleVar()
        self.crossover_number = Entry(self.root, textvariable=self.crossover_probability)

        # Mutation section
        self.mutation_frame = LabelFrame(self.root, text="Mutation", width=190, height=100)
        self.mutation_label = Label(self.root, text="Mutation rate")
        self.mutation_probability = DoubleVar()
        self.mutation_number = Entry(self.root, textvariable=self.mutation_probability)




        # run window
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        """ The placement and font setting of all widgets."""
        self.problem_frame.place(x=0, y=0)
        self.define_label.config(font=("helvetica", 12))
        self.define_label.place(x=20, y=20)

        self.enter_prob.current(0)
        self.enter_prob.config(font=("helvetica", 10))
        self.enter_prob.place(x=20, y=45)

        # Stop and start button
        self.start_button.place(x=20, y=200)
        self.stop_button.place(x=110, y=200)

        # Population input
        self.population_frame.place(x=340, y=0)
        self.population_label.config(font=("helvetica", 10))
        self.population_label.place(x=360, y=20)

        self.population_num.set(50)
        self.population_number.place(x=363, y=45)

        # Crossover input
        self.crossover_frame.place(x=560, y=0)
        self.crossover_label.config(font=("helvetica", 10))
        self.crossover_label.place(x=570, y=20)

        self.crossover_probability.set(0.7)
        self.crossover_number.place(x=573, y=45)

        # Mutation input
        self.mutation_frame.place(x=340, y=120)
        self.mutation_label.config(font=("helvetica", 10))
        self.mutation_label.place(x=360, y=140)
        self.mutation_probability.set(0.01)
        self.mutation_number.place(x=363, y=170)


        

    def start_genetic(self):
        print("ga in progress")

    def stopping(self):
        print("stopped")

if __name__ == '__main__':
    gui = GUI()
