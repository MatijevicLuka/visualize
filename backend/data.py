import numpy as np
from dataclasses import dataclass

@dataclass
class Data:
    '''
    Data to visualize.
    '''
    data: np.array
    labels: list[str]