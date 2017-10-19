# -*- coding: utf-8 -*-
"""Data utilities to train models.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def load(file_data, file_imgs_left, file_imgs_right): # TODO move params
    """Load preprocessed data from files.
    Returns
    -------
    _ : pandas DataFrame
    _ : images left array
    _ : images right array
    """
    return(
        pd.read_csv(file_data),
        np.load(file_imgs_left+".npy"),
        np.load(file_imgs_right+".npy")
    )


def split(data, imgs_left, imgs_right, validation_size, test_size, random_state=42):
    """Split the augmented data into train, validation and test.
    
    """
    imgs = list(set(data['img'])) # original images, index used to split
    index_not_augmented = data['eye_right_image'].str.endswith('_0.jpg')  # 0 images are the original
    # Test data
    (train_val_imgs, test_imgs) = train_test_split(imgs, train_size=1-test_size, random_state=random_state)
    index_test_augmented = data['img'].isin(test_imgs)
    index_test = index_test_augmented & index_not_augmented
    # Validation data
    (train_imgs, val_imgs) = train_test_split(train_val_imgs, train_size=1-validation_size, random_state=random_state)
    index_val_augmented = data['img'].isin(val_imgs)
    index_val = index_val_augmented & index_not_augmented
    # Train data (augmented)
    index_train = data['img'].isin(train_imgs)
    return(
        (data[index_train], imgs_left[index_train], imgs_right[index_train]),
        (data[index_val], imgs_left[index_val], imgs_right[index_val]),
        (data[index_test], imgs_left[index_test], imgs_right[index_test])
    )
