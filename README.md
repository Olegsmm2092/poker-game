# PokerGame

This is a Python implementation of a simple Poker Game using Object-Oriented Programming and functions. The game allows up to 4 players and follows the standard rules of Texas Hold'em.

## Requirements
* Python 3.x
* pip

## Installation
1. Clone the repository:
````python
git clone https://github.com/Olegsmm2092/poker-game.git

````
Alternatively, you can download the zip file and extract it.

2. Install the required packages:

````python
pip install -r requirements.txt
````

## How to play

1. Run the app.py script:
````python
python app.py
````
2. Follow the instructions on the command line to start the game and make your moves.

## Design

The game is designed using Object-Oriented Programming principles and funcions. There are three main classes and 12 functions:

* player: Represents a player in the game. A player has a name, a stack of chips, and a hand of cards.

* Card: Represents a playing card. A card has a rank and a suit.

* FrenchDeck: Represents a deck of cards. A deck can be shuffled and cards can be dealt from it.

* main: Represents the game itself. The game has a list of players, a deck of cards, and manages the different phases of the game (preflop, flop, turn, and river).

## License
This project is licensed under the MIT License - see the LICENSE file for details.
