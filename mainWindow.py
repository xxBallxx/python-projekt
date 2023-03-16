import pygame
from environment import *
from playerPy import *

pygame.init()

window = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Jump 'n' Run")
playerStanding = pygame.image.load('images/playerStandingFront.png').convert_alpha()
playerMovingRight = pygame.image.load('images/playerMovingRight.png').convert_alpha()
playerMovingLeft = pygame.image.load('images/playerMovingLeft.png').convert_alpha()
playerJumping = pygame.image.load('images/playerJumpingFront.png').convert_alpha()
playerDuck = pygame.image.load('images/playerDuck.png').convert_alpha()
tile = pygame.image.load('images/tile.png').convert_alpha()
# initializes the Player
ALLTILES = []
person = Player(10, 10)
gravitation = 5
tile1 = SimpleTile(10,500)
tile2 = SimpleTile(110,500)

row1 = createRow(410, 700, 3, ALLTILES)
row2 = createRow(610, 300, 3, ALLTILES)

ALLTILES.append(tile1)
ALLTILES.append(tile2)
#ALLTILES.append(row1)

pygame.display.update()
isRunning = True

while isRunning:
    
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            isRunning = False   

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and person.positionX > 0:
        person.moveX(-10)
    if keys[pygame.K_RIGHT] and person.positionX < 1050:
        person.moveX(10)
    if keys[pygame.K_SPACE] and person.positionY > 0:
        person.moveY(-10)
    if keys[pygame.K_DOWN]:
        person.moveY(0)
    
    

    window.fill((255, 255, 255))
    window.blit(tile, (tile1.posX, tile1.posY))
    window.blit(tile, (tile2.posX, tile2.posY))

    visualizeRow(row1, window, tile)
    visualizeRow(row2, window, tile)

    if person.isStanding:
        window.blit(playerStanding, (person.positionX, person.positionY))
    if person.movesRight:
        window.blit(playerMovingRight, (person.positionX, person.positionY))
    if person.movesLeft:
        window.blit(playerMovingLeft, (person.positionX, person.positionY))
    if person.movesDown:
        window.blit(playerDuck, (person.positionX, person.positionY))
    gravitation = 5
    
    for x in range(len(ALLTILES)):
        if person.positionY == ALLTILES[x].getUpperEdge() and person.positionX > ALLTILES[x].getSideEdgeLeft() and person.positionX < ALLTILES[x].getSideEdgeRight():
            gravitation = 0  

    person.gravitation(gravitation)
    
    
    pygame.display.update()




pygame.quit()



