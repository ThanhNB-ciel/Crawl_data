import pandas as pd
import numpy as np


data_1 = pd.read_csv('tuuyensinh_daihoc.csv',encoding='utf-8')
# data = pd.concat(data_1,data_2)
print(data_1.head())

# data_2 = data_1[(data_1['Năm']==2015) & (data_1['Tỉnh']=='Bắc Giang')]
