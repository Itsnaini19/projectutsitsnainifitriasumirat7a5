import pandas as pd

df = pd.read_json('data2.json')

print(df.to_string())
