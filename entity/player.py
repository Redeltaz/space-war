import pygame
from pygame.surface import Surface

from .entity import Entity
from utils import get_screen_size

class Player(Entity):
    def player_key_event(self) -> None:
        """
        Handle Player key event
        """
        key = pygame.key.get_pressed()
        dist = self.speed
        full_x_screen, full_y_screen = get_screen_size(self._screen)
        
        if key[pygame.K_DOWN]:
            if full_y_screen <= (self.pos_y + self.img_height): return
            self.pos_y += dist
            self._angle = 180
        if key[pygame.K_UP]:
            if self.pos_y <= 0: return
            self.pos_y -= dist
            self._angle = 0
        if key[pygame.K_RIGHT]:
            if full_x_screen <= (self.pos_x + self.img_width): return
            self.pos_x += dist
            self._angle = 270
        if key[pygame.K_LEFT]:
            if self.pos_x <= 0: return
            self.pos_x -= dist
            self._angle = 90