from game import Game
from player import Player, PlayerType


def main():
    player1 = Player("White", PlayerType.WHITE)
    player2 = Player("Black", PlayerType.BLACK)

    game = Game(player1, player2)
    game.start()


if __name__ == '__main__':
    main()