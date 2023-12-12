#!/usr/bin/env python

import ffmpeg
import os
from tkinter import filedialog

def find_file():
  file_path = filedialog.askopenfilename()
  if file_path:
    print(f"Filepath is {file_path}")
  return file_path

def compress(file_path, target_filesize=25):
  pass

def find_save_directory():
  save_directory = filedialog.askdirectory()
  if save_directory:
    print(f"Saving to {save_directory}")
  return save_directory

file_path = find_file()
compress(file_path)
save_directory = find_save_directory()






