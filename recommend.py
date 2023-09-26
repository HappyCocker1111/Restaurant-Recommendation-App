import pandas as pd

ranking_df = pd.read_csv('ranking.csv')

print('こんにちは!私は Robokoです。あなたの名前は何ですか?')
user_name = input('>>')
print(user_name)

Robokos_question = user_name + 'さん。どこのレストランが好きですか?'

ranking_df = pd.read_csv('ranking.csv')
if ranking_df.empty == True:
    print(Robokos_question)

user_anser = input('>>')
user_anser = user_anser.split()
new_user_anser = ''
for ua in user_anser:
    new_user_anser = new_user_anser + ' ' + ua.capitalize()








