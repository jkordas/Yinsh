"""
Module to start game with stub player instances - test purpose
"""
from yinsh.game_logic.game import Game
from yinsh.utils.player import WhitePlayerStub, BlackPlayerStub


def main():
    """
    Main demo run function
    :return:
    """
    player1 = WhitePlayerStub()
    player2 = BlackPlayerStub()

    game = Game(player1, player2)
    game.start()


if __name__ == '__main__':
    main()
