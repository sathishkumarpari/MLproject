import os 
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts","train.csv")
    test_data_path: str = os.path.join("artifacts","test.csv")
    raw_data_path: str = os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestionconfig = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("initializing the data ingestion method")
        
        try:
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("Read the dataset from the data source")

            os.makedirs(os.path.dirname(self.ingestionconfig.train_data_path),exist_ok=True)

            df.to_csv(self.ingestionconfig.raw_data_path,index=False,header=True)

            logging.info("splitting the train test dataset")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=27)

            train_set.to_csv(self.ingestionconfig.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestionconfig.test_data_path,index=False,header=True)

            logging.info("The data ingestion is completed")

            return (
                self.ingestionconfig.train_data_path,
                self.ingestionconfig.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()