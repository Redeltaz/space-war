import pygame
from random import randrange

from .entity import Entity

from utils.number import random_number
from utils import get_screen_size

class Asteroid(Entity):
    _spawn_place: str
    
    def __init__(self, screen, img, speed):
        spawn_place = randrange(4)
        
        full_x_screen, full_y_screen = get_screen_size(screen)
        random_x_pos = random_number(start=0, end=full_x_screen)
        random_y_pos = random_number(start=0, end=full_y_screen)
        random_width = random_number(start=50, end=200)
        random_height = random_number(start=50, end=200)
        
        if spawn_place == 0:
            # spawn on top
            x_pos = random_x_pos
            y_pos = 0 - random_height
            self._spawn_place = "top"
        elif spawn_place == 1:
            # spawn on right
            x_pos = full_x_screen + random_width
            y_pos = random_y_pos
            self._spawn_place = "right"
        elif spawn_place == 2:
            # spawn on bottom
            x_pos = random_x_pos
            y_pos = full_y_screen + random_height
            self._spawn_place = "bottom"
        elif spawn_place == 3:
            # spawn on left
            x_pos = 0 - random_width
            y_pos = random_y_pos
            self._spawn_place = "left"
        
        super().__init__(screen, img, random_width, random_height, x_pos, y_pos, speed)
        
    def asteroid_movement(self) -> None:
        """
        Define the movement of the asteroid
        """
        speed = self.speed
        
        if self._spawn_place == "top":
            self.pos_y += speed
        if self._spawn_place == "bottom":
            self.pos_y -= speed
        if self._spawn_place == "left":
            self.pos_x += speed
        if self._spawn_place == "right":
            self.pos_x -= speed
        
        self._draw_entity()

            
            