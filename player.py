import pygame
class Player():
    """ Klasse die Variablen und Konstanten des Spielers 
        beinhaltet """
    movesRight = False
    movesLeft = False
    isStanding = True

    def __init__(self, positionX, positionY):
        self.positionX = positionX
        self.positionY = positionY

    def moveX(self, addX):
        self.positionX = self.positionX + addX
        if addX > 0:
            self.isStanding = False
            self.movesLeft = False
            self.movesRight = True
        else:
            self.isStanding = False
            self.movesRight = False
            self.movesLeft = True

    def moveY(self, addY):
        self.positionY = self.positionY + addY

    def defaultPosition(self):
        self.movesRight = False
        self.movesLeft = False
        self.movesDown = False
        self.isStanding = True

    def gravitation(self, yValue):
        self.positionY += yValue
    
