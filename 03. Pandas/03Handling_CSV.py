import pandas as pd
# df = pd.read_csv("data.csv")
# #print(df.head())
# #print(df.head(5))
# #print(df.tail())
# print(df.info())

df = pd.read_json("dta.json")
print(df.head())