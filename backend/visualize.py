from constants import *
from data import Data
from utils.preprocess import load_data
from plot_pairwise import stem

import numpy as np
import pandas as pd

if __name__=='__main__':

    my_style = Style.GGPLOT
    settings = Settings(
        style=my_style,
        
        title_file = TITLE_FILE,
        title_graph = TITLE_GRAPH,
        
        label_x = LABEL_X,
        label_y = LABEL_Y,
        label_z = LABEL_Z,
        label_x_position = LABEL_X_POSITION,
        label_y_position = LABEL_Y_POSITION,
        label_z_position = LABEL_Z_POSITION
    )

    filepath = './data/house-price-parquet.csv'
    df = load_data(filepath)

    # print(df)
    print(df.columns.values)
    print(df.index)
    
    # TODO send that data to frontend to show it in a nuxt table
    # enable user to show everything and make plots easily
    # data = Data(data=df, labels=df.columns.values)
    # stem(data=data, settings=settings)
