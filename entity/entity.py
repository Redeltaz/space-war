from typing import List
import pygame
from pygame.surface import Surface

# Parent class, all entities must inherit from it
class Entity:
    pos_x: int = 0
    pos_y: int = 0
    img_width: int = 0
    img_height: int = 0
    image_size: Surface = None
    image: Surface = None
    _screen: Surface = None
    _angle: int = 0
    speed: int = 0
    
    def __init__(self, screen, img, width, height, pos_x, pos_y, speed):
        self.image = pygame.image.load(img).convert_alpha()
        self._screen = screen
        self.img_width = width
        self.img_height = height
        self.image_size = pygame.transform.scale(self.image, (width, height))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.draw_collider()
        
    def _draw_entity(self) -> None:
        """
        Draw entity properties
        """
        self.draw_collider()
        self._screen.blit(pygame.transform.rotate(self.image_size, self._angle), (self.pos_x, self.pos_y))
        
    def draw_collider(self):
        """
        Draw the rectangle that's use to see the colisions between objects
        """
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.img_width, self.img_height)