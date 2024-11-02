
import requests
import re
import datetime

f1 = open('teams.txt', 'r')
f2 = open('match_data_20241102.csv', 'w')

f2.write('date,hometeam,awayteam,home,away\n')

teams = [line.strip() for line in f1]

for teama in teams:
  for teamb in teams:
    if teama < teamb:
      print(teama, teamb)
      url = 'https://www.rugbypass.com/live/' + teama + '-vs-' + teamb + '/head-to-head/'

      text = requests.get(url)

      scores = re.findall(r'[0-9]+ - [0-9]+', text.text)
      dates = re.findall(r'[0-9]{2} \w{3} [0-9]{2}', text.text)
      countries = re.findall(r'maxw=43&v=[0-9]+" alt="[A-Za-z ]+', text.text)

      try:
        # if in future, remove
        if datetime.datetime.strptime(dates[0], "%d %b %y").date() > datetime.date.today():
          dates = dates[1:]
      except:
        pass

      for i in range(len(countries) // 2):
        score = re.findall(r'[0-9]+', scores[i])
        pointsa, pointsb = score[0], score[1]
        date = dates[i]
        # maxw=43&v=1725422053" alt="England
        home = countries[2 * i][27:]
        away = countries[2 * i + 1][27:]
        f2.write(date + ',' + home + ',' + away + ',' + pointsa + ',' + pointsb + '\n')

f2.close()
