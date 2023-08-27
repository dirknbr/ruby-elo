
import pandas as pd
from utils import *

data = pd.read_csv('match_data_20230826.csv', parse_dates=['date'])
data['diff'] = data.home - data.away
print(data.describe())

# sort by date and then calculate elo
data = data.sort_values('date')

elo = {team: 400 for team in data.hometeam.unique()}

for i, row in data.iterrows():
  R_A, R_B = elo[row.hometeam], elo[row.awayteam]
  S_A = 1 * (row['diff'] > 0)
  E_A = expect(R_A, R_B)
  # elo[row.hometeam] = update(R_A, S_A, E_A)  
  # elo[row.awayteam] = update(R_B, 1 - S_A, 1 - E_A)
  elo[row.hometeam] = update2(R_A, row['diff'], E_A)  
  elo[row.awayteam] = update2(R_B, -row['diff'], 1 - E_A)

for x in sorted([(elo[k], k) for k in elo], reverse=True):
  print(x)

print(expect(elo['Ireland'], elo['Italy']))