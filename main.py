from Game import Game
from Board import Board

board = Board((10, 10))
screenSize = (800, 800)
game = Game(board, screenSize)
game.run()