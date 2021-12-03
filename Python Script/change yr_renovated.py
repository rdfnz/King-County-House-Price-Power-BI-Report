import pandas as pd

df = pd.read_csv("maribisniscityadd.csv")
df.loc[df['yr_renovated'] > 0, 'yr_renovated'] = 1
df.to_csv("maribisnistraining.csv", index=False)