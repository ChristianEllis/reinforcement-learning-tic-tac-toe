# Custom Imports
from game import TicTacToe
from board_state import State

class Human(object):
  def __init__(self, player):
    self.player = player

  def chose_action(self, board_state_hash):
    state = State.hash_to_state(board_state_hash)
    action = ''
    while action == '':
      TicTacToe.print_board(state)
      action = input('Your move? i.e. x,y : ')
    return (int(action.split(',')[0]),int(action.split(',')[1]))

  def end_of_episode(self, winner, board_state_hash):
    state = State.hash_to_state(board_state_hash)
    TicTacToe.print_board(state)
    if winner == 0:
      print('Game over! It was a draw.')
    else:
      print('Game over! Winner: Player {0}'.format(winner))