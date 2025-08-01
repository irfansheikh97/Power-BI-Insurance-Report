import pandas as pd
from sqlalchemy import create_engine



conn_string = "mysql+mysqldb://{username}:{password}@{host}/{db_name}".format(username="root",
                                                                              password="root",
                                                                              host="localhost",
                                                                              db_name="insurance_db")

try:
    conn = create_engine(conn_string)
    if conn:
        df = pd.read_csv("InsuranceData.csv", parse_dates=['PolicyStartDate', 'PolicyEndDate', 'ClaimDate'])
        # print(df.head())
        # print()
        # print(df.info())
        df.to_sql("insurancedata", con=conn, if_exists='replace', index=False)
        print("Data Loaded to Database")
except ConnectionError as e:
    print("Failed to Connect DB")
    