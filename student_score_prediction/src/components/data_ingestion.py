import os 
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTranformation
from src.components.data_transformation import DataTranformationConfig
from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainConfig


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
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

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
    train_data, test_data = obj.initiate_data_ingestion()

    data_tranformation = DataTranformation()
    train_array,test_array,_ = data_tranformation.initiate_data_transformation(train_data,test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_array,test_array))