import os
import ffmpeg
import string

VIDEOS_URL = 'videos_from_yt'
AUDIOS_URL = 'audios_from_yt'

def convert_video_to_audio(title, encoder):
    stream = ffmpeg.input(f"{VIDEOS_URL}/{title}")
    stream = ffmpeg.output(stream, f"{AUDIOS_URL}/{title}.{encoder}")
    ffmpeg.run(stream)
    os.remove(os.path.join(VIDEOS_URL,title))