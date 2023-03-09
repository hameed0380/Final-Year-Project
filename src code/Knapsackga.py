import random
import pygame
import time

# Constants
ITEMS = []
CAPACITY = 0
POPULATION_SIZE = 50
NUM_GENERATIONS = 100
MUTATION_PROBABILITY = 0.1

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Pygame initialization
pygame.init()
SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Knapsack Problem")

# Item class
class Item:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight
