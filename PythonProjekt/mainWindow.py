import pygame
from environment import *
from playerPy import *
import constants as c

pygame.init()

window = c.window
pygame.display.set_caption("Jump 'n' Run")

# initializes the Player

person = Player(10, 10)
c.gravitation = 5
c.ALLTILES.append(SimpleTile(10,500)) 
c.ALLTILES.append(SimpleTile(110,500))

createRow(410, 700, 3, c.ALLTILES)
createRow(610, 300, 3, c.ALLTILES)

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
    if keys[pygame.K_SPACE]:
        person.moveY(-10)

    
    window.fill((255, 255, 255))
    #window.blit(c.pngBackground,(0,0))
    drawTiles(c.ALLTILES, window, c.pngTile)

    if person.isStanding:
        window.blit(c.pngPlayerStanding, (person.positionX, person.positionY))
    if person.movesRight:
        window.blit(c.pngPlayerMovingRight, (person.positionX, person.positionY))
    if person.movesLeft:
        window.blit(c.pngPlayerMovingLeft, (person.positionX, person.positionY))
    
    c.gravitation = 5
    for tile in c.ALLTILES:
        if person.positionY == tile.getUpperEdge() and person.positionX > tile.getSideEdgeLeft() and person.positionX < tile.getSideEdgeRight():
            c.gravitation = 0  

    person.gravitation(c.gravitation)
    
    
    pygame.display.update()


pygame.quit()



