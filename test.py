import pandas as pd

ranking_df = pd.read_csv('ranking.csv')
print(ranking_df['Name'])

user_anser = input('>>')
user_anser = user_anser.split()
new_user_anser = ''
No_user_anser = ''
for ua in user_anser:
    new_user_anser = new_user_anser + ' ' + ua.capitalize()
    new_user_anser = str.strip(new_user_anser)
    if new_user_anser == 'N':
        No_user_anser = 'No'

returen_data = ranking_df[ranking_df['Count'].isin([new_user_anser])]

if len(returen_data.index) == 0:
    new_row = {'Name': new_user_anser, 'Count': 1}
    ranking_df = pd.concat([ranking_df, pd.DataFrame([new_row])], ignore_index=True)
    print('xyz')









