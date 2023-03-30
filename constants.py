import pygame

#Game Fenster
window = pygame.display.set_mode((1200, 800))

#Grafiken
pngPlayerStanding = pygame.image.load('images/playerStandingFront.png').convert_alpha()
pngPlayerMovingRight = pygame.image.load('images/playerMovingRight.png').convert_alpha()
pngPlayerMovingLeft = pygame.image.load('images/playerMovingLeft.png').convert_alpha()
pngTile = pygame.image.load('images/tile.png').convert_alpha()

#Liste aller Tile Objekte
ALLTILES = []
