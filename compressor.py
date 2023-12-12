#!/usr/bin/env python

import ffmpeg
import os
import tkinter as tk
from tkinter import filedialog

# From what I understand, this creates the 'parent' window
# Other windows (filedialog) become child windows of it
root = tk.Tk()
root.withdraw()  # Commenting this out will open filedialog AND the root window

file_path = filedialog.askopenfilename()

def compress(file_path):
  print(f"Filepath is {file_path}")

compress(file_path)





