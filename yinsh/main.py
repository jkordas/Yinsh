"""
Game starter module
"""
from yinsh.game_logic.game import Game
from yinsh.utils.player import PLAYER_TYPE, Player


def main():
    """
    Main program function - use to start the game
    :return:
    """
    player1 = Player("White", PLAYER_TYPE['WHITE'])
    player2 = Player("Black", PLAYER_TYPE['BLACK'])

    game = Game(player1, player2)
    game.start()


if __name__ == '__main__':
    main()
