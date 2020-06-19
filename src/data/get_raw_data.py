import os
import logging
from kaggle.api.kaggle_api_extended import KaggleApi
from pathlib import Path
import zipfile
import time

def extract_data(raw_data_path, competition, logger):
    logger.info("Authenticating to Kaggle")
    api = KaggleApi()
    api.authenticate()

    logger.info("Downloading raw data at '" + raw_data_path + "'")
    api.competition_download_files(competition, path=raw_data_path)
    
    logger.info("Unzipping raw data file")
    with zipfile.ZipFile(raw_data_path + "/" + competition + ".zip","r") as zip_ref:
        zip_ref.extractall(raw_data_path)

    logger.info("Deleting zipped raw data file")
    os.remove(raw_data_path + "/" + competition + ".zip")
    
def main(project_dir):
    '''
    main method
    '''
    logger = logging.getLogger(__name__)
    logger.info("getting raw data")
    
    # file paths
    raw_data_path = os.path.join(project_dir,'data','raw')
    competition = "titanic"
    extract_data(raw_data_path, competition, logger)
    
if __name__ == '__main__':
    #getting root directory
    project_dir = Path(__file__).parents[2]
    
    #setup logger
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    
    # call the main
    main(project_dir)
