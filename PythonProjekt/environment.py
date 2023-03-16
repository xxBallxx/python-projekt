import pygame

pygame.init()
class SimpleTile():
    """Einfache Plattform für die Umgebung in der der Spieler sich bewegt"""

    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def getUpperEdge(self):
        return self.posY-300
    
    def getSideEdgeRight(self):
        return self.posX+60
    
    def getSideEdgeLeft(self):
        return self.posX-100

def createRow(startX, yCoordinate, howManyTiles, allTileList):

    rowList = []
    for x in range(howManyTiles):
        rowList.append(SimpleTile(startX, yCoordinate))
        if allTileList != None:
            allTileList.append(SimpleTile(startX, yCoordinate))
        startX += 100


def drawTiles(tileList, pygameDisplay, tileImage):
    
    for x in tileList:
        pygameDisplay.blit(tileImage,(x.posX, x.posY))

    
