import requests
from bs4 import BeautifulSoup
response = requests.get(
    'https://diemthi.tuyensinh247.com/dc-lop10.html')
data = response.text
soup = BeautifulSoup(data, "html.parser")
link_table = soup.find(
    "ul", attrs={'class': 'list_style', "id": "benchmarking"})


li = link_table.findAll("li")
for year in range(2015, 2024):
    with open(f"/Users/tungnguyen/Desktop/FTECH/FQA_DA/data/school_10_{year}.csv", "+a", encoding="utf-8") as f:
        f.write(f"""City|STT|schoolName|NV1|NV2|NV3|Note\n""")
        for i in range(1, 70):
            try:
                res = requests.get(
                    f"""https://diemthi.tuyensinh247.com/dc-lop10/ha-noi-p{i}.html?year={year}""")
                data_res = res.text
                soup_res = BeautifulSoup(data_res, "html.parser")
                city = soup_res.find(
                    "p", attrs={'class': 'inl-block fl'}).strong.text[6:-7]
                link_table = soup_res.findAll(
                    "tr", attrs={'class': 'bg_white diemchuan10_datarow'})
                for i in link_table:
                    tds = i.findAll("td")
                    note = "\"" + \
                        str(tds[5].text)\
                        .replace("\"", "")\
                        .replace(",", ".")\
                        .replace('&nbsp;', '')\
                        + "\""
                    school = str(tds[1].text)\
                        .replace("\"", "")\
                        .replace('&nbsp;', '')
                    if "THPT" in str({tds[1].text}):

                        f.write(
                            f"""{city}|{tds[0].text}|"{school}"|{tds[2].text}|{tds[3].text}|{tds[4].text}|{note}\n""")
                    else:
                        f.write(
                            f"""{city}|{tds[0].text}|"THPT {tds[1].text}"|{tds[2].text}|{tds[3].text}|{tds[4].text}|{note}\n""")
            except Exception as e:
                print(i)
_list = []              
                #12
#đẩy data import pandas as pd
# from clickhouse_driver import Client
# import csv
# clickhouse_info = {
#     "host": "192.168.8.124",
#     "user": "",
#     "password": ""
# }
# client_ch = Client(host=clickhouse_info['host'], user=clickhouse_info['user'],
#                    password=clickhouse_info['password'], settings={
#     'use_numpy': True}
# )
# for year in range(2015, 2024):
#     # Read data
#     print(year)
#     df = pd.read_csv(
#         f'/Users/tungnguyen/Desktop/FTECH/FQA_DA/data/school_10_{year}.csv', sep="|", quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     # Processing data
#     df['year'] = year
#     df['NV1'] = df['NV1'].replace(",", ".")
#     df['NV2'] = df['NV2'].replace(",", ".")
#     df['NV3'] = df['NV3'].replace(",", ".")
#     # df.to_csv("test.csv")
#     # quit()
#     # Storage data
#     client_ch.insert_dataframe(
#          'INSERT INTO FQA_Score.highSchool_score VALUES',
#          df,
#          settings=dict(use_numpy=True),
#      )

