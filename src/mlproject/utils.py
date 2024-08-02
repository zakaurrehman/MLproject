import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
import os
from dotenv import load_dotenv
import pymysql 

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    logging.info("Reading SQL database")
    try:
       mydb=pymysql.connect(
           host=host,
           user=user,
           password=password,
           db=db    

       ) 
       logging.info("Connection established", mydb)

       df=pd.read_sql_query('Select * from student',mydb)
       print(df.head())

       return df

    except Exception as ex:
        raise CustomException(ex)


