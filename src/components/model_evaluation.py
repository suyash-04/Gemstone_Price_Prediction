import os
import sys
from src.logger.my_logger import logging
from dataclasses import dataclass
from sklearn.metrics import mean_absolute_error, mean_squared_error
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import pickle 
from src.utils.utils import load_object
from src.exception.exception import customexception

@dataclass
class ModelEvaluationConfig:
    pass
    
    
class ModelEvaluation:
    def __init__(self):
        pass
    
    
    def initiate_model_evaluation(self, train_arr, test_arr):
        try:
            pass
        except Exception as e:
            logging.info("sadasd")
            raise customexception(e, sys)
    