import yt_dlp
import re
import os
# import s3fs

# If using s3
# fs = s3fs.S3FileSystem()

ftv_url = "https://www.youtube.com/playlist?list=PLYXOi0ZKJEKKEWl_jgqTTXN9mzvcj4oP0" #FTV
esp_url = "https://www.youtube.com/playlist?list=PLMvsN4LH5cSFtlag_bbqDc76pyetG_4Ol" #ESP

def playlist_scraper (url) : 
    ydl_opts = {'quiet': True, 'extract_flat': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    playlist_dict = {entry['title']: entry for entry in info['entries']}

    # Start from index 340
    entries_to_download = list(playlist_dict.items())[886:]

    for title, entry in entries_to_download:
        # Skip long videos (>25 min)
        if entry.get('duration') and entry['duration'] > 1500:
            continue

        # Safe title for filenames
        safe_title = re.sub(r'[^a-zA-Z0-9_\- ]', '', title)[:100].strip()
        
        local_path = f"/tmp/{safe_title}.webm"
        
        # s3_path = "path"

        ydl_opts = {
            'format': 'bestaudio[ext=webm]',
            'outtmpl': local_path,
            'postprocessors': [],
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([entry['url']])

        # Upload to S3
        # fs.put(local_path, s3_path)

        # Delete local temp file
        # os.remove(local_path)

playlist_scraper(ftv_url)
playlist_scraper(esp_url)