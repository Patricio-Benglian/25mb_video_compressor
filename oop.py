#!/usr/bin/env python

import ffmpeg
from functools import partial
import os
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk

class Gui_Window:
  """Definition of gui instance"""
  def __init__(self):
    self.file_path = None
    self.save_directory = None
    # Tkinter gfx init
    self.root = tk.Tk() # Create the base window
    self.root.title("Video Compressor")  # Title of the Window
    self.root.geometry("400x250")  # Window launch dimensions

    # Create the widgets

    # Target Filesize Widgets
    self.size_label = tk.Label(self.root, text="Desired Filesize (MB):")
    self.size_label.pack(pady=10, padx=30, anchor="w")

    self.size_slider = ttk.Scale(self.root, from_=8, to=500, length=200, orient="horizontal")
    self.size_slider.set(25)  # Default value
    self.size_slider.pack(pady=10, padx=30, anchor="w")

    # Video Selection Widgets
    self.upload_button = tk.Button(self.root, text="Upload File", command=partial(self.find_file))
    self.upload_button.pack(pady=10, padx=30, anchor="w")

    self.file_label = tk.Label(self.root, text="Selected File: None")  # Needs to update with filename
    self.file_label.pack(pady=10, padx=30, anchor="w")

    # Compression Widget
    self.compress_button = tk.Button(self.root, text="Compressor", command=partial(self.compress))
    self.compress_button.pack(pady=20, padx=30, anchor="w")

    # Loops (like a console)
    # Updates GUI and checks for events (widget updates)
    self.root.mainloop()

  def find_file(self):
    self.file_path = tk.filedialog.askopenfilename()
    if self.file_path:
      print(f"Filepath is {self.file_path}")
    else:
      print("No filepath selected")

    # Temporary measure
    if self.file_path[-4:] != ".mp4":
      print ("Currently only support mp4 :/")
      self.file_path = None
    # Maybe have error text/warning if none selected

  def find_save_directory(self):
    self.save_directory = tk.filedialog.askdirectory()
    if self.save_directory:
      print(f"Saving to {self.save_directory}")
    # Maybe have an error text if none was selected?
    else:
      print("No file selected")

  def compress(self, target_filesize=25):
    if self.file_path == None:
      return
    file_path = self.file_path
    file_info = ffmpeg.probe(file_path)


    # Get duration (mult. by bitrate to get filesize)
    duration = float(file_info["format"]["duration"])

    print(f"Duration: {duration}")

    # Get bitrates
    _video_bitrate = int(file_info["streams"][0]["bit_rate"])
    _audio_bitrate = int(file_info["streams"][1]["bit_rate"])
    total_bitrate = _audio_bitrate + _video_bitrate

    print(
        f"Total Bitrate: {total_bitrate}\n\
    Video Bitrate: {_video_bitrate}\n\
    Audio Bitrate: {_audio_bitrate}"
    )

    # Calculate bitrate ratios
    video_bitrate_ratio = _video_bitrate / total_bitrate
    audio_bitrate_ratio = _audio_bitrate / total_bitrate

    print(f"Video Bitratio: {video_bitrate_ratio}")
    print(f"Audio Bitratio: {audio_bitrate_ratio}")

    # Calculate desired bitrate for target filesize
    # For future reference:
    # *8 to go from bit to byte
    # *1000 to go from byte to kilobyte
    # *1000 to go from kilo to megabyte
    target_bitrate = int(target_filesize * 8 * 1000 * 1000 / duration)
    # Reduce it just a little so it doesn't reach target filesize exactly (Just in case?)
    target_bitrate = int(target_bitrate * 0.95)

    print(
        f"Target Bitrate: {target_bitrate}\n\
    Projected Filesize: {round(target_bitrate * duration / 8 / 1000 / 1000, 2)}"
    )

    # Calculate new bitrate values for desired filesize
    # reducing audio bitrate ruins the audio quickly, quick patch to fix it
    new_video_bitrate = int((target_bitrate * video_bitrate_ratio) - (target_bitrate * audio_bitrate_ratio))
    # new_audio_bitrate = int(target_bitrate * audio_bitrate_ratio)
    new_audio_bitrate = _audio_bitrate

    print(
        f"Total New Bitrate: {new_video_bitrate + new_audio_bitrate}\n\
    New Video Bitrate: {new_video_bitrate}\n\
    New Audio Bitrate: {new_audio_bitrate}"
    )

    # Get filename and designate name for new file
    input_filename = os.path.basename(file_path)
    output_filename = "compr_" + input_filename
    print(f"Filename: {input_filename}")
    print(f"New filename: {output_filename}")

    # Get directory to save to
    self.find_save_directory()
    save_directory = self.save_directory
    if save_directory == None:
        print("No directory selected, exiting...")
        quit()
    # Designate full path to the file created
    output_file_path = os.path.join(save_directory, output_filename)
    print(f"Saving file in: {output_file_path}")

    # Save the new video
    input_vid = ffmpeg.input(file_path)
    output_vid = input_vid.output(
        output_file_path,
        acodec="aac",
        vcodec="h264",
        video_bitrate=new_video_bitrate,
        audio_bitrate=new_audio_bitrate,
        format="mp4",
    )
    ffmpeg.run(output_vid)


if __name__ == "__main__":
  window = Gui_Window()