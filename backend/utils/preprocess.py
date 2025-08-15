'''
Preprocess data module.
'''
import os

import pandas as pd

def load_data(filepath) -> pd.DataFrame:
    '''
    Safely load data from a CSV or Excel file into a DataFrame.
    
    Aegs:
        filepath (str): Path to file.
        
    Returns:
        pd.DataFrame: Loaded DataFrame or an empty one if loading fails.
    '''
    
    if not os.path.exists(filepath):
        print(f'File not found {filepath}')
        return pd.DataFrame()
    
    try:
        if filepath.lower().endswith('csv'):
            df = pd.read_csv(filepath)
        elif filepath.lower().endswith('.xls', '.xlsx'):
            df = pd.read_excel(filepath)
        else:
            print(f'Unsuported file type {filepath}')
            
        return df
    
    except Exception as e:
        print(f'Error loading file: {e}')
        return pd.DataFrame()
    