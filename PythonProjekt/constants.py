import pygame

window = pygame.display.set_mode((1200, 800))

pngPlayerStanding = pygame.image.load('images/playerStandingFront.png').convert_alpha()
pngPlayerMovingRight = pygame.image.load('images/playerMovingRight.png').convert_alpha()
pngPlayerMovingLeft = pygame.image.load('images/playerMovingLeft.png').convert_alpha()
pngPlayerJumping = pygame.image.load('images/playerJumpingFront.png').convert_alpha()
pngTile = pygame.image.load('images/tile.png').convert_alpha()
#pngBackground = pygame.image.load('images/background.png').convert_alpha()

ALLTILES = []
gravitation = 5
