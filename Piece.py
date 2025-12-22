class Piece():
    def __init__(self, hasBomb):
        self.hasBomb = hasBomb
        self.clicked = False
        self.flagged = False

    def getHasBomb(self):
        return self.hasBomb

    def setHasBomb(self, hasBomb):
        self.hasBomb = hasBomb

    def getClicked(self):
        return self.clicked

    def getFlagged(self):
        return self.flagged

    def setNeighbors(self, neighbors):
        self.neighbors = neighbors
        self.setNumberAround()
    def getNumberAround(self):
        return self.numberAround

    def setNumberAround(self):
        self.numberAround = 0
        for piece in self.neighbors:
            if (piece.getHasBomb()):
                self.numberAround += 1

    def toggleFlag(self):
        self.flagged = not self.flagged

    def click(self):
        self.clicked = True

    def getNeighbors(self):
        return self.neighbors

    def getIndex(self):
        self.index

    def setIndex(self, index):
        self.index = index