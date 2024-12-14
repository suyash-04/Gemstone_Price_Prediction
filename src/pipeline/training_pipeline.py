import os
import sys
from src.logger.my_logger import logging
from src.exception.exception import customexception
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation

class TrainingPipeline:
    def start_data_ingestion(self):
        try:
            logging.info("Starting data ingestion process.")
            data_ingestion = DataIngestion()
            train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed. Train path: {train_data_path}, Test path: {test_data_path}")
            return train_data_path, test_data_path
        except Exception as e:
            logging.error("Error in data ingestion step.")
            raise customexception(e, sys)

    def start_data_transformation(self, train_data_path, test_data_path):
        try:
            logging.info("Starting data transformation process.")
            data_transformation = DataTransformation()
            train_arr, test_arr = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
            logging.info("Data transformation completed.")
            return train_arr, test_arr
        except Exception as e:
            logging.error("Error in data transformation step.")
            raise customexception(e, sys)

    def start_model_training(self, train_arr, test_arr):
        try:
            logging.info("Starting model training process.")
            model_trainer = ModelTrainer()
            model_trainer.initiate_model_training(train_arr, test_arr)
            logging.info("Model training completed.")
        except Exception as e:
            logging.error("Error in model training step.")
            raise customexception(e, sys)

    def start_model_evaluation(self, train_arr, test_arr):
        try:
            logging.info("Starting model evaluation process.")
            model_eval = ModelEvaluation()
            model_eval.initiate_model_evaluation(train_arr, test_arr)
            logging.info("Model evaluation completed.")
        except Exception as e:
            logging.error("Error in model evaluation step.")
            raise customexception(e, sys)

    def start_training_pipeline(self):
        try:
            logging.info("Starting the entire training pipeline.")
            train_data_path, test_data_path = self.start_data_ingestion()
            train_arr, test_arr = self.start_data_transformation(train_data_path, test_data_path)
            self.start_model_training(train_arr, test_arr)
            self.start_model_evaluation(train_arr, test_arr)
            logging.info("Training pipeline executed successfully.")
        except Exception as e:
            logging.error("Error in the training pipeline.")
            raise customexception(e, sys)

# Run the training pipeline
if __name__ == "__main__":
    try:
        pipeline = TrainingPipeline()
        pipeline.start_training_pipeline()
    except Exception as e:
        logging.error(f"Pipeline execution failed: {e}")
