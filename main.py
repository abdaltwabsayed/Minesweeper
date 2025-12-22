from Board import Board
from Game import Game

prob =0.2
board = Board((9, 9), prob)
screenSize = (800, 800)
game = Game(board, screenSize)
game.run()