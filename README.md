# reinforcement-learning-tic-tac-toe
An RL agent that learns to play Tic Tac Toe through value iteration. Inspired by Sutton and Barto's, "Reinforcement Learning - An Introduction". Can train an agent through self play, and then test that policy against a human. A human can directly play against an agent.

## Usage
1. Install requirements `pip install -r requirements.txt`
2. Run the program, `python main.py`

## Program Structure
This program was designed using OOP principles. A description of files is below.
- main.py - main program - run this from your terminal `python main.py`.
- board_state.py (class) - manages the state of a TicTacToe game.
- agent.py (class) - an autonomous agent that will make decisions based on a policy and learn through value iteration.
- human.py (class) - helper class so that a player may interact with the game.
- game.py (static class) - play the game, determines if a game is over, and prints board state to the console.

## Citing and Extending This Work
See LICENSE, if used for academic purposes, please cite this repository. Forks, & merge-requests are encouraged.
