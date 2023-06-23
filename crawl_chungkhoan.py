import numpy as np
from selenium import webdriver
from time import sleep
import random
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd
import os,time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import date
from clickhouse_driver import Client




# '//*[@id="data"]'


# driver = webdriver.Chrome(executable_path='chromedriver.exe')
# driver.get('http://s.cafef.vn/screener.aspx')
# table_id = driver.find_element(By.XPATH,'//*[@id="myTable"]/tbody')

# dfx=[]
# rows = table_id.find_elements(By.TAG_NAME, 'tr')
# for row in rows[:30]:
#     # col = [row.find_elements(By.TAG_NAME, "td")[i].text for i in range(11)]
#     col = [col.text for col in row.find_elements(By.TAG_NAME, "td")]
#     df = pd.DataFrame([col],columns=['stt','ten_cong_ty','ma_co_phieu','san_chung_khoan','thay_doi_5_phien_truoc','von_hoa_thi_truong','klgd','eps','p_e','he_so_beta','gia'])
#     dfx.append(df)
#     df = pd.concat(dfx, ignore_index=True)
#     df = df.sort_values(by='gia',ascending = False)
#     df['date'] = [date.today()] * len(df.index)
#     df = df[['date','ten_cong_ty','ma_co_phieu','san_chung_khoan','thay_doi_5_phien_truoc','von_hoa_thi_truong','klgd','eps','p_e','he_so_beta','gia']]
#     # df.to_csv('ck.csv', index=False)

# # print(df.head())
# time.sleep(5)
# driver.close()

df = pd.read_csv('ck.csv',index_col= 0)

# đẩy data import pandas as pd
from clickhouse_driver import Client
import csv
clickhouse_info = {
    "host": "103.119.132.171",
    "user": "",
    "password": ""
}
client = Client(host=clickhouse_info['host'], port=8123, user=clickhouse_info['user'],
                   password=clickhouse_info['password'], settings={
    'use_numpy': True}
)

# client = Client(host ='localhost', port=9002, user="default", settings ={'use_numpy':True})
client.insert_dataframe("insert into thanhnb.chung_khoan values",df)

