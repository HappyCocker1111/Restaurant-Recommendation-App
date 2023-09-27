import pandas as pd

ranking_df = pd.read_csv('ranking.csv')
print(ranking_df)

user_anser = input('>>')
user_anser = user_anser.split()
new_user_anser = ''
for ua in user_anser:
    new_user_anser = new_user_anser + ' ' + ua.capitalize()
    if new_user_anser == 'N':
        new_user_anser = 'No'

if new_user_anser == 'No':

#https://qiita.com/ryu022304/items/e5a3b470795de883a09a