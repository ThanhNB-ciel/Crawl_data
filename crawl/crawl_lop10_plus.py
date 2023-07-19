import requests
from bs4 import BeautifulSoup
response = requests.get(
    'https://diemthi.tuyensinh247.com/dc-lop10.html')
data = response.text
soup = BeautifulSoup(data, "html.parser")
link_table = soup.find(
    "ul", attrs={'class': 'list_style', "id": "benchmarking"})


li = link_table.findAll("li")
for year in range(2015, 2023):
    with open(f"/Users/tungnguyen/Desktop/FTECH/FQA_DA/data/school_10_{year}.csv","+a",encoding="utf-8") as f :
        f.write(f"""City,STT,schoolName,NV1,NV2,NV3,Note\n""")
        for i in li:
            city = i.strong.text
            href = i.a['href']
            res = requests.get(
                f"""https://diemthi.tuyensinh247.com{href}?year={year}""")
            data_res = res.text
            soup_res = BeautifulSoup(data_res, "html.parser")
            link_table = soup_res.findAll(
                "tr", attrs={'class': 'bg_white diemchuan10_datarow'})
            for i in link_table:
                tds = i.findAll("td")
                if "THPT" in str({tds[1].text}):
                    f.write(f"""{city},{tds[0].text},{tds[1].text},{tds[2].text},{tds[3].text},{tds[4].text},{tds[5].text}\n""")
                else:
                    f.write(f"""{city},{tds[0].text},THPT {tds[1].text},{tds[2].text},{tds[3].text},{tds[4].text},{tds[5].text}\n""")