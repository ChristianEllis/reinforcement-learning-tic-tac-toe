# Library Imports
import csv
from tqdm import trange

# Custom Imports
from game import TicTacToe
from board_state import State
from agent import Agent
from human import Human

def train_agent(iterations):
  try:
    p1 = Agent(
      1, # Player #
      -10, # Loss Value
      0.2, # Epsilon (exploration rate)
      0.2, # Alpha (learning rate)
      0.9, # Gamma (make infinite sum finite) - https://stats.stackexchange.com/questions/221402/understanding-the-role-of-the-discount-factor-in-reinforcement-learning
      True, # Update learner
    )
    # p2 = p1
    p2 = Agent(2, -1, 1, 0.1, 0.9, False) # Random Agent

    series = ['P1_Wins', 'P2_Wins', 'Draw']
    f = open('results.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(series)

    p1_wins = 0
    p2_wins = 0
    draw = 0
    iterator = 1

    for i in trange(iterations):

      if iterator % 2 == 0:
        winner, board_state_hash = TicTacToe.play(p1, p2)
      else:
        winner, board_state_hash = TicTacToe.play(p2, p1)

      if winner == -1:
        draw += 1
      elif winner  == 1:
        p1_wins += 1
      elif winner == 2:
        p2_wins += 1

      if iterator % 100 == 0:
        writer.writerow([p1_wins, p2_wins, draw])
        p1_wins = 0
        p2_wins = 0
        draw = 0

      iterator += 1

    print('Saving policy')
    p1.dump_policy_to_csv('p1_policy.csv')
    p2.dump_policy_to_csv('p2_policy.csv')
  except Exception as e:
    print(str(e))
    print("Program crashed - saving policy...")
    p1.dump_policy_to_csv('p1_policy.csv')
  except KeyboardInterrupt:
    print("Program crashed - saving policy...")
    p1.dump_policy_to_csv('p1_policy.csv')
    p2.dump_policy_to_csv('p2_policy.csv')

def human_against_agent(player_num, filename):
  play = True
  while play == True:
    # Assign players
    if player_num == 1:
      player_1 = Human(1)
      player_2 = Agent(2, -1, 0.0, .1, 0.9, True, filename)
    else:
      player_1 = Agent(1, -1, 0.0, .1, 0.9, True, filename)
      player_2 = Human(2)

    winner, board_state_hash = TicTacToe.play(player_1, player_2)
    if player_num == 2:
      # then player 1 must be the agent
      print("Thanks for the training data silly human!")
      player_1.dump_policy_to_csv('p1_policy.csv')

    action = input('Play Again? (y or n)')
    if action != 'y':
      return

if __name__ == "__main__":
  # train_agent(int(1e6))
  human_against_agent(2, 'p1_policy.csv')