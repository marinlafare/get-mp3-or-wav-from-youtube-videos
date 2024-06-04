from download_videos import get_video
from remove_audio import convert_video_to_audio
import os

if __name__ == '__main__':
    URL = input('URL please :::  ')
    encoder = input("1 for MP3 2 for WAV :: ")
    if encoder == "1":
        encoder = 'mp3'
    elif encoder == "2":
        encoder = 'wav'
    else:
        print(" Unrecognized encoder, choose 1 for MP3 2 for WAV")

    title = get_video(URL)
    convert_video_to_audio(title, encoder)
    print('AUDIO READY AT audios_from_youtube FOLDER')