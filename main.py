# Library Imports
import csv
from tqdm import trange

# Custom Imports
from board_state import State
from agent import Agent
from game import TicTacToe

def train_agent(iterations):
  try:
    p1 = Agent(1, -1, 0.1, 0.1, True, 'p1_policy.csv')
    p2 = p1
    # p2 = Agent(1, -1, 0.1, 0.1, True)

    series = ['P1_Wins', 'P2_Wins', 'Draw']
    f = open('results.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(series)

    p1_wins = 0
    p2_wins = 0
    draw = 0
    iterator = 1
    for i in trange(iterations):
      winner = TicTacToe.play(p1, p2)
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

      p1.end_of_episode()
      iterator += 1

    p1.dump_policy_to_csv('p1_policy.csv')
  except:
    print("Program crashed - saving policy...")
    p1.dump_policy_to_csv('p1_policy.csv')

if __name__ == "__main__":
  train_agent(int(1e3))
  