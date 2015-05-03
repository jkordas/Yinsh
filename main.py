from game import Game
from player import Player

__author__ = 'jkordas'


player1 = Player("White-player")
player2 = Player("Black-player")

game = Game(player1, player2)
game.start()