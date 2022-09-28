from .component import Component
from .bouncingmovementcomponent import *
import pygame

class GameOverComponent(Component):
    def __init__(self, assetFileName, name, actor):
        super().__init__(name, actor)
        self.assetFileName = assetFileName
        global counter
        self.image = None

    def load(self):
        self.image = pygame.image.load(self.assetFileName)
        
            
    def render(self, surface):
        if len(counter)<1 and self.image != None:
            rect = self.image.get_rect()
            rect.centerx = self.owner.x
            rect.centery = self.owner.y
            surface.blit(self.image, rect)
      