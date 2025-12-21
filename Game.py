import os
import pygame

class Game():
    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        self.pieceSize = self.screenSize[0] // self.board.getSize()[1], self.screenSize[1] // self.board.getSize()[0]
        self.loadImages()

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw()
            pygame.display.flip()    
        pygame.quit()
    
    def draw(self):
        topleft = (0, 0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.board[row][col]
                if piece is not None:
                    image = self.images['empty-block']
                    self.screen.blit(image, topleft)
                topleft = (topleft[0] + self.pieceSize[0], topleft[1])
            topleft = (0, topleft[1] + self.pieceSize[1])

    def loadImages(self):
        self.images = {}
        for file in os.listdir('images'):
            if not file.endswith('.png'):
                continue
            path = r'images/{file}'
            image = pygame.image.load(path)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[file.split('.')[0]] = image