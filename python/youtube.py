from yt_dlp import YoutubeDL
 
ydl_opts = {'format': 'best'}
with YoutubeDL(ydl_opts) as ydl:
    result = ydl.download(['https://www.youtube.com/watch?v=eALcAWaJRbc'])
    print(result)