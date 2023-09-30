import pandas as pd

ranking_df = pd.read_csv('ranking.csv')


print('こんにちは!私は Robokoです。あなたの名前は何ですか?')
user_name = input('>>')
print(user_name)

Robokos_question = user_name + 'さん。どこのレストランが好きですか?'

#ranking_df = pd.read_csv(ranking_df.to_csv("ranking.csv", index=False, encoding="utf-8", mode='a', header=False).csv)
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

returen_data = ranking_df[ranking_df['Count'].isin([new_user_anser])]
if len(returen_data.index) == 0:
    new_row = {'Name': new_user_anser, 'Count': 1}
    new_row.to_csv("ranking.csv",index=False, encoding="utf-8", mode='a', header=False)
    print(user_name +'さん。ありがとうございました。\n良い一日を！さようなら。')






