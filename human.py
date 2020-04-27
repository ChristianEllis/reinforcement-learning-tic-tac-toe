# Custom Imports
from game import TicTacToe

class Human(object):
  def __init__(self, player):
    self.player = player

  def action(self, state):
    TicTacToe.print_board(state)
    action = input('Your move? i.e. x,y : ')
    return (int(action.split(',')[0]),int(action.split(',')[1]))

  def episode_over(self, winner):
    if winner == 0:
      print('Game over! It was a draw.')
    else:
      print('Game over! Winner: Player {0}'.format(winner))