import sys
import pygame

class Alien_Invasion:# a class to manage game resource and behaviors
    def __init__(self):# init the game
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien_Invasion")

    def run_game(self):
        while True:

