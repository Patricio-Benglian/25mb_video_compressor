#!/usr/bin/env python

from tkinter import filedialog

def find_file():
  file_path = filedialog.askopenfilename()
  if file_path:
    print(f"Filepath is {file_path}")
  return file_path

def find_save_directory():
  save_directory = filedialog.askdirectory()
  if save_directory:
    print(f"Saving to {save_directory}")
    return save_directory
  return None