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
# print(list_school)
# list_year = soup
l1 = list_school[0].find_all("li")
href_list = [item.a["href"] for item in l1]
provine = [item.find("strong").text for item in l1]
# year = [item.find("option") for item in l1]
# quit()
# print(provine)
# quit()
l = list()
driver = webdriver.Chrome()
for year in range(2021,2023,1):
    for href, p in zip(href_list, provine):
# href = href_list[0]
# p = provine[0]
# year=2015
        url = f"https://diemthi.tuyensinh247.com{href}?year={year}"

        print(url)

        response_1 = requests.get(url)
        # print(response_1)
        driver.get(url)
        driver.execute_script("window.scrollTo(0, 1300)")
        tables = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[1]/div[2]"
        )
        time.sleep(6)
        try:
            tables.find_element(By.XPATH, '//*[@id="view_more"]').click()
        except Exception as e:
            # Logger.error(e, "Error: ")
            print("Error")
        time.sleep(6)
        print("finish")

        # soup = BeautifulSoup(driver.page_source, "html.parser")
        # print(soup.text)
        dfx = pd.read_html(driver.page_source)
        if dfx:
            df = dfx[0]
            df.columns = df.iloc[0]  # xu ly list to dataframe 
            df = df[1:]
            df["Tỉnh"] = p
            df['Năm'] = year
        print(df)
        l.append(df)
            
pd.concat(l).to_csv('test4.csv',index = False)


# quit()
# link_table = soup.find("div", attrs={"class": "list-schol fl"}) # tìm thẻ div của bảng điểm
# print(link_table)


# def test(_path):
#     url = f"{path}{_path}"
#     response = requests.get(url).text        #request get tex
#     df = pd.read_html(response)
#     dfx = df[0]
#     dfx.columns = dfx.iloc[0]
#     dfx=dfx[1:]
#     return dfx





