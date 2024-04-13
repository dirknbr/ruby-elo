
import pandas as pd
from utils import *

data = pd.read_csv('investec_20240413.csv', parse_dates=['Date'])
def calc(x):
  try:
    h, a = x.split('-')
    return int(h) - int(a)
  except:
    return None # for nan
print(calc('10-1'))

data['diff'] = [calc(str(x)) for x in list(data.Score)]
print(data.head())

# sort by date and then calculate elo
# data = data.sort_values('Date')

# compare the three elo algos and find smallest error

elo1 = {team: 400 for team in data.Home.unique()}
elo2 = {team: 400 for team in data.Home.unique()}
elo3 = {team: 400 for team in data.Home.unique()}

err = np.zeros(4)

for i, row in data.iterrows():
  R_A1, R_B1 = elo1[row.Home], elo1[row.Away]
  R_A2, R_B2 = elo2[row.Home], elo2[row.Away]
  R_A3, R_B3 = elo3[row.Home], elo3[row.Away]
  S_A = 1 * (row['diff'] > 0)
  E_A1 = expect(R_A1, R_B1)
  E_A2 = expect(R_A2, R_B2)
  E_A3 = expect(R_A3, R_B3)
  E_A4 = (E_A1 + E_A2 + E_A3) / 3 # avg
  err[0] += abs(E_A1 - S_A)
  err[1] += abs(E_A2 - S_A)
  err[2] += abs(E_A3 - S_A)
  err[3] += abs(E_A4 - S_A)
  elo1[row.Home] = update(R_A1, S_A, E_A1)  
  elo1[row.Away] = update(R_B1, 1 - S_A, 1 - E_A1)
  elo2[row.Home] = update2(R_A2, row['diff'], E_A2)  
  elo2[row.Away] = update2(R_B2, -row['diff'], 1 - E_A2)
  elo3[row.Home] = update3(R_A3, row['diff'], E_A3)  
  elo3[row.Away] = update3(R_B3, -row['diff'], 1 - E_A3)

print(err)

for x in sorted([(elo1[k], k) for k in elo1], reverse=True):
  print(x)

# print(expect(elo['Ireland'], elo['Italy']))