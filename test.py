import pandas as pd

post_url = (
    "https://www.daggegevens.knmi.nl/klimatologie/daggegevens?stns=370&vars=TN:TX:DR:RH"
)
df = pd.read_csv(
    post_url,
    delimiter=",",
    comment="#",
    header=None,
    names=["Stn", "Date", "Lo", "Hi", "DR", "RH"],
)

print(df.head())
