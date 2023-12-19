#!/usr/bin/env python

from compressor import compress
import tkinter as tk
from tkinter import ttk


def find_file():
    file_path = tk.filedialog.askopenfilename()
    if file_path:
        print(f"Filepath is {file_path}")
    return file_path


def find_save_directory():
    save_directory = tk.filedialog.askdirectory()
    if save_directory:
        print(f"Saving to {save_directory}")
        return save_directory
    print("No file selected")


# Creates the main window to store widgets in
root = tk.Tk()
root.title("Video Compressor")  # Title of the Window
root.geometry("720x480")  # Window launch dimensions

# Create the widgets

# Target Filesize Widgets
size_label = tk.Label(root, text="Desired Filesize (MB):")
size_label.pack(pady=10, padx=30, anchor="w")

size_slider = ttk.Scale(root, from_=8, to=500, length=200, orient="horizontal")
size_slider.set(25)  # Default value
size_slider.pack(pady=10, padx=30, anchor="w")

# Video Selection Widgets

upload_button = tk.Button(root, text="Upload File", command=find_file)
upload_button.pack(pady=10, padx=30, anchor="w")

file_label = tk.Label(root, text="Selected File: None")  # Needs to update with filename
file_label.pack(pady=10, padx=30, anchor="w")

# Compression Widget
compress_button = tk.Button(root, text="Compressor", command=compress)
compress_button.pack(pady=20, padx=30, anchor="w")

# Loops (like a console)
# Updates GUI and checks for events (widget updates)
root.mainloop()
