import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from bs4 import BeautifulSoup

knmi_url = 'https://www.daggegevens.knmi.nl/'
post_url = 'https://www.daggegevens.knmi.nl/klimatologie/daggegevens?stns='

# Parsing the HTML
r = requests.get(knmi_url)
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_='stations-container')
lines = s.find_all('div')

options = []
for line in lines:
    line = line.text.strip()
    if len(line) > 0:
        options.append(line)

selection = st.multiselect("Weerstation", options)

if len(selection) > 0:
    for option in selection:
        post_url = post_url + option[0:3] + ':'

    post_url = post_url + '&vars=TN:TX'

    df = pd.read_csv(post_url, delimiter=',', comment='#',
                     header=None, names=['Stn', 'Date', 'Lo', 'Hi'])

    df['Date'] = pd.to_datetime(df['Date'], format="%Y%m%d")
    df.drop(df.index[df['Lo'] == '     '], inplace=True)
    df.drop(df.index[df['Hi'] == '     '], inplace=True)

    pd.to_numeric(df['Lo'], errors='coerce').fillna(0).astype(int)
    pd.to_numeric(df['Hi'], errors='coerce').fillna(0).astype(int)
    df['Lo'] = df['Lo'].astype('int')
    df['Hi'] = df['Hi'].astype('int')
    df["Lo"] = df["Lo"] / 10
    df["Hi"] = df["Hi"] / 10

    fig = px.bar(df, x='Date', y='Hi', color='Stn')

    st.plotly_chart(fig, use_container_width=True)
