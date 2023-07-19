# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# from tqdm import tqdm

# data = {'username':[],
#         'name':[],
#         # 'prize':[],
#         'note':[]}
# link_lazi = []
# for num in tqdm(range(0,41,10)):
#     url = f'https://lazi.vn/event?start={num}'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     lazi_links = soup.find_all(class_='nen_trang_full')
#     for link in lazi_links:
#         response=''
#         try:
#             link = link.h2.a.get('href')
#             if 'giai-thuong-thang' in link:
#                 # print(link)
#                 # link_lazi.append(link)
#                 response = requests.get(link)
#                 soup = BeautifulSoup(response.content, 'html.parser')
#                 name = soup.find(class_='art_content').find_all('a')
#         # prize = soup.find(class_='art_content').find_all(class_='red')
#                 for item in name:
#                     data['username'].append(item.get('href').split('/')[-1])
#                     data['name'].append(item.find(class_='xanh'))
#                     data['note'].append(link.rstrip('\n').split('/')[6])
#         except:
#             print('err')

# df = pd.DataFrame(data)
# print(df)
# df.to_csv('data_lazi_test.csv',index=False)


import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import re


link_lazi = []
for num in tqdm(range(0,41,10)):
    url = f'https://lazi.vn/event?start={num}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    lazi_links = soup.find_all(class_='nen_trang_full')
    for link in lazi_links[2]:
        response=''
        try:
            link = link.h2.a.get('href')
            if 'giai-thuong-thang' in link:
                # print(link)
                # link_lazi.append(link)
                response = requests.get(link)
                soup = BeautifulSoup(response.content, 'html.parser')
                name = soup.find(class_='art_content').find_all('a')
                data = {'username':[],
                        'name':[],
                        # 'prize':[],
                        'note':[]}
                for item in name:
                    data['username'].append(item.get('href').split('/')[-1])
                    data['name'].append(item.find(class_='xanh'))
                    data['note'].append(link.rstrip('\n').split('/')[6])
                
                text = soup.find(class_='art_content').findAll(text=True)
                out= text[text.index('1. Điểm giải bài (điểm do người đăng bài tập chấm điểm):'):-37]
                out= list(filter(lambda a: a != ": ", out))
                out= list(filter(lambda a: a != ", ", out))
                data1 = {'name':[],
                        'prize':[],
                        'top_prize':[],
                        'type_prize':[]}
                name = ''
                prize = ''
                top_prize = ''
                type_prize = ''

                for i in out:
                    if re.search(r"\d\.\s\w+", i): #loại giải
                        type_prize = i
                    elif re.search(r"^([0-9]{2,3}:?)\s\w+", i): #giá trị
                        prize = i
                    elif "-" in i or "+" in i: #top giải
                        top_prize = i
                    else:
                        data1['name'].append(i)
                        data1['prize'].append(prize)
                        data1['top_prize'].append(top_prize)
                        data1['type_prize'].append(type_prize)

                df1 = pd.DataFrame(data1)
                df2 = pd.DataFrame(data)
                df2['name']=df2['name'].str.replace(r'<[^<>]*>', '', regex=True)
                df2 = df2[~df2['username'].isin(['adminlazi','statistic','setting_reward','lazi.assistant'])]

        except:
            print('err')
            pass


# print(df)
# df.to_csv('data_lazi_test.csv',index=False)