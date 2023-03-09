import pygame
import environment
import playerPy

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

person = playerPy.Player(10, 10)
tile1 = environment.SimpleTile(10,500)
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
    if person.isStanding:
        window.blit(playerStanding, (person.positionX, person.positionY))
    if person.movesRight:
        window.blit(playerMovingRight, (person.positionX, person.positionY))
    if person.movesLeft:
        window.blit(playerMovingLeft, (person.positionX, person.positionY))
    if person.movesDown:
        window.blit(playerDuck, (person.positionX, person.positionY))
    ball = 1
    
    if person.positionY >= tile1.getUpperEdge() and person.positionX > 0 and person.positionX < 10:
        ball = 0    

    person.gravitation(ball)
    
    #if person.positionY < 450:
    #    person.gravitation(1)
    

    pygame.display.update()




pygame.quit()



