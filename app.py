from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig

if __name__=="__main__":
    logging.info("The Execution has Started")

    try:
        #data_ingestion_consfig = DataIngestionConfig()
        data_ingestion =DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)