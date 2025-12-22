import os
import pygame
from time import sleep
from AStarSolver import AStarSolver
from Piece import Piece


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
            if (self.board.clickNumber == 0 and pygame.event.EventType.type == pygame.MOUSEBUTTONUP):
                position = pygame.mouse.get_pos()
                index = position[1] // self.pieceSize[1], position[0] // self.pieceSize[0]
                piece = self.board.getPiece(index)
                piece.setHasBomb(False)
                piece.click()
            self.board.setNeighbors()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position, rightClick)
                    # solver = AStarSolver(self.board)
                    # solver.move()
            self.draw()
            pygame.display.flip()
            # solver = AStarSolver(self.board)
            # solver.move()
            self.draw()
            if (self.board.getWon()):
                font = pygame.font.SysFont(None, 90)
                text = font.render("You Win!", True, (0, 255, 0), (255, 255, 255, 30))
                self.screen.blit(text, (0.29 * self.screenSize[0], 0.4 * self.screenSize[1]))
                pygame.display.flip()
                sound = pygame.mixer.Sound("win.wav")
                sound.play()
                sleep(3)
                running = False
            if (self.board.getLost()):
                for row in range(self.board.getSize()[0]):
                    for col in range(self.board.getSize()[1]):
                        piece = self.board.getPiece((row, col))
                        if piece.getHasBomb(): image = self.images["bomb-at-clicked-block"]
                        else: continue
                        self.screen.blit(image, (col * self.pieceSize[1], row * self.pieceSize[0]))
                font = pygame.font.SysFont(None, 90)
                text = font.render("Game Over", True, (255, 0, 0), (255, 255, 255, 30))
                self.screen.blit(text, (0.29 * self.screenSize[0], 0.4 * self.screenSize[1]))
                pygame.display.flip()
                sleep(5)
                break
        pygame.quit()
    
    def draw(self):
        topleft = (0, 0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece((row, col))
                piece.setIndex((row, col))
                image = self.getImage(piece)
                self.screen.blit(image, topleft)
                topleft = (topleft[0] + self.pieceSize[0], topleft[1])
            topleft = (0, topleft[1] + self.pieceSize[1])

    def loadImages(self):
        self.images = {}
        for file in os.listdir('images'):
            if not file.endswith('.png'):
                continue
            image = pygame.image.load(r"images/" + file)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[file.split('.')[0]] = image

    def getImage(self, piece):
        string = None
        if (piece.getClicked()):
            string = "bomb-at-clicked-block" if piece.getHasBomb() else str(piece.getNumberAround())
        else:
            string = "flag" if piece.getFlagged() else "empty-block"
        return self.images[string]

    def handleClick(self, position, rightClick):
        if (self.board.getLost()):
            return
        index = position[1] // self.pieceSize[1], position[0] // self.pieceSize[0]
        piece = self.board.getPiece(index)
        self.board.handleClick(piece, rightClick)
    def getScreen(self):
        return self.screen