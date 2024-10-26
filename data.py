import numpy as np
from dataclasses import dataclass

@dataclass
class Data:
    '''
    Data to visualize.
    '''
    x: np.array
    y: np.array
    z: np.array = None