#!/usr/bin/env python3

import ffmpeg
import os
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

def compress(file_path):
  print(f"Filepath is {file_path}")

compress(file_path)



