#!/usr/bin/python
import os

# FILE FORMAT
FILE_IO_EXT = '.ngqt'

# PIPE
PIPE_WIDTH = 1.2
PIPE_STYLE_DEFAULT = 'line'
PIPE_STYLE_DASHED = 'dashed'
PIPE_STYLE_DOTTED = 'dotted'
PIPE_DEFAULT_COLOR = (127, 149, 151, 255)
PIPE_WAITED_COLOR = (13, 232, 184, 255)
PIPE_ACTIVE_COLOR = (232, 13, 184, 255)
PIPE_HANDSHAKED_COLOR = (60, 100, 20, 255)

PIPE_HIGHLIGHT_COLOR = (232, 184, 13, 255)
PIPE_LAYOUT_STRAIGHT = 0
PIPE_LAYOUT_CURVED = 1

# PORT DEFAULTS
IN_PORT = 'in'
OUT_PORT = 'out'
PORT_ACTIVE_COLOR = (29, 80, 84, 255)
PORT_ACTIVE_BORDER_COLOR = (45, 215, 255, 255)
PORT_HOVER_COLOR = (17, 96, 20, 255)
PORT_HOVER_BORDER_COLOR = (136, 255, 35, 255)


# NODE DEFAULTS
NODE_ICON_SIZE = 24
NODE_SEL_COLOR = (255, 255, 255, 30)
NODE_SEL_BORDER_COLOR = (254, 207, 42, 255)

# NODE GRAPH VIEWER DEFAULTS
VIEWER_BG_COLOR = (35, 35, 35)
VIEWER_GRID_COLOR = (45, 45, 45)
VIEWER_GRID_OVERLAY = True

# GRAPH PATHS
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
ICON_PATH = os.path.join(BASE_PATH, 'widgets', 'icons')
ICON_DOWN_ARROW = os.path.join(ICON_PATH, 'down_arrow.png')
ICON_NODE_BASE = os.path.join(ICON_PATH, 'node_base.png')

# DRAW STACK ORDER
Z_VAL_PIPE = -1
Z_VAL_NODE = 1
Z_VAL_PORT = 2
Z_VAL_NODE_WIDGET = 3

