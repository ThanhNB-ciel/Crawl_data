import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://hoidap247.com/bai-viet-hao-quang-ruc-ro-thang-3-nam-2023-tren-hoidap247/27'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# table = soup.find('table', xpath='/html/body/div[3]/div/div[5]/div/div[1]/div/div/div[1]/div/table')
table = soup.tbody


data = []
data_rows = table.find_all('tr')
for row in data_rows:
   # columns = row.find('td')
    row_data = []
    for td in row.find_all('td'):
        row_data.append(td.text.strip())
    data.append(row_data)
print(data)