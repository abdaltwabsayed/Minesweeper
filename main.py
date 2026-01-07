import os
import pygame
from Board import Board
from Button import Button
from Game import Game
# 1. Initialize Pygame
pygame.init()

# 2. Set the window dimensions (width, height)
width = 800
height = 600

screen = pygame.display.set_mode((width, height))

# 3. Set the window title (optional)
timer = pygame.time.Clock()
image_path = os.path.join(os.path.dirname(__file__), "images", "logo.png")
logo = pygame.image.load(image_path).convert_alpha()
pygame.display.set_icon(logo)
pygame.display.set_caption("Minesweeper")
def start(screenSize, boardSize, auto):
    while running:
            startButton.draw('light green')
            sound = pygame.mixer.Sound("minecraft-click-cropped.mp3")
            sound.play()
            prob = 0.2
            board = Board(boardSize, prob)
            game = Game(board, screenSize, auto)
            game.run()
            break
# 4. The Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    WIN = (width, height)
    image_path = os.path.join(os.path.dirname(__file__), "images", "background.png")

    background = pygame.image.load(image_path).convert_alpha()
    background = pygame.transform.smoothscale(background, WIN)
    screen.blit(background, (0, 0))
    startButton = Button(screen, "Play", 0.37 * width, 0.8 * height, 250, 50, 36, 'green')
    autoButton = Button(screen, "Auto Solve", 0.4 * width, 0.6 * height)
    hardButton = Button(screen, "Hard", 0.4 * width, 0.4 * height)
    mediumButton = Button(screen, "Medium", 0.4 * width, 0.3 * height)
    easyButton = Button(screen, "Easy", 0.4 * width, 0.2 * height)
    pygame.display.flip()
    screenSize = (800, 800)
    boardSize = (9, 9)
    auto = False
    if easyButton.check_clicked():
        easyButton.changeColor('gray')
        screenSize = (800, 800)
        boardSize = (9, 9)
    elif mediumButton.check_clicked():
        mediumButton.changeColor('gray')
        screenSize = (1423, 1423)
        boardSize = (16, 16)
    elif hardButton.check_clicked():
        hardButton.changeColor('gray')
        screenSize = (2667, 1423)
        boardSize = (30, 16)
    if autoButton.check_clicked():
        autoButton.changeColor('gray')
        auto = True
    if startButton.check_clicked():
        start(screenSize, boardSize, auto)
    else: continue
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()
pygame.quit()
