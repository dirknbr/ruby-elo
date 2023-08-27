
import numpy as np
from scipy.special import expit

# https://en.wikipedia.org/wiki/Elo_rating_system
# http://www.lifewithalacrity.com/2006/01/ranking_systems.html

def expect(R_A, R_B):
  return 1 / (1 + 10 ** ((R_B - R_A) / 400))

# print(expect(100, 200))

def update(R_A, S_A, E_A, K=20):
  return R_A + K * (S_A - E_A)

# print(update(100, 1, .5))

# https://en.wikipedia.org/wiki/TrueSkill
# https://www.microsoft.com/en-us/research/wp-content/uploads/2007/01/NIPS2006_0688.pdf

def err_prob_score(score, p):
  # p is in (0, 1), score is in (-25, 25) because score ~ N(5, 20)
  score2 = (np.clip(score, -25, 25) + 25) / 50
  return score2 - p

# print(err_prob_score(0, .5))
# print(err_prob_score(-100, .999))

def update2(R_A, S_A, E_A, K=20):
  # take into account actual point difference
  return R_A + K * err_prob_score(S_A, E_A)

def update3(R_A, S_A, E_A, K=20):
  # take into account actual point difference
  return R_A + K * (expit(S_A / 7) - E_A)

# print(update(100, 1, .5))
# print(update2(100, 10, .5))
# print(update3(100, 10, .5))

def odds_to_prob(odds):
  return odds / (odds + 1)

def prob_to_odds(p):
  return p / (1 - p)

# print(odds_to_prob(13/10))
# print(prob_to_odds(.6))

