# Eye Tracking Workshop

## INFO
* Requirements: linux, virtualenv, python3.5
* For Dlib see: https://www.pyimagesearch.com/2017/03/27/how-to-install-dlib/



## Installation

### Install the project

_NOTE(1)_: if you are deploying over AWS for training purposes, comment the following packages located in `deploy/requirements.txt`.
```
dlib
PyAutoGUI
PyV4L2Camera
```

_NOTE(1)_: if you have GPU computing power (CUDA), edit `deploy/requirements.txt` and change.

```bash
#tensorflow==1.2.0
tensorflow-gpu==1.2.0
```

```bash
# Go into the desired folder. home?
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
