import numpy as np
import tkinter as tk
from tkinter import filedialog as fd

from constants import *
from data import Data

if __name__=='__main__':

    root = tk.Tk()
    root.title(TITLE_GUI)

    file = fd.askopenfile(mode='r', title='Select file with data.')

    print(file)

    tk.Label(root, text=f'Graph title (default is `{TITLE_GRAPH}`): ').grid(row=0, column=0, sticky='w')
    title_graph = tk.Entry(root)
    title_graph.grid(row=0, column=1)

    tk.Label(root, text=f'File name (default is `{TITLE_FILE}`): ').grid(row=1, column=0, sticky='w')
    title_file = tk.Entry(root)
    title_file.grid(row=1, column=1)

    tk.Label(root, text=f'X Label (default is `{LABEL_X}`): ').grid(row=2, column=0, sticky='w')
    label_x = tk.Entry(root)
    label_x.grid(row=2, column=1)

    tk.Label(root, text=f'Y Label (default is `{LABEL_Y}`): ').grid(row=3, column=0, sticky='w')
    label_y = tk.Entry(root)
    label_y.grid(row=3, column=1)

    tk.Label(root, text=f'Z Label (default is `{LABEL_Z}`): ').grid(row=4, column=0, sticky='w')
    label_y = tk.Entry(root)
    label_y.grid(row=4, column=1)

    style = Style.GGPLOT

    title_file = TITLE_FILE
    title_graph = TITLE_GRAPH
    label_x = LABEL_X
    label_y = LABEL_Y
    label_z = LABEL_Z
    label_x_position = LABEL_X_POSITION
    label_y_position = LABEL_Y_POSITION
    label_z_position = LABEL_Z_POSITION


    # get data
    x = 0.5 + np.arange(8)
    y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

    data = Data(x,y)


    from plot_pairwise import stem

    settings = Settings(
        style=style,
        title_file=title_file,
        title_graph=title_graph,
        label_x=label_x,
        label_y=label_y,
        label_x_position=label_x_position,
        label_y_position=label_y_position,
        label_z_position=label_z_position,
    )

    stem(data=data, settings=settings)
