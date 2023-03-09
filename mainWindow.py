import pygame
import playerPy
import environment

pygame.init()

window = pygame.display.set_mode((1200, 800))

pygame.display.set_caption("Jump 'n' Run")
playerStanding = pygame.image.load('images/playerStandingFront.png').convert_alpha()
playerMovingRight = pygame.image.load('images/playerMovingRight.png').convert_alpha()
playerMovingLeft = pygame.image.load('images/playerMovingLeft.png').convert_alpha()
playerJumping = pygame.image.load('images/playerJumpingFront.png').convert_alpha()
# initializes the Player

person = playerPy.Player(10, 10)
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
    
    elif keys[pygame.K_RIGHT] and person.positionX < 1200:
        person.moveX(10)
    elif keys[pygame.K_SPACE]:
        person.moveY(-10)
    elif keys[pygame.K_DOWN]:
        person.moveY(10)
    elif True:
        person.defaultPosition()
    
    

    window.fill((255, 255, 255))
    if person.isStanding:
        window.blit(playerStanding, (person.positionX, person.positionY))
    if person.movesRight:
        window.blit(playerMovingRight, (person.positionX, person.positionY))
    if person.movesLeft:
        window.blit(playerMovingLeft, (person.positionX, person.positionY))

    person.gravitation(1)

    pygame.display.update()




pygame.quit()



