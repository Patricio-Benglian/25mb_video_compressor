#!/usr/bin/env python

import ffmpeg
import os
from tkinter import filedialog


def compress(file_path, target_filesize=25):
    file_info = ffmpeg.probe(file_path)
    # print(file_info)

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
    save_directory = find_save_directory()
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


if __name__ == "__main__":
    file_path = find_file()
    compress(file_path)
