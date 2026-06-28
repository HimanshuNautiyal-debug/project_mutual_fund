import os 
import pandas as pd 
data_path= "data/raw"


def load_data(path_of_data):
    """
    path_of_data: path of the folder where the csv files are stored
    
    Loads the data from the specified path and returns a list of DataFrames.
    And prints basic information about each dataset.
    """
    files=[f for f in os.listdir(path_of_data) if f.endswith('.csv')]

    print(f"{len(files)} Numbers of files found in the directory: {path_of_data}")

    for file in files:
        file_path=os.path.join(path_of_data, file)
        df=pd.read_csv(file_path)
        print(f"Dataset: {file}")
        print(f"Shape: {df.shape}")
        print(f"Columns: {df.columns.tolist()}")
        print(f"Missing Values: {df.isnull().sum().sum()}")
        print("-"*50)
load_data(data_path)
