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



# '//*[@id="data"]'


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('http://s.cafef.vn/screener.aspx')
table_id = driver.find_element(By.XPATH,'//*[@id="myTable"]/tbody')


dfx=[]
rows = table_id.find_elements(By.TAG_NAME, 'tr')
for row in rows[:30]:
    # col = [row.find_elements(By.TAG_NAME, "td")[i].text for i in range(11)]
    col = [col.text for col in row.find_elements(By.TAG_NAME, "td")]
    df = pd.DataFrame([col],columns=['stt','ten_cong_ty','ma_co_phieu','san_chung_khoan','thay_doi_5_phien_truoc','von_hoa_thi_truong','klgd','eps','p_e','he_so_beta','gia'])
    dfx.append(df)
    df = pd.concat(dfx, ignore_index=True)
    df = df.sort_values(by='gia',ascending = False)
    df['date'] = [date.today()] * len(df.index)
    df = df[['date','ten_cong_ty','ma_co_phieu','san_chung_khoan','thay_doi_5_phien_truoc','von_hoa_thi_truong','klgd','eps','p_e','he_so_beta','gia']]
    df.to_csv('ck.csv', index=False)

print(df.head(5))
time.sleep(5)
driver.close()