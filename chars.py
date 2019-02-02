# import the pygame module
import pygame
# import random for random numbers!
import random
# import pygame.locals for easier access to key coordinates
from pygame.locals import *

WHITE = (255, 255, 255)

class Car(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        #self.image = pygame.Surface([width, height])
        #self.image.fill(WHITE)
        #self.image.set_colorkey(WHITE)

        # Draw the car (a rectangle!)
        #pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Instead we could load a proper pciture of a car...
        #self.image = pygame.Surface([width, height])
        self.image = pygame.image.load("banana.png").convert()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def update(self, keys):
        if keys[K_UP]:
            self.rect.move_ip(0, -5)
        if keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 1080:
            self.rect.right = 1080
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 720:
            self.rect.bottom = 720
