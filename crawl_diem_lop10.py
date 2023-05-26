import numpy as np
from selenium import webdriver
from time import sleep
import random
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
)
from selenium.webdriver.common.by import By
import pandas as pd
import os, time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import date
from tqdm import tqdm
from selenium.webdriver.support.ui import WebDriverWait as wait
from logging import Logger


# path = "https://diemthi.tuyensinh247.com"
path = "https://diemthi.tuyensinh247.com/dc-lop10.html"
response = requests.get(path)
soup = BeautifulSoup(response.content, "html.parser")

list_school = soup.find_all(class_="list-schol fl")
l1 = list_school[0].find_all("li")
href_list = [item.a["href"] for item in l1]
provine = [item.find("strong").text for item in l1]
# print(provine)
# quit()
l = list()
driver = webdriver.Chrome()
for href, p in zip(href_list[:3], provine[:3]):
    url = f"https://diemthi.tuyensinh247.com{href}"
    # print(url, p)
    # print(url)
    # print(href_list)
    # url = f"{path}/dc-lop10.html"
    # break
    response_1 = requests.get(url)
    # print(response_1)
    # quit()

    # def open_browser():
    
    driver.get(url)
    driver.execute_script("window.scrollTo(0, 1200)")
    tables = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[1]/div[2]"
    )
    time.sleep(5)
    try:
        tables.find_element(By.XPATH, '//*[@id="view_more"]').click()
    except Exception as e:
        # Logger.error(e, "Error: ")
        print("Error")
    time.sleep(2)
    print("finish")

    soup = BeautifulSoup(driver.page_source, "html.parser")
    # print(soup.text)
    dfx = pd.read_html(driver.page_source)
    df = dfx[0]
    df.columns = df.iloc[0]  # xu ly list to dataframe
    df = df[1:]
    df["tinh"] = p
    print(df)
    # print(pd.read_html(driver.page_source))
    # df.to_csv('testlop10.csv')
    l.append(df)
    
pd.concat(l).to_csv('testlop101.csv')


quit()
link_table = soup.find("div", attrs={"class": "list-schol fl"}) # tìm thẻ div của bảng điểm
print(link_table)


def test(_path):
    url = f"{path}{_path}"
    response = requests.get(url).text        #request get tex
    df = pd.read_html(response)
    dfx = df[0]
    dfx.columns = dfx.iloc[0]
    dfx=dfx[1:]
    return dfx

links = []
title = []
for row in link_table.find_all("li"):       #Lấy dự liệu trong các thẻ li của bảng
    link = row.find("a")
    if link:
        links.append(link["href"]) 
        title.append(link['title'])
        
l2 = []
len_link = len(links)
for i in tqdm(range(len_link)):     #   Lấy tên tỉnh 
    # df = pd.DataFrame(test(i))
    try:
        df = test(links[i])
        df['Tên trường']= title[i]
        l2.append(df)
    except:
        continue
    
dfx = pd.concat(l2)
# print(dfx)




