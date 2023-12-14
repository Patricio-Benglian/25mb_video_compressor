# 25MB Video Compressor

## To broke for discord nitro? Look no further.
Basically this script allows you to select a file and saves a version with a lowered bitrate so that it's under 25 Megabytes. Currently you run it with

`./compressor.py`


# Requirements:
## ffmpeg
### You can get it here: https://ffmpeg.org/


## ffmpeg-python
### `pip install ffmpeg-python`

<sub><sub><sub>and also obviously you need to install Python</sub></sub></sub>
# Random info

## [tkinter](https://docs.python.org/3/library/tkinter.html)
Tkinter is a GUI (graphical user interface) toolkit. I'm using it to open a window to select your file and another to select the save directory. 

In the future, I could also utilize it to give this script a graphical interface for choosing the files, for selecting the desired filesize and maybe even other things I haven't considered.

## [ffmpeg-python](https://github.com/kkroening/ffmpeg-python)
ffmpeg-python is a python wrapper for ffmpeg, basically allowing you to execute ffmpeg commands with Python code. This is useful because I don't know much about ffmpeg but I do know something about Python.

# [Things to do](https://www.youtube.com/watch?v=GBMSMovYDSw)
- Figure out if I'm being optimal in my filesize reduction (probably not) and how to improve it
- Use tkinter for a GUI
    - Add options for 
        - desired filesize
        - desired codecs?
        - probably something else idk