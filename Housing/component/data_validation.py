from Housing.logger import logging
from Housing.exception import HousingException
from entity.config_entitiy import DataValidationConfig
from entity.artifact_entity import DataIngestionArtifact
import os, sys
class Data_Validation:
    def __init__(self, data_validation_config: DataValidationConfig, 
        data_ingestion_artifact: DataIngestionArtifact):
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e
    def is_train_test_files_exists(self)-> bool:
        try:
            logging.info("check whether the train and test file is available or not ")
            is_train_file_exist =False
            is_test_file_exist =False
            
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)

            is_available = is_train_file_exist and is_test_file_exist

            logging.info(f"Is train and test files are available ->{is_available}")
            if not is_available:
                training_file = self.data_ingestion_artifact.train_file_path
                testing_file = self.data_ingestion_artifact.test_file_path 
                message = f"Training file : {training_file} or Testing file : {testing_file}"\
                "is not available"
                logging.info(message)
                raise Exception(message)
            
            return is_available
        
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def validate_dataset_schema(self)-> bool:
        try:
            validate_status = False


            validate_status = True
            return validate_status
        except Exception as e:
            raise HousingException(e,sys) from e
        
   
    def initiate_data_validation(self):
        try:
            self.is_train_test_files_exists()
            self.initiate_data_validation() 
            
        except Exception as e:
            raise HousingException(e,sys) from e
        
