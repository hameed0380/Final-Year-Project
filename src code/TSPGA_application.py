import pygame
import random
import math
import sys
import time

#  initiate
pygame.init()

# Colour presets
bg_colour = (51, 51, 51)  # set bg colour (grey)
white = (240, 240, 240) # colour used
red = (255, 0, 0) # colour used

# Used in the actual calculation and is a determinant factor
(width, height) = (500, 500) # window created with set width and height


screen = pygame.display.set_mode((width, height)) # set screen size
pygame.display.set_caption('TSP Genetic Algorithm') # Sets title of screen
#screen.fill(bg_colour)

# set values
totalCities = 15
pop_size = 5000
nxt_gen = 0.5
font = pygame.font.SysFont('Calibri', 15, True, False) # Font used to draw text on the screen (size 15)


# For the TSP a gene in this case would be a city with its coordinates(x, y).
# The x and y represent the coordinates for the city.
# n is a label that represents each city
class City:
   def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.node = n
        self.text = font.render("City: " + str(self.node), False, red)

   # Drawing each point onto the screen
   def display(self):
         pygame.draw.circle(screen, (red), (self.x, self.y), 5)


# Fitness class to find the routes
# The distance of the route
class FitnessFunc:
   def __init__(self):
      # generate path for each city
      self.route = random.sample(list(range(totalCities)), totalCities)
      self.distance = 0

   # Draw lines connecting each point to be traversed
   def display(self):
     for n, cityNum in enumerate(self.route):
         pygame.draw.line(screen, (white), (c_list[self.route[n]].x, c_list[self.route[n]].y), \
                         (c_list[self.route[n-1]].x, c_list[self.route[n-1]].y))


   # Calculates the Euclidean distance between 2 points (cities)
   # Decided from research this was the best metric for distance
   def calcDistance(self):
      distance = 0
      for n, cityNum in enumerate(self.route):
         distance += math.sqrt((c_list[self.route[n]].x - c_list[self.route[n-1]].x)**2 + \
                                 (c_list[self.route[n]].y - c_list[self.route[n-1]].y)**2)
      self.distance = distance
      return distance



# Carries out ranking -> looking at best(elitism) 
# Sorts the population according to the fitness function, which is the route's distance
def rank():
   global population
   # will sort the nested list based on the result of the lambda function
   population.sort(key = lambda x : x.distance, reverse = False)
   return


# selects best percentage of population and produce new generation
# Uses similar principle of crossover in TSPGA 
# Creates a new population from the top of a previous generation, replacing any non-essential individuals with the new ones.
def crossover():
   global population
   updatedPop = []
   updatedPop.extend(population[: int(pop_size*nxt_gen)])

   for n in range(pop_size - len(updatedPop)):
     index1 = random.randint(0, len(updatedPop) - 1)
     index2 = random.randint(0, len(updatedPop) - 1)
     while index1 == index2:
         index2 = random.randint(0, len(updatedPop) - 1)

     # gene from parents set to random index used from above i.e use of random lib    
     parent_a = updatedPop[index1]
     parent_b = updatedPop[index2]
     p = random.randint(0, totalCities - 1)
     Offspring = FitnessFunc()
     Offspring.route = parent_a.route[:p]
     
     notInOffspring = [item for item in parent_b.route if not item in Offspring.route]
     Offspring.route.extend(notInOffspring)
     updatedPop.append(Offspring)
   population = updatedPop
   return

# For each cities coordinate use the width and height of screen 
# 50, -50 intervals is used to be able to show the cities -> tested
c_list = [City(random.randint(50, width - 50), random.randint(50, height - 50), n) for n in range(totalCities)] 
population = [FitnessFunc() for n in range(pop_size)]

def main():
   global population
   running = True
   iter = 0

   # select the best
   best = random.choice(population)
   FinalDistance = best.calcDistance()
   clock = pygame.time.Clock()

   # Event Processing 
   # Instruction Page Loop 
   while True:
      best.display()
      if iter >= pop_size - 1:
         break
      # Limit to 60 frames per second
      clock.tick(60)
      pygame.display.update()
      screen.fill((bg_colour))
      # coordinates randomly generated
      for city in c_list:
         # Displays the cities
         city.display()
         screen.blit(city.text, (city.x, city.y))
         
      for element in population:
         element.calcDistance()

      # Carries out other processes
      rank()
      crossover()

      for element in population:
         if element.distance < FinalDistance:
             FinalDistance = element.calcDistance()
             best = element
         elif element.distance == FinalDistance:
             iter += 1

      # Display final path
      # Render the text. "True" means anti-aliased text.
      text = font.render("Final distance: "+str(FinalDistance), True, red, white)
      textRect = text.get_rect()
      screen.blit(text, textRect)

      # exit window
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
             pygame.quit() # End pygame
             sys.exit()


   print("The Final distance is: ", (FinalDistance))
   print("Predicted Path: ", (best.route))
   best.display()
   pygame.display.update()
   time.sleep(10)

if __name__ == "__main__":
    main()

# Full implemetation could not be carried out due to time constraint
# Although I did try to use other methods I could not quite figure out how to link them together
# Overall creating pygame was much better then trying to create visual in tkiner
# Fitness function and crossover are the main processes that need to be encoded
