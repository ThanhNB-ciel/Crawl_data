
import pandas as pd
import requests
from bs4 import BeautifulSoup


response = requests.get("http://s.cafef.vn/screener.aspx").text
soup = BeautifulSoup(response, "html.parser")

df = pd.read_html(response)
dfx = df[0]
print(dfx) 