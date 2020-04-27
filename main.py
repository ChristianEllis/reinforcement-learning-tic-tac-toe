import csv

from board_state import State
from agent import Agent
from game import TicTacToe

def play(agent_1, agent_2):
  board_state = State()
  board_state_hash = board_state.get_curr_state_hash_str()
  player = None
  
  for i in range(9): # 9 moves per game
    if i % 2 == 0:
      player = 1
      move = agent_1.chose_action(board_state_hash)
    else:
      player = 2
      move = agent_2.chose_action(board_state_hash)
    
    board_state.set_state(player, move)  #update state
    board_state_hash = board_state.get_curr_state_hash_str()
    result = TicTacToe.is_game_over(board_state_hash)
    
    if result != 0:
      break
  return result

if __name__ == "__main__":
  p1 = Agent(1, -1, 0.1, 0.1, True, 'p1_policy.csv')
  p2 = p1
  # p2 = Agent(1, -1, 0.1, 0.1, True)

  series = ['Winner']
  f = open('results.csv', 'w')
  writer = csv.writer(f)
  writer.writerow(series)

  p1_wins = 0
  p2_wins = 0
  draw = 0
  for i in range(1e9):
    winner = play(p1, p2)
    if winner == -1:
      draw += 1
    elif winner  == 1:
      p1_wins += 1
    elif winner == 2:
      p2_wins += 1

    p1.end_of_episode()
    writer.writerow([str(winner)])

  p1.dump_policy_to_csv('p1_policy.csv')