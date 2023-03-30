import pygame
from environment import *
from player import *
import constants as c

pygame.init()

window = c.window
pygame.display.set_caption("Jump 'n' Run")

# initializes the Player

person = Player(10, 10)
gravitation = 10
jumping = False
onFloor = False
velocity = 10 
currentYPos = 0

#Creates the platforms
c.ALLTILES.append(SimpleTile(10,500)) 
c.ALLTILES.append(SimpleTile(110,500))
createRow(410, 700, 3, c.ALLTILES)
createRow(800, 500, 3, c.ALLTILES)
createRow(610, 300, 3, c.ALLTILES)


isRunning = True
while isRunning:
    
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            isRunning = False   

    keys = pygame.key.get_pressed()

    person.defaultPosition()
    if keys[pygame.K_LEFT] and person.positionX > 0:
        person.moveX(-10)
    if keys[pygame.K_RIGHT] and person.positionX < 1050:
        person.moveX(10)
    if keys[pygame.K_SPACE] and onFloor == True:
        jumping = True
        onFloor = False
        currentYPos = person.positionY
    
    if jumping:
        person.moveY(-velocity)
        velocity += 5
        if person.positionY <= currentYPos-300:
            velocity = 15
            jumping = False
    
    window.fill((255, 255, 255))
    #window.blit(c.pngBackground,(0,0))
    drawTiles(c.ALLTILES, window, c.pngTile)

    if person.isStanding:
        window.blit(c.pngPlayerStanding, (person.positionX, person.positionY))
    if person.movesRight:
        window.blit(c.pngPlayerMovingRight, (person.positionX, person.positionY))
    if person.movesLeft:
        window.blit(c.pngPlayerMovingLeft, (person.positionX, person.positionY))
    
    gravitation = 10
    for tile in c.ALLTILES:
        if person.positionY == tile.getUpperEdge() and person.positionX > tile.getSideEdgeLeft() and person.positionX < tile.getSideEdgeRight():
            gravitation = 0
            onFloor = True  

    person.gravitation(gravitation)
    
    #"Respawn"
    if person.positionY >= 1000:
        person.positionX = 10
        person.positionY = 10
    
    pygame.display.update()


pygame.quit()



