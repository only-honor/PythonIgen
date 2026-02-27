import pandas as pd
df = pd.read_json("package.json")
print(df.head())
print(df.head(2))
print(df.tail(2))
print(df.info())
