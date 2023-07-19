import requests
from bs4 import BeautifulSoup

response = requests.get('http://s.cafef.vn/screener.aspx')
data = response.text
soup = BeautifulSoup(data, "html.parser")

table = soup.find('div', attrs={'class': "clearfix", "id": "data"})
# table = soup.find('div', attrs={'class': 'tablesorter'})
# print(table)


# quit()
headers = []
header_row = table.find('tr')
for th in header_row.find_all('th'):
    headers.append(th.text.strip())

data = []
data_rows = table.find_all('tr') 
print(data_rows)
for row in data_rows:
    row_data = []
    for td in row.find_all('td'):
        row_data.append(td.text.strip())
    data.append(row_data)
print(row_data)  

quit()
import requests
from bs4 import BeautifulSoup

response = requests.get('http://s.cafef.vn/screener.aspx')
data = response.text
soup = BeautifulSoup(data, "html.parser")

table = soup.find('div', attrs={'class': "clearfix", "id": "data"})
# print(table)
# quit()

headers = []
header_row = table.find('tr')
for th in header_row.find_all('th'):
    headers.append(th.text.strip())
print(headers)


data = []
data_rows = table.find_all('tr') 
print(data_rows)

for row in data_rows:
    row_data = []
    for td in row.find_all('td'):
        row_data.append(td.text.strip())
    data.append(row_data)
print(data)




# data = []
# data_rows = table.findAll('tr')
# for row in data_rows:
#     row_data = []
#     for td in row.findAll('td'):
#         row_data.append(td.text.strip())
#     data.append(row_data)
    
# print(data)
