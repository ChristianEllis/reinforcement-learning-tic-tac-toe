from board_state import State

class TicTacToe(object):
  @staticmethod
  def is_game_over(state_hash_key):
    ''' Desc: returns player winner (1 or 2), 0 if no winner, or -1 if draw
    '''
    state = State.hash_to_state(state_hash_key) # convert state_hash_key to state object
    
    for i in range(3):
      if state[i][0] != 0 and state[i][0] == state[i][1] and state[i][0] == state[i][2]: # Check for horizontal win
        return state[i][0]

      if state[0][i] != 0 and state[0][i] == state[1][i] and state[0][i] == state[2][i]: # Check for vertical win
        return state[0][i]

    if state[0][0] != 0 and state[0][0] == state[1][1] and state[0][0] == state[2][2]: # Check for diagonal win
      return state[0][0]

    if state[0][2] != 0 and state[0][2] == state[1][1] and state[0][2] == state[2][0]:  # Check for secondary diagonal win
      return state[0][2]

    # if no winner thus far, and empty spots remain - there is no winner
    for i in range(3):
      for j in range(3):
        if state[i][j] == 0:
          return 0
    
    # else no free spots remain, it is a draw
    return -1
