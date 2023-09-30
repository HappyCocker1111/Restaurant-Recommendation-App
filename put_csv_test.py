import pandas as pd

"""ranking_df = pd.read_csv('ranking.csv')

new_row = {'Name': 'Test Mise', 'Count': 1}
ranking_df = pd.concat([ranking_df, pd.DataFrame([new_row])], ignore_index=True)
print('xyz')"""

df = pd.DataFrame([
  ["0001", "ジョン", "Engineer"],
  ["0002", "リリィ", "Sales"]],
  columns=['id', 'name', 'job'])

# CSV ファイル (employee.csv) として出力
df.to_csv("employee.csv", index=False, encoding="utf-8")
print(df)
w = pd.DataFrame([["0003", "ジョー", "Teacher"]])
w.to_csv("employee.csv", index=False, encoding="utf-8", mode='a', header=False)
print('wwww')
print(df)
