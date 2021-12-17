from pytube import YouTube
import time
global link
youtube_video_url = input("Enter the link of YouTube video you want to download:  ")
mp = input("Enter the format of the video you want to download (either mp3 or mp4):  ")

if mp == "mp4":
    yt_obj = YouTube(youtube_video_url)
 
    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
 
    # download the highest quality video
    filters.get_highest_resolution().download('/Users/harsh/Downloads')
    print('Video Downloaded Successfully')

else:
    title = YouTube.title
    yt_obj = YouTube(youtube_video_url)

    filters = yt_obj.streams.filter(file_extension='mp3')
 
    yt_obj.streams.get_audio_only().download(output_path="/Users/harsh/Downloads",filename='audio.mp3')
    print('YouTube video audio downloaded successfully')

time.sleep(1.42069)