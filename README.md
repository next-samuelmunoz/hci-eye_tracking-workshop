# Eye Tracking Workshop


## Installation

Installation tested on Ubuntu.

### System packages

```bash
# Python and virtual environments
apt-get install python3.5 python3.5-dev virtualenv

# Git and makefile
apt-get install git cmake

# Dlib (face detection)
# See: https://www.learnopencv.com/install-dlib-on-ubuntu/
# See: https://www.pyimagesearch.com/2017/03/27/how-to-install-dlib/
apt-get install build-essential cmake pkg-config libx11-dev libatlas-base-dev libgtk-3-dev libboost-all-dev libboost-python-dev

# PyautoGUI (mouse controller)
# See: http://pyautogui.readthedocs.io/en/latest/install.html
apt-get install scrot python3-tk python3-dev
```

### Install the project

_NOTE_: if you are deploying over AWS for training purposes, comment the following packages located in `deploy/requirements.txt`.
```
dlib
PyAutoGUI
PyV4L2Camera
```

_NOTE_: if you have GPU computing power (CUDA), edit `deploy/requirements.txt` and change.

```bash
#tensorflow==1.2.0
tensorflow-gpu==1.2.0
```

```bash
# Go into the desired folder. I.E. home
cd ~
git clone https://github.com/beeva-samuelmunoz/hci-eye_tracking-workshop.git
cd hci-eye_tracking-workshop
make install
```


### Dataset for training
1. Get into the `data` folder and download the [features02_augmented dataset](https://drive.google.com/file/d/0B4BwXne65MbQdWhmNXlFaGdNWjA/view?usp=sharing).

1. Unzip the dataset, it will create the directory `hci-eye_tracking-workshop/data/features02_dlib_augmented`.
```bash
7z x -so features02_dlib_augmented.tar.7z | tar xf -
```

1. There should be 181981 files in the folder.
```bash
ls features02_dlib_augmented | wc -l
```
