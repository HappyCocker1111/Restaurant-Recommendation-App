import pandas as pd

ranking_df = pd.read_csv('ranking.csv')
# print(ranking_df['Count'].idxmax())
# print(ranking_df.iat[ranking_df['Count'].idxmax(), 0])

#print(ranking_df[ranking_df['Count']=='Hanano Sato'].empty)
print(ranking_df[ranking_df['Name']=='Hanano Sato'][-1])