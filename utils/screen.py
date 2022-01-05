from pygame.surface import Surface

def get_screen_center(screen: Surface) -> int:
    """
    Return the coordinates of the center of the screen
    """
    x = screen.get_width() / 2
    y = screen.get_height() / 2
    
    return x, y

def get_screen_size(screen: Surface) -> int:
    """
    Return the coordinates of the full screen
    """
    x = screen.get_width()
    y = screen.get_height()
    
    return x, y