import pandas as pd

ranking_df = pd.read_csv('ranking.csv')
print(ranking_df)

user_anser = input('>>')
user_anser = user_anser.split()
new_user_anser = ''
for ua in user_anser:
    new_user_anser = new_user_anser + ' ' + ua.capitalize()


print(new_user_anser)
