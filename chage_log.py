import pyodbc
import pandas as pd
from clickhouse_driver import Client
from datetime import date, timedelta

[
    "Account ",
    "Account_Activity",
    "Account_LogForBadge",
    "Account_Login",
    "Account_ReadNotiPopup_Log",
    "ActivityType",
    "Answers",
    "Area",
    "BadWord_Report",
    "Badge",
    "BlackList_Account",
    "Level",
    "Notify",
    "PointGiftChange_History",
    "Point_Transction_In",
    "Point_Transction_Out",
    "Question_Topic",
    "Questions",
    "Subjects",
    "Topic",
    "TrakingLog",
    "Ward",
]


def change_log():
    client = Client(
        host="192.168.8.96",
        user="da_team",
        password="Ftech@123",
        settings={"use_numpy": True},
    )
    # Set connection parameters
    server = "192.168.20.137"
    database = "Fschool.QnADB"
    username = "devAI"
    password = "ftech@345&*("
    driver = "{ODBC Driver 17 for SQL Server}"
    port = 1433
    cnxn_str = f"DRIVER={driver};SERVER={server},{port};DATABASE={database};UID={username};PWD={password};charset=utf-16-le"
    cnxn = pyodbc.connect(cnxn_str, encoding="utf-16-le")

    # cursor = cnxn.cursor()
    # query = "select max(transid) transid from Vw_WebSale vws"
    # cursor.execute(query)
    # trans_id = cursor.fetchone()[0]
    table = "Notify"
    df = pd.read_sql(f"select  * from {table} where CreatedDate = '2023-04-14'", cnxn)
    print(df)
    # df.to_csv(f"{table}.csv", index=False)
    # client.insert_dataframe(f"insert into da_cdp_fqa.{table} values ", df)
    print("Update finished!")


change_log()