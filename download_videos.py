from pytube import YouTube
import string

allowed = ''.join([string.ascii_letters + string.digits + '-()'])
def get_clean_title(title):
    new_title = ''        
    for letter in title:
        if letter == ' ':
            new_title += '_'
        if letter not in allowed:
            pass
        else:
            new_title += letter
    return new_title
    
def get_video(URL):
    video_url = URL
    video_object = YouTube(video_url)
    
    best_audio = list(video_object.streams.filter(only_audio=True).order_by('abr'))[-1].itag
    clean_title = get_clean_title(video_object.title)
    stream = video_object.streams.get_by_itag(best_audio)
    stream.download(output_path = 'videos_from_yt', filename = clean_title)
    return clean_title