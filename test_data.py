import pandas as pd
import numpy as np


# data_1 = pd.read_csv('tuuyensinh_daihoc.csv',encoding='utf-8')
d1 = pd.read_csv('test5.csv')
d2 = pd.read_csv('test4.csv')

data = pd.concat([d1,d2])
print(data.head())
data.to_csv('tuyensinh_lop10.csv')

# data_2 = data_1[(data_1['Năm']==2015) & (data_1['Tỉnh']=='Bắc Giang')]
