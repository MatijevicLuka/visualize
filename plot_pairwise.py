import matplotlib.pyplot as plt
import numpy as np

from data import Data
from constants import Settings


def stem(data: Data, settings: Settings):
    
       plt.style.use(settings.style.value)
       fig, ax = plt.subplots()
       fig.canvas.manager.set_window_title(title=settings.title_file)

       ax.stem(data.x, data.y)

       ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
              ylim=(0, 8), yticks=np.arange(1, 8))

       ax.set_xlabel(settings.label_x, loc=settings.label_x_position.value)
       ax.set_ylabel(settings.label_y, loc=settings.label_y_position.value)
       
       plt.title(settings.title_graph)
       plt.xlabel(settings.label_x)
       plt.ylabel(settings.label_y)
       
       plt.show()