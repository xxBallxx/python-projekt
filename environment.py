class SimpleTile():
    """Einfache Plattform für die Umgebung in der der Spieler sich bewegt"""

    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def getUpperEdge(self):
        return self.posY-300
    
    def getSideEdge(self):
        return self.posX
    
    
    

    
