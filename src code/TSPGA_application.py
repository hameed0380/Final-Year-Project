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

