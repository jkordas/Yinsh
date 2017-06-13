# Yinsh Game Documentation
![yinsh](./res/yinsh.jpg "yinsh")

## Game description

YINSH is an abstract strategy board game by game designer Kris Burm. It is the fifth game to be released in the GIPF Project.

Short rules version: <br /> 
The players each start with 5 rings on the board. Every time a ring is moved, it leaves a marker behind.
Markers are white on one side and black on the other. When markers are jumped over by a ring they must be flipped,
so their color is constantly changing. The players must try to form a row of 5 markers with their own color face up.
If a player succeeds in doing so, he removes one of his rings as an indication that he has formed such a row.
The first player to remove 3 of his rings wins the game. In other words, each row you make brings you closer to 
victory-but also makes you weaker, because you have one less ring to play with. Very tricky!

[Extended online rules](http://www.gipf.com/yinsh/rules/rules.html)

## Project description

Whole game is displayed in text (ASCII) version. Two players make their moves alternately. Each move is preceded by
short note about current player, type of movement and allowable input.

### How to play

Game starts with short intro with title and players rings and markers symbols.<br />
![Intro](./res/intro.png "Intro")

Before each move board in current state is displayed. At the beginning it is empty board.<br />
![Board](./res/board.png "Board")

Board is followed by next movement note.<br />
![Single placement](./res/single_placement.png "Single placement")

After correct move input, appropriate symbol is placed at given position and board is redrawn.<br />
![Single placement result](./res/single_placement_result.png "Single placement result")

When each player place all rings on board, placement phase is finished.<br />
![Placement phase finished](./res/placement_phase_finished.png "Placement phase finished")

Then ring movement phase is continued until one of the players wins or all of markers are used.<br />
![Single ring move](./res/single_ring_move.png "Single ring move")

As long as given position is incorrect, player will be asked for new one.<br />
![Wrong position examples](./res/wrong_position_examples.png "Wrong position examples")

Black player completed a row of black markers.<br />
![Five in row completed](./res/five_in_row_completed.png "Five in row completed")

Row of five black markers is deleted.<br />
![Row deleted](./res/row_deleted.png "Row deleted")

Black players scores three points. Game is finished.<br />
![Game finished](./res/game_finished.png "Game finished")


### Code

Project consist of following classes:

game.py:

* Game - general game logic

board.py

* Board - specific board logic

player.py:

* Player - handles user input
* PlayerType - enum
* WhitePlayerStub - white player stub for demo purpose
* BlackPlayerStub - black player stub for demo purpose

move.py

*  PlacementMove - Ring placement move representation (first 5 moves)
*  RingMove - Ring movement representation (rest of the moves)

main.py - run typical game `python -m yinsh.main`<br />
demo.py - run test demo `python -m yinsh.demo`

All test included in test directory.<br />
Board class is covered with tests in 78%.<br />
Game class cannot be easily tested because of input needed from user.
Game demo file and player stubs was created to present basic game test.<br />
Pylint score: 10/10.
