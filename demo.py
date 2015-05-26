from game import Game
from player import WhitePlayerStub, BlackPlayerStub


def main():
    player1 = WhitePlayerStub()
    player2 = BlackPlayerStub()

    game = Game(player1, player2)
    game.start()


if __name__ == '__main__':
    main()
