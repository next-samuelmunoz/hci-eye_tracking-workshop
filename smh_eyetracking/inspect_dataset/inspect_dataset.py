# -*- coding: utf-8 -*-
"""Tool to inspect the raw dataset.
"""

import csv
import traceback

import pygame
from pygame.locals import *
import skimage.io
import skimage.color

from ..features02.utils.features02_dlib import dlib2features,FEATURES
from ..game import config as config_game
from ..keras.predictor import Predictor
from ..utils.data import Data
from ..utils.features_dlib import FeaturesDlib


def get_img_id(game_id, timestamp):
    return '{}_{}'.format(game_id, timestamp)

predictor = Predictor(
    model_name='01_baseline-02',
    screen_width=config_game.SCREEN_WIDTH,
    screen_height=config_game.SCREEN_HEIGHT,
    webcam_width=config_game.WEBCAM_WIDTH,
    webcam_height=config_game.WEBCAM_HEIGHT,
)




FEATURES = [f.split('.')[0] for f in FEATURES] # quit .x .y
def draw_features02(img, features):
    # Points
    for point in [str(x) for x in FEATURES if x.isdigit() ]:
        pygame.draw.circle(
            img, (0,255,0), (features[point+'.x'], features[point+'.y']), 2, 0)
    # Face bounding box
    pygame.draw.rect( # Face
        img, (0,255,0),
        [int(features[x]) for x in ('face.x','face.y','face.width','face.height')],
        3
    )


def loop(data_list):
    pygame.init()
    i_data = 0
    exit = 0
    flag_dot = False
    flag_landmarks = False
    features_dlib = FeaturesDlib()
    flag_predictor = False
    # ds01_key_index = 0
    # Calculate webcam image position
    img = pygame.image.load(data_list[i_data]['img_path'])
    img_w, img_h = img.get_rect().size
    if data_list[i_data]['camera_position'] == 'TC':
        img_pos = ((data_list[i_data]['screen_width']-img_w)/2,0)
    else:
        img_pos = (0,0)

    screen = pygame.display.set_mode(
        (data_list[i_data]['screen_width'],data_list[i_data]['screen_height'])
    )
    while not exit:
        img = pygame.image.load(data_list[i_data]['img_path'])
        print("\n\n-> IMAGE DATA:")
        print(data_list[i_data])
        if flag_landmarks:  # Compute landmarks and show
            try:
                f = features_dlib.extract_features(
                    skimage.util.img_as_ubyte(skimage.color.rgb2gray(
                        skimage.io.imread(data_list[i_data]['img_path'])
                    )),
                )
                landmarks = dlib2features(f)
                draw_features02(img, landmarks)
            except Exception as e:
                print("[WARNING] Exception: {}".format(e))
        screen.fill((0,0,0))
        screen.blit(img, img_pos)
        if flag_dot:  # Show dot
            print("-> LOOKING AT: {},{}".format(data_list[i_data]['x'], data_list[i_data]['y']))
            pygame.draw.circle(screen, (255,0,0), (-data_list[i_data]['x']+data_list[i_data]['screen_width'],data_list[i_data]['y']), 25, 0)
        if flag_predictor: # show prediction
            try:
                print("fails?")
                x,y = predictor.predict(
                    skimage.color.rgb2gray(skimage.io.imread(
                        data_list[i_data]['img_path']
                    ))
                )
                print("-> PREDICTION: {},{}".format(int(x),int(y)))
                pygame.draw.circle(screen, (255,255,0), (-int(x)+config_game.SCREEN_WIDTH,int(y)), 40, 0)
            except Exception as e:
                print("[WARNING] Exception:{}".format(e))
                traceback.print_exc()
        pygame.display.update()
        click = False
        while not click:
            # for event in pygame.event.get():
            event = pygame.event.wait()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    exit = True
                    click = True
                elif event.key == K_RIGHT:
                    if i_data<len(data_list)-1:
                        i_data += 1
                        click = True
                elif event.key == K_LEFT:
                    if i_data>0:
                        i_data -= 1
                        click = True
                elif event.key == K_d: # Switch dot (where the user looks)
                    flag_dot = False if flag_dot else True
                    click = True
                elif event.key == K_l: # Switch landmarks
                    flag_landmarks = False if flag_landmarks else True
                    click = True
                elif event.key == K_p: # Switch predictor
                    flag_predictor = False if flag_predictor else True
                    click = True
            pygame.event.clear()
    pygame.display.quit()



data = Data(config_game.PATH_DATA_RAW)
data_list = list(data.iterate())
if data_list:
    print("NUMBER OF SAMPLES: {}".format(len(data_list)))
    loop(data_list)
else:
    print("No data")
