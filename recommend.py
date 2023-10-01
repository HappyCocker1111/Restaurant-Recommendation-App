import pandas as pd

ranking_df = pd.read_csv('ranking.csv')


print('こんにちは!私は Robokoです。あなたの名前は何ですか?')
user_name = input('>>')
print(user_name)

Robokos_question = user_name + 'さん。どこのレストランが好きですか?'

ranking_df = pd.read_csv("ranking.csv")
if ranking_df['Name'].empty == True:
    print(Robokos_question)

user_anser = input('>>')
user_anser = user_anser.split()
new_user_anser = ''
No_user_anser = ''
for ua in user_anser:
    new_user_anser = new_user_anser + ' ' + ua.capitalize()
    new_user_anser = str.strip(new_user_anser)
    if new_user_anser == 'N':
        No_user_anser = 'No'


if len(ranking_df['Count']) == 0:
    Result = pd.DataFrame({'Name': [new_user_anser], 'Count': [1]})
    Result.to_csv("ranking.csv",index=False, encoding="utf-8",header=True)
    print(user_name +'さん。ありがとうございました。\n良い一日を！さようなら。')






