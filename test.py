import pandas as pd

ranking_df = pd.read_csv('ranking.csv')


user_anser = input('>>')
user_anser = user_anser.split()
new_user_anser = ''
No_user_anser = ''
for ua in user_anser:
    new_user_anser = new_user_anser + ' ' + ua.capitalize()
    new_user_anser = str.strip(new_user_anser)
    if new_user_anser == 'N':
        No_user_anser = 'No'

returen_data = ranking_df[ranking_df['Name'].isin([new_user_anser])]

print(returen_data.iloc[-1]['Name'])








