import pandas as pd

df = pd.read_csv("/content/MariBisnis.csv")

from uszipcode import SearchEngine, SimpleZipcode, Zipcode
search = SearchEngine()

postcode = df['zipcode'].values
citylist = []
for x in postcode:
  zipcode = search.by_zipcode(x)
  citylist.append(zipcode.major_city)

df['city'] = citylist
df.to_csv('maribisniscityadd.csv', index=False)