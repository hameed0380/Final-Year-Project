from tkinter import *
import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from ga import GenAlgorithm

class GUI:
    """Class for the GUI process"""

    def __init__(self):
        self.root= tk.Tk()
        self.text = StringVar(self.root, "")
        self.root.geometry("800x600")
        # self.root.configure(bg="lightblue")
        self.root.title("Genetic Algorithm Program")

        # Problem selection part
        self.problems = ['Rastrigin Function']

        self.problem_frame = LabelFrame(self.root, text="Problems", width=260, height=190)
        self.define_label = Label(self.root, text='Choose problem:', justify='left')
        self.enter_prob = ttk.Combobox(self.root, values=self.problems)

        # Starting and stopping the process
        self.start_button = Button(self.root, text='Start', width=10, height=2, command=self.run_ga)
        self.stop_button = Button(self.root, text='Stop', width=10, height=2, command=self.stopping)

        self.stop = False

        # Set max and min values
        self.min_x = -512
        self.max_x = 512

        # Population section
        self.population_frame = LabelFrame(self.root, text="Population", width=190, height=120)
        self.population_label = tk.Label(self.root, text='Population size:')
        self.population_num = IntVar()
        self.population_number = Spinbox(self.root, from_=0, to=100, textvariable=self.population_num)

        # Precision section
        self.precision_label = Label(self.root, text='Precision')
        self.precision = DoubleVar()
        self.precision_number = Entry(self.root, textvariable=self.precision)

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

        # num_iter section
        self.iteration_frame = LabelFrame(self.root, text="Iteration", width=190, height=100)
        self.iteration_label = Label(self.root, text="Iteration number")
        self.iteration = IntVar()
        self.iteration_number = Entry(self.root, textvariable=self.iteration)

        # Generation5
        self.gen_no = StringVar(self.root, "")
        self.gen_no.set("Generation: 1")
        self.current_gen = Label(self.root, textvariable=self.gen_no, justify='left')

        # Label for displaying the results
        self.result_label = Label(self.root, text="", justify='left', wraplength=400)

        # Creates 3d plot
        self.figure = plt.figure(figsize=(3, 3))
        self.axis = self.figure.add_subplot(111, projection="3d")

        # Creating a dictionary to map problem names to their corresponding objective functions and boundary values
        self.options_map = {
            self.problems[0]: ["20 + x1 * x1 - 10*np.cos(2 * np.pi * x1) + x2 * x2 -10 * np.cos(2 * np.pi * x2)", -5.12,
                              5.12]  
        } # Lower and upper boundary value for the variables x1 and x2


        # run window
        self.create_widgets()
        self.update_surface_plot()
        self.root.mainloop()

    def create_widgets(self):
        """ The placement and font setting of all widgets."""
        self.problem_frame.place(x=10, y=0)
        self.define_label.config(font=("helvetica", 12))
        self.define_label.place(x=20, y=20)

        # Section for entering problem (function)
        self.enter_prob.current(0)
        self.enter_prob.config(font=("helvetica", 10))
        self.enter_prob.place(x=20, y=45)

        self.enter_prob = ttk.Combobox(self.root, values=self.problems)
        self.enter_prob.bind("<<ComboboxSelected>>", self.update_surface_plot) # connecting a Tkinter Combobox widget to update_surface_plot


        # Stop and start button
        self.start_button.place(x=20, y=200)
        self.stop_button.place(x=110, y=200)

        # Population input
        self.population_frame.place(x=340, y=0)
        self.population_label.config(font=("helvetica", 10))
        self.population_label.place(x=360, y=20)

        self.population_num.set(50)
        self.population_number.place(x=363, y=45)

        # Precision
        self.precision_label.config(font=("helvetica", 10))
        self.precision_label.place(x=360, y=70)

        self.precision.set(0.01)
        self.precision_number.place(x=363, y=90)

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

        # Iterations input
        self.iteration_frame.place(x=560, y=120)
        self.iteration_label.config(font=("helvetica", 10))
        self.iteration_label.place(x=570, y=140)

        self.iteration.set(100)
        self.iteration_number.place(x=573, y=170)

        # Result label
        self.result_label.config(font=("helvetica", 12))
        self.result_label.place(x=400, y=250)

        self.current_gen.config(font=("helvetica", 12))
        self.current_gen.place(x=20, y=550)
        

    def run_ga(self):
        """Run the main loop of ga"""

        # Initialize the genetic algorithm with parameters retrieved from the GUI
        genetic = GenAlgorithm(2, self.population_num.get(), self.precision_number.get(),
                         self.crossover_probability.get(), self.mutation_probability.get(),
                         self.min_x, self.max_x, self.iteration.get())
        plot_points = []
        genetic.end, genetic.precision = genetic.bit_count()
        population = genetic.create_population() # Create the initial population
        objective_values = genetic.assess_population(genetic.objective_function, population, self.options_map[self.problems[self.enter_prob.current()]][0])

        best_individual, best_value = genetic.find_best(population, objective_values)
        best_parameters = genetic.binary_to_decimal(best_individual)

        # Initialize lists to store the best and mean objective values per generation
        best_values_list = [best_value]
        mean_values_list = [np.average(objective_values)]
        best_value_per_generation = [best_value]
        best_solution = 0

        # Decode the initial population
        decoded_population = []
        for individual in population:
            decoded_population.append(genetic.binary_to_decimal(individual))
        decoded_population = np.array(decoded_population)
        plot_points.append(decoded_population)

        # Main loop for the genetic algorithm
        for iteration in range(genetic.max_iterations):
            # Inorder to stop the program running
            if self.stop:
                self.stop = False
                break
            population = genetic.selection(population, objective_values)
            population = genetic.crossover(population, genetic.crossover_prob)
            population = genetic.mutation(population, genetic.mutation_prob)
            objective_values = genetic.assess_population(genetic.objective_function, population,
                                            self.options_map[self.problems[self.enter_prob.current()]][0])
            decoded_coordinates = np.apply_along_axis(self.convert_binary_to_decimal, 1, population, genetic)
            plot_points_current = self.display_charts(decoded_coordinates, objective_values)
            for point in plot_points_current:
                point.remove()
            current_min_value = np.min(objective_values)
            best_value_per_generation.append(current_min_value)
            if current_min_value < best_value:
                best_value = current_min_value
                best_solution = iteration
                best_parameters = genetic.binary_to_decimal(population[np.argmin(objective_values)])
                self.result_text = f"Minimum value: {round(best_value, 2)}\nAt: {np.around(best_parameters, 2)}\nIn generation number: {best_solution + 1}"
                self.result_label.config(text=self.result_text)
            best_values_list.append(best_value)
            mean_values_list.append(np.average(objective_values))
            if iteration == genetic.max_iterations / 2 or iteration == genetic.max_iterations - 1:
                decoded_population = []
                for individual in population:
                    decoded_population.append(genetic.binary_to_decimal(individual))
                decoded_population = np.array(decoded_population)
                plot_points.append(decoded_population)
            self.gen_no.set(f"Generation: {iteration + 1} / {genetic.max_iterations}")

        # Return the results and data for further processing
        return best_value, best_solution, best_parameters, best_values_list, best_value_per_generation, mean_values_list, plot_points

    def display_charts(self, x_values, obj_values):
        """Plotting charts"""
        # Initialize empty list to store the plotted points
        plotted_points = []
        # Loop through the objective values and plot the corresponding points
        for idx, j in enumerate(obj_values):
            plotted_points.append(self.axis.scatter(x_values[idx][0], x_values[idx][1], j, color='#1f77b4', s=6))
        self.figure.canvas.draw() # Redraw canvas and update the GUI
        self.root.update()
        return plotted_points

    @staticmethod
    def convert_binary_to_decimal(population, genetic_algo_instance):
        # convert binary to decimal
        decimal_values = GenAlgorithm.binary_to_decimal(genetic_algo_instance, population)
        return decimal_values
        
    def update_surface_plot(self, *args):
        """Updating the plot"""
        actual_fun = self.options_map[self.problems[self.enter_prob.current()]]

        # Set the new minimum and maximum x values for the selected function
        self.min_x = actual_fun[1]
        self.max_x = actual_fun[2]

        plt.ion() # Enables interactive mode for the plot
        self.axis.clear() # clears the current plot

        points = np.linspace(self.min_x, self.max_x, 50)
        x, y = np.meshgrid(points, points) # creates a meshgrid of x and y points which will be used to compute z values for the surface plot
        # compute z values for each (x, y) pair using the function and stores them in the z matrix
        z = np.zeros((len(points), len(points)))
        for i in range(len(points)):
            for j in range(len(points)):
                z[i, j] = GenAlgorithm.objective_function((x[i, j], y[i, j]), actual_fun[0])

        # a surface plot using the x, y, and z values
        self.axis.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis',
                            linewidth=0.3, antialiased=True, alpha=0.5)
        self.axis.view_init(30, 200)

        canvas_ = FigureCanvasTkAgg(self.figure, self.root) # create object which is a canvas to be placed in tk window
        canvas_.get_tk_widget().place(x=20, y=250)


    # Clears and stops the plot
    def stopping(self):
        """Clear the plot and stop the GA execution when the stop button is pressed."""
        self.stop = True
        self.axis.clear()
        self.figure.canvas.draw()
        self.root.update()



if __name__ == '__main__':
    gui = GUI()
