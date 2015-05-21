from game import Game
from player import WhitePlayerStub, BlackPlayerStub

__author__ = 'jkordas'

player1 = WhitePlayerStub()
player2 = BlackPlayerStub()

game = Game(player1, player2)
game.start()
