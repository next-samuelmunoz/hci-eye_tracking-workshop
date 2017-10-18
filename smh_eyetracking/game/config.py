# -*- coding: utf-8 -*-
"""Constants
"""

from ..config_local import PATH_DATA


#
### CONSTANTS
#

# Space where de user is looking at
SCREEN_WIDTH = 1368
SCREEN_HEIGHT = 768
SCREEN_DIAGONAL =  14  # Not used


# Webcam
WEBCAM_WIDTH = 1280
WEBCAM_HEIGHT = 720
WEBCAM_DEVICE = "/dev/video0"
"""
-NOT USED-
Position of the camera respect to the screen.
Format is XX where X can be:
T: top
B: bottom
C: center
L: left
R: right
"""
WEBCAM_POSITION = 'TC'


#
### game
#

# IMAGES
GAME_IMG_BACKGROUND = 'extras/img/game/bg-sky.jpg'
GAME_IMG_TARGET = 'extras/img/game/target01.png'

# OTHER
GAME_TIME = 60  # Seconds
GAME_FAILS = 5  # Hits a user can fail
GAME_RADIUS = 75.0  # Radius of the target, centered in the image



#
### DATASET: raw
#

PATH_DATA_RAW = PATH_DATA+'/raw'
