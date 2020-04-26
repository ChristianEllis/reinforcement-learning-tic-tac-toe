# Imports
import random

# Custom Imports
from board_state import State
from game import TicTacToe

'''
state_hash = '000 010 002'; value = '0.3'
policy = {
  state_hash_0: value_0,
  state_hash_1: value_1,
  ...
  state_hash_n: value_n
}
'''

class Agent(object):
  def __init__(self, player_num, loss_val, epsilon, alpha, is_learner):
    self.player = player_num
    self.loss_val = loss_val
    self.epsilon = epsilon
    self.alpha = alpha
    self.is_learner = is_learner

    self.policy = {}
    self.prev_state_hash_key = None
    self.prev_score = None

  def chose_action(self, state_hash_key):
    self.prev_state_hash_key = state_hash_key
    self.prev_score = self.lookup_score_in_policy(state_hash_key)

    roll = random.random()
    if roll < self.epsilon:
      move = self.explore(state_hash_key)
    else:
      move, best_val = self.exploit(state_hash_key)
      self.value_iteration(best_val)
    return move

  def explore(self, state_hash_key):
    state = State.hash_to_state(state_hash_key)
    available_states = []
    for i in range(3):
      for j in range(3):
        if state[i][j] == 0:
          available_states.append((i,j))
    return random.choice(available_states)

  def exploit(self, state_hash_key):
    state = State.hash_to_state(state_hash_key)
    best_val = -999999
    best_move = None

    # Iterate through each possible move, calculate value, and update best value
    for i in range(3):
      for j in range(3):
        if state[i][j] == 0:
          possible_state = state
          possible_state[i][j] = self.player
          possible_state_hash_key = State.state_to_hash(possible_state) #convert state to a hash
          val = self.lookup_score_in_policy(possible_state_hash_key)

          if val > best_val:
            best_val = val
            best_move = (i, j)
    return (best_move, best_val)

  def value_iteration(self, new_best_val):
    if self.prev_state_hash_key != None and self.is_learner:
      new_value = self.alpha * (new_best_val - self.prev_score)
      self.policy[self.prev_state_hash_key] += new_value

  def lookup_score_in_policy(self, state_hash_key):
    if not state_hash_key in self.policy:
      value = self.get_value_of_state(state_hash_key)# calclate value
      self.add_state_hash_value_pair_to_policy(state_hash_key, value)
    return self.policy[state_hash_key]
  
  def get_value_of_state(self, state_hash_key):
    overall_game_state = TicTacToe.is_game_over(state_hash_key) # Determine if there is a winner or not
    value = self.calc_value(overall_game_state)# Determine value of state based on win, loss, draw, or none

    return value

  def calc_value(self, overall_game_state):
    if overall_game_state == self.player:
      return 1
    elif overall_game_state == 0:
      return 0.5
    elif overall_game_state == -1:
      return 0
    else:
      return self.loss_val

  def add_state_hash_value_pair_to_policy(self, key, value):
    self.policy[key] = value

  def end_of_episode(self):
    self.prev_state_hash_key = None
    self.prev_score = 0

