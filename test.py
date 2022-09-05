import pandas as pd
import numpy as np

df = pd.read_csv(
    'https://www.daggegevens.knmi.nl/klimatologie/daggegevens?stns=235:370&vars=TN:TX', delimiter=',', comment='#', na_filter=True, header=None, names=['Stn', 'Date', 'Lo', 'Hi'])

df['Date'] = pd.to_datetime(df['Date'], format="%Y%M%d")
df.drop(df.index[df['Lo'] == '     '], inplace=True)
df.set_index("Stn", inplace=True)
df['Lo'] = df['Lo'].astype('int')
df['Hi'] = df['Hi'].astype('int')
df["Lo"] = df["Lo"] / 10
df["Hi"] = df["Hi"] / 10

print(df)
