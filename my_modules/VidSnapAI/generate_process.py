# This file looks for new folders inside user_uploads and converts to reels if not already converted
import os
import time
from text_to_audio import text_to_speech_file
import subprocess


# Using Eleven labs text to speech APIs
def text_to_audio(folder):
    print("TTA - ", folder)
    with open(f"user_uploads/{folder}/desc.txt") as f:
        text = f.read()
        print(text, folder)
        text_to_speech_file(text, folder)


# text_to_audio("e6fe882a-8c61-11f0-bd4c-acde48001122")


# Using FFMpeg tool
# https://evermeet.cx/ffmpeg/
def create_reel(folder):
    print("CR - ", folder)
    command = f'''ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf "scale=1080:1920: force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4'''

    subprocess.run(command, shell=True, check=True)


if __name__ == "__main__":

    while True:
        print("Processing Queue...")
        with open("done.txt", "r") as f:
            # done_folders.append(f.readline())
            done_folders = f.readlines()
        done_folders = [f.strip() for f in done_folders]

        folders = os.listdir("user_uploads")

        for folder in folders:
            if (folder not in done_folders):
                # Generate the audio from desc.txt
                text_to_audio(folder)
                # convert the images and audio.mp3 inside the folder to a reel
                create_reel(folder)
                with open("done.txt", "a") as f:
                    f.write(folder + "\n")
        time.sleep(5)
