import pandas as pd

ranking_df = pd.read_csv('ranking.csv')
"""
ユーザーからの回答を処理します
"""
def processing_useranser(user_anser):
    user_anser = user_anser.split()
    new_user_anser = ''
    No_user_anser = ''
    for ua in user_anser:
        new_user_anser = new_user_anser + ' ' + ua.capitalize()
        new_user_anser = str.strip(new_user_anser)
        if new_user_anser == 'N':
            new_user_anser = 'No'
        elif new_user_anser == 'Y':
            new_user_anser = 'Yes'
    return new_user_anser


print('こんにちは!私は Robokoです。あなたの名前は何ですか?')
user_name = input('>>')
print(user_name)




Robokos_question = user_name + 'さん。どこのレストランが好きですか?'
if ranking_df['Name'].empty == True:
    print(Robokos_question)
    user_anser = input('>>')
    new_user_anser = processing_useranser(user_anser)

    if len(ranking_df['Count']) == 0:
        Result = pd.DataFrame({'Name': [new_user_anser], 'Count': [1]})
        Result.to_csv("ranking.csv", index=False, encoding="utf-8", header=True)
        print(user_name + 'さん。ありがとうございました。\n良い一日を！さようなら。')
else:
    print('私のオススメのレストランは、 Japanes\nAppleです。 このレストランは好きですか? [Yes / No]')

    user_anser = input('>>')
    new_user_anser = processing_useranser(user_anser)

    if new_user_anser == 'No':
        print(user_name + 'さん。どこのレストランが好きですか?')
        user_anser = input('>>')
        print(user_name + 'さん。ありがとうございました\n 良い一日を!さようなら。')
    elif new_user_anser == 'Yes':
        print(user_name + 'さん。ありがとうございました\n 良い一日を!さようなら。')











