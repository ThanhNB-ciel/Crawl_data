import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

path = "https://diemthi.tuyensinh247.com"
url = f"{path}/diem-chuan.html"
response = requests.get(url)


soup = BeautifulSoup(response.content, "html.parser")
# print(soup)
link_table = soup.find("div", attrs={"class": "list-schol fl"})
def test(_path,year):
    url = f"{path}{_path}?y={year}"
    response = requests.get(url).text
    df = pd.read_html(response)
    dfx = df[0]
    dfx.columns = dfx.iloc[0]
    dfx=dfx[1:]
    return dfx

links = []
title = []
for row in link_table.find_all("li"):
    link = row.find("a")
    if link:
        links.append(link["href"])
        title.append(link['title'])
        
l2 = []
len_link = len(links)
for i in tqdm(range(len_link)):
    # df = pd.DataFrame(test(i))
    for year in range(2015,2023,1):
        try:
            df = test(links[i],year)
            df['Tên trường']= title[i]
            df['Năm'] = year
            l2.append(df)
        except:
            continue

# print(df)
dfx = pd.concat(l2)
dfx=dfx[['Tên trường','Mã ngành','Tên ngành','Tổ hợp môn','Điểm chuẩn','Ghi chú','Năm']]
new_order = ['Tên trường','Năm','Mã ngành','Tên ngành','Tổ hợp môn','Điểm chuẩn','Ghi chú']
dfx = dfx.reindex(columns=new_order)
print(dfx.head())
dfx.to_csv("diemchuan_daihoc.csv", index=False)