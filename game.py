from board_state import State

class TicTacToe(object):
  '''
  Board layout for 3x3 Tic Tac Toe that will be printed out to the console when
  playing a human, or training in verbose mode.
  '''
  BOARD_FORMAT = '''
  ----------------------------
  | {0} | {1} | {2} |
  |--------------------------|
  | {3} | {4} | {5} |
  |--------------------------|
  | {6} | {7} | {8} |
  ----------------------------
  '''
  MARKERS = [' ', 'X', 'O']

  @staticmethod
  def play(player_1, player_2):
    board_state = State()
    board_state_hash = board_state.get_curr_state_hash_str()
    
    for i in range(9): # 9 moves per game
      if i % 2 == 0:
        player = 1
        move = player_1.chose_action(board_state_hash)
      else:
        player = 2
        move = player_2.chose_action(board_state_hash)

      board_state.set_state(player, move) #update state
      board_state_hash = board_state.get_curr_state_hash_str()
      result = TicTacToe.is_game_over(board_state_hash)

      if result != 0:
        # game is over
        player_1.end_of_episode(result, board_state_hash)
        player_2.end_of_episode(result, board_state_hash)
        break
    return (result, board_state_hash)

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
  
  @staticmethod
  def print_board(state):
    ''' Description: print the current state of the board to the console
    :param: state:
    :return: none
    '''

    cells = []
    for i in range(3): # each row
      for j in range(3): # each elem in row
        cells.append(TicTacToe.MARKERS[state[i][j]].center(6)) # make a pretty string w/ state info
    print(TicTacToe.BOARD_FORMAT.format(*cells)) # starred expression to unpack a  list - transform each element of cell to a positional argurment to format
