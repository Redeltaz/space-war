#!/usr/bin/env python3

import pygame

from typing import Dict, List
from pygame.constants import MOUSEBUTTONDOWN
from pygame.event import Event
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from entity import Player, Asteroid

from utils import get_screen_center

class Game:
    _state: str = "start"
    _screen_width: int = 0
    _screen_height: int = 0
    _screen: Surface = None
    _icon: Surface = None
    _background: Surface = None
    _is_game_running: bool = False
    _player: Player
    _asteroids: List[Asteroid] = []
    _life_remaining: int = 3
    _font: Font = None
    
    def __init__(self, width, height) -> None:
        self._screen_width = width
        self._screen_height = height
        self._init_screen()
        
    def _init_screen(self) -> None:
        """
        Initialization of all screen properties 
        """
        pygame.init()
        
        self._screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self._screen = pygame.display.set_mode((self._screen_width, self._screen_height))
        pygame.display.set_caption("Space War")
        
        self._icon = pygame.image.load("./assets/invader.png").convert()
        pygame.display.set_icon(self._icon)
        
        self._background = pygame.image.load("./assets/background.png")
        
    def stop_game(self) -> None:
        """
        Stop the game
        """
        self._is_game_running = False
        
    def _key_event(self, event: Event) -> None:
        """
        Handle all pygame key events 
        """     
        if event.type == pygame.QUIT:
            self.stop_game()
            
    def _add_player(self) -> None:
        """
        Add a new player
        """
        x_center, y_center = get_screen_center(self._screen)
        width_player, height_player = 70, 70
        x_center -= width_player / 2
        y_center -= height_player / 2
        
        player = Player(
            screen=self._screen, 
            img="./assets/spaceship.png", 
            width=width_player, 
            height=height_player, 
            pos_x=x_center, 
            pos_y=y_center,
            speed=3
        )

        self._player = player

    def _add_asteroid(self) -> None:
        """
        Add new asteroid
        """
            
        asteroid = Asteroid(
            screen=self._screen, 
            img="./assets/asteroid.png",
            speed=self._parameters["asteroid_speed"]
        )
        
        if len(self._asteroids) == self._parameters["asteroid_limit"]:
            del self._asteroids[0]
            
        self._asteroids.append(asteroid)
            
        print("NEW ASTEROID")
        
    def _display_life(self) -> None:
        """
        See life remaining
        """
        font = pygame.font.SysFont("Arial", 30)
        life = font.render(f"LIFE : {self._life_remaining}", True, (255, 255, 255))
        self._screen.blit(life, (10, 10))
        
    def _starting_screen(self) -> None:
        """
        Display starting screen
        """
        x_center, y_center = get_screen_center(self._screen)
        
        font = pygame.font.SysFont("Arial", 30)
        text = font.render("Start the Game", True, (255, 255, 255)) 
        self._screen.fill([0, 0, 0])
        self._screen.blit(text, (int(x_center - text.get_width() / 2), int(y_center / 2)))
        
        easy_button = self._draw_button("EASY", 100, 400, 150, 75)
        normal_button = self._draw_button("NORMAL", 300, 400, 150, 75)
        hard_button = self._draw_button("HARD", 500, 400, 150, 75)
        impossible_button = self._draw_button("IMPOSSIBLE", 700, 400, 200, 75)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop_game()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if easy_button.collidepoint(event.pos):
                        self._state = "play"
                        self._parameters = {
                            "asteroid_speed": 1,
                            "asteroid_timeout": 20000,
                            "asteroid_limit": 5
                        }
                        
                    if normal_button.collidepoint(event.pos):
                        self._state = "play"
                        self._parameters = {
                            "asteroid_speed": 2,
                            "asteroid_timeout": 10000,
                            "asteroid_limit": 10
                        }
                        
                    if hard_button.collidepoint(event.pos):
                        self._state = "play"
                        self._parameters = {
                            "asteroid_speed": 3,
                            "asteroid_timeout": 500,
                            "asteroid_limit": 20
                        }
                        
                    if impossible_button.collidepoint(event.pos):
                        self._state = "play"
                        self._parameters = {
                            "asteroid_speed": 5,
                            "asteroid_timeout": 100,
                            "asteroid_limit": 30
                        }
        
    def _draw_button(self, text: str, coord_x: int, coord_y: int, width: int, height: int) -> Rect:
        """
        Draw a button
        """
        font = pygame.font.SysFont("Arial", 30)
        button = pygame.draw.rect(self._screen, (255, 255, 255), (coord_x, coord_y, width, height), 5)
        text = font.render(text, True, (255, 255, 255))
        self._screen.blit(text, button)
        
        return button
            
    def start_game(self) -> None:
        """
        Start the game
        """
        self._is_game_running = True
        self._screen.fill([255, 255, 255])
        self._add_player()
        
        nb_ticks_start = pygame.time.get_ticks()

        while self._is_game_running:
            
            if self._state == "start":
                self._starting_screen()
            elif self._state == "play":
                nb_ticks_now = pygame.time.get_ticks()
                self._screen.blit(self._background, (0, 0))
                
                self._display_life()
                
                for event in pygame.event.get():
                    self._key_event(event)
                    
                self._player.player_key_event()
                
                self._player._draw_entity()
                
                if nb_ticks_now - nb_ticks_start > self._parameters["asteroid_timeout"]:
                    nb_ticks_start = nb_ticks_now
                    self._add_asteroid()
                    
                for index, asteroid in enumerate(self._asteroids):
                    asteroid.asteroid_movement()
                    
                    if asteroid.rect.colliderect(self._player.rect):
                        del self._asteroids[index]
                        print("HURTED")
                        self._life_remaining -= 1
                        
                        if self._life_remaining == 0:
                            self.stop_game()

                    
                    
            pygame.display.update()
            
        pygame.quit()
        
        
space_game = Game(1000, 700)
        

if __name__ == "__main__":
    space_game.start_game()