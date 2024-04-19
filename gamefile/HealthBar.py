import pygame
from settings import *
class healthbar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("health5.png")

    def render(self,display_surface):
        display_surface.blit(self.image, (10, 10))