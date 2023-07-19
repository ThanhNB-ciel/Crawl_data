import boto3
from io import StringIO
import pandas as pd
# from botocore.client import Config


from clickhouse_driver import Client
import csv
clickhouse_info = {
    "host": "103.119.132.171",
    "user": "default",
    "password": "",
    'port' : "9002"
}
client = Client(host=clickhouse_info['host'], port=clickhouse_info['port'], user=clickhouse_info['user'],
                   password=clickhouse_info['password'], settings={
    'use_numpy': True}
)

s3  = boto3.client(
    's3',
    endpoint_url ='http://192.168.1.21:2345/',
    aws_access_key_id = 'minioadmin',
    aws_secret_access_key ='minioadmin',
    # config=Config(signature_version='s3v4'),
    # region_name='us-east-1'  # or your preferred region
)

l_o = s3.list_objects_v2(Bucket="tes1", Prefix="cdp/cdp_1")
dataframes = []
for o in l_o["Contents"]:
    print(o["Key"])

    obj = s3.get_object(Bucket="tes1", Key=o["Key"])["Body"].read().decode("utf-8")
    df = pd.read_csv(StringIO(obj))
    dataframes.append(df)
    # print(df)
    
for dfs in dataframes:
    client.insert_dataframe("insert into thanhnb.test_minio values",dfs.astype(str))
    print(dfs)
    
    


# client.insert_dataframe("insert into thanhnb.chung_khoan values",df)






# import boto3
# import pandas as pd
# from io import StringIO

# def get_dataframe_from_s3():
#     s3 = boto3.client(
#         's3',
#         endpoint_url='http://192.168.1.21:2345/',
#         aws_access_key_id='minioadmin',
#         aws_secret_access_key='minioadmin',
#         # config=Config(signature_version='s3v4'),
#         # region_name='us-east-1'  # or your preferred region
#     )

#     l_o = s3.list_objects_v2(Bucket="tes1", Prefix="cdp/cdp_1")
#     data = []

#     for o in l_o["Contents"]:
#         obj = s3.get_object(Bucket="tes1", Key=o["Key"])["Body"].read().decode("utf-8")
#         df = pd.read_csv(StringIO(obj))
#         data.append(df)
#     return pd.concat(data, ignore_index=True)

# df = get_dataframe_from_s3()
# print(df)









