
import argparse

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-b","--behavior",
        help="Set the mouse behavior",
        choices=['move', 'drag2center', 'scroll'],
        default="move",
        type=str
    )
    parser.add_argument("-d","--debug", action='store_true')
    parser.add_argument('model_name',
        help="Name of the model to use",
        type=str
    )
    args = parser.parse_args()

    # Everything is OK
    print("Loading program")


    import os
    import time

    import numpy as np
    import pygame
    from pygame.locals import *


    from ..game import config as config_game
    from ..keras.predictor import Predictor
    from ..utils.webcam_pyv4l2Camera import Webcam

    from . import mouse_behavior


    # Debug mode
    DEBUG = True if args.debug else False

    # Set mouse behavior
    if args.behavior=="drag2center":
        mouse = mouse_behavior.Drag2Center(
            threshold_radius=80,
            radius= config_game.SCREEN_HEIGHT*0.3,
            screen_width=config_game.SCREEN_WIDTH,
            screen_height=config_game.SCREEN_HEIGHT,
            fire_sg=0.5,
            duration=0.7
        )
    elif args.behavior=="scroll":
        mouse = mouse_behavior.Scroll(
            border= int(config_game.SCREEN_HEIGHT/3),
            screen_height=config_game.SCREEN_HEIGHT,
            scroll_move=1,
            fire_sg=0.05,
            # duration=1.5
        )
    else:
        mouse = mouse_behavior.MoveTo(
            threshold_radius=80,
            duration=0.2
        )


    os.nice(10)
    predictor = Predictor(
        model_name=args.model_name,
        screen_width=config_game.SCREEN_WIDTH,
        screen_height=config_game.SCREEN_HEIGHT,
        webcam_width=config_game.WEBCAM_WIDTH,
        webcam_height=config_game.WEBCAM_HEIGHT
    )
    webcam = Webcam(
        config_game.WEBCAM_DEVICE,
        config_game.WEBCAM_WIDTH,
        config_game.WEBCAM_HEIGHT
    )
    if DEBUG:
        pygame.init()
        screen = pygame.display.set_mode(
            (320, 240)
        )
    flag_exit = False
    while not flag_exit:
        try:
            tstamp = time.time()
            img = webcam.get_img()
            if DEBUG:
                s = pygame.transform.scale(
                    pygame.image.fromstring(img.tobytes(), img.size, img.mode),
                    (320,240)
                )
                screen.blit(s,(0,0))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        flag_exit = True
            # Predict postion
            x,y = predictor.predict(
                np.asarray(img.convert('L')).copy()  # To grayscale
            )
            mouse.action(np.array([x,y]))
            if DEBUG:
                print("Loop {}sg".format(time.time()-tstamp))
        except Exception as e:
            print(e)
    webcam.close()
    if DEBUG:
        pygame.display.quit()
