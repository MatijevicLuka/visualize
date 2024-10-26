'''
Constants for styling, colouring, label positioning, default axis text,...
'''

TITLE_GUI: str = 'Plotter'
TITLE_FILE: str = 'plot'
TITLE_GRAPH: str = 'Correlation'

LABEL_X: str = 'X'
LABEL_Y: str = 'Y'
LABEL_Z: str = 'Z'

from enum import Enum

class PositionHorizontal(Enum):
    '''
    Position for labels.
    '''
    LEFT = 'left'
    RIGHT = 'right'
    CENTER = 'center'

class PositionVertical(Enum):
    '''
    Position for labels.
    '''
    TOP = 'top'
    BOTTOM = 'bottom'
    CENTER = 'center'


LABEL_X_POSITION: PositionHorizontal = PositionHorizontal.CENTER
LABEL_Y_POSITION: PositionVertical = PositionVertical.CENTER
# use same position for 'z' as for 'y'
LABEL_Z_POSITION: PositionVertical = PositionVertical.CENTER


class Style(Enum):
    '''
    Plot style.

    You should one of the styles defined inside of this Enum.
    We recommend using the 'usual' styles to keep up with standards
    of writing a scientific journal.

    Not all styles found on Matplotlib docs can be found here.
    We included only the most used styles.

    To check out all styles, visit the following link:
    https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
    '''
    DEFAULT = 'default'
    CLASSIC = 'classic'
    SOLARIZE_LIGHT2 = 'Solarize_Light2'
    BMH = 'bmh'
    DARK_BACKGROUND = 'dark_background'
    FAST = 'fast'
    FIVETHIRTYEIGHT = 'fivethirtyeight'
    GGPLOT = 'ggplot'
    GRAYSCALE = 'grayscale'

style_default = Style.GGPLOT

from dataclasses import dataclass

@dataclass
class Settings:
    '''
    Contains settings for plotting. Specifically, `Style` class, title(s), label(s), ...
    
    All arguments have a default value.
    '''
    style: Style = style_default

    title_file: str = TITLE_FILE
    title_graph: str = TITLE_GRAPH
    
    label_x: str = LABEL_X
    label_y: str = LABEL_Y
    label_z: str = LABEL_Z
    label_x_position: PositionHorizontal = LABEL_X_POSITION
    label_y_position: PositionVertical = LABEL_Y_POSITION
    label_z_position: PositionVertical = LABEL_Y_POSITION
