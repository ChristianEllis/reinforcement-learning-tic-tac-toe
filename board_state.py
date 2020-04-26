# Library Imports
import numpy as np

class State(object):
  ''' Desc: Static class containing helpers to manage board state
  Notes:
    - 0 represents an empty spot on the board
    - 1 represents a spot taken up by player_1's marker - normally 'X'
    - 2 represents a spot taken up by by player_2's marker - normally 'O'
  '''

  def __init__(self):
    ''' Desc: initializes a new state class that sets current state to a blank board and a non-existent previous state

    '''
    self.state = State.empty_state()
    self.prev_state = None
  
  def set_state(self, player_number, position):
    ''' Desc: Update the board's state
    :param 1: position - 2 pair tuple for x, y position (x,y)
    :param 2: player number - either player 1 or player 2
    '''
    prev_state = self.state
    new_state = prev_state

    if player_number == 1:
      prev_state[position] = 1
    elif player_number == 2:
      prev_state[position] = 2

    self.state = new_state
    self.prev_state = prev_state

  def get_curr_state_hash_str(self):
    ''' Desc: Convert  3,3 np array of state (single digit integers) into a string

    '''
    s = "".join([ str(i) for i in self.state.flatten() ])
    return s[0:3] + ' ' + s[3:6] + ' ' + s[6:9]

  @staticmethod
  def empty_state():
    ''' Desc: Returns a 3x3 np array all containing zeros

    '''
    return np.array([
    [ 0, 0, 0 ],
    [ 0, 0, 0 ],
    [ 0, 0, 0 ]
  ])

  @staticmethod
  def indexed_state():
    ''' Desc: Returns a 3x3 np array all containing zeros

    '''
    return np.array([
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
  ])
    
  @staticmethod
  def hash_to_state(hash):
    ''' Desc: Convert a string of single digit integers into an np array

    '''
    hash = hash.replace(' ', '')
    return np.asarray(list(map(int, hash))).reshape((3,3))
  
  @staticmethod
  def state_to_hash(state):
    ''' Desc: Convert a board state to a string of single digit integers
    
    '''
    s = "".join([ str(i) for i in state.flatten() ])
    return s[0:3] + ' ' + s[3:6] + ' ' + s[6:9]
