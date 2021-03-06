from enum import IntEnum, auto
import math

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 600

BUTTON_SIZE = (100, 30)
BUTTON_MARGIN = (10, 10)
BUTTON_BOTTOM_RIGHT = (WINDOW_WIDTH - BUTTON_SIZE[0] - BUTTON_MARGIN[0],
                       WINDOW_HEIGHT - BUTTON_SIZE[1] - BUTTON_MARGIN[1])
BUTTON_BOTTOM_LEFT = (BUTTON_MARGIN[0], WINDOW_HEIGHT - BUTTON_SIZE[1] - BUTTON_MARGIN[1])
BUTTON_STYLE = {'fill': '#090', 'outline': '#090'}
BUTTON_TEXT_STYLE = {'fill': '#fff'}

SUBMENU_STYLE = {'fill': '#9F9', 'outline': '#090'}
DEBUG = True

ANGLE_CHANGE = math.pi/4


def debug(string, **kw):
    if DEBUG:
        print(string, kw)


class Axis(IntEnum):
    HORIZONTAL = 0
    VERTICAL = auto()
    HORIZ = HORIZONTAL
    VERT = VERTICAL


class ControlStates(IntEnum):
    WHOLE = 0
    TOP_LEFT = auto()
    TOP_RIGHT = auto()
    BOTTOM_LEFT = auto()
    BOTTOM_RIGHT = auto()
    CENTER = auto()


class Faces(IntEnum):
    RED = 0
    GREEN = auto()
    ORANGE = auto()
    BLUE = auto()
    YELLOW = auto()
    WHITE = auto()


class Direction(IntEnum):
    CLOCKWISE = 0
    COUNTERCLOCKWISE = auto()
    CW = CLOCKWISE
    CCW = COUNTERCLOCKWISE


class RGB:
    rgb = {0: (1, 0, 0), 1: (0, 1, 0), 2: (1, 176.0 / 255.0, 5.0 / 255.0), 3: (0, 0, 1), 4: (1, 1, 0), 5: (1, 1, 1), }
