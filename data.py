
import requests
import re

f1 = open('teams.txt', 'r')
f2 = open('match_data_20230826.csv', 'w')

f2.write('date,hometeam,awayteam,home,away\n')

teams = [line.strip() for line in f1]

for teama in teams:
  for teamb in teams:
    if teama < teamb:
      print(teama, teamb)
      url = 'https://www.rugbypass.com/live/' + teama + '-vs-' + teamb + '/head-to-head/'

      text = requests.get(url)

      scores = re.findall(r'div> [0-9]+ - [0-9]+ </div', text.text)
      dates = re.findall(r'[0-9]{2} \w{3} [0-9]{2}', text.text)
      countries = re.findall(r'maxw=43" alt="[A-Za-z ]+', text.text)
      diff = len(dates) - len(scores)

      for i in range(len(scores)):
        score = re.findall(r'[0-9]+', scores[i])
        pointsa, pointsb = score[0], score[1]
        date = dates[diff + i]
        home = countries[2 * i][14:]
        away = countries[2 * i + 1][14:]
        f2.write(date + ',' + home + ',' + away + ',' + pointsa + ',' + pointsb + '\n')


