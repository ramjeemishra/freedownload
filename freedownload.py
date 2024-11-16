import yt_dlp
import re

def detect_url_type(url):
    youtube_pattern = r"(https?://(?:www\.)?youtube\.com/(?:watch\?v=[\w-]+|shorts/[\w-]+))"
    instagram_pattern = r"(https?://(?:www\.)?instagram\.com/(?:p/[\w-]+|reel/[\w-]+))"
    
    if re.match(youtube_pattern, url):
        return 'YouTube'
    elif re.match(instagram_pattern, url):
        return 'Instagram'
    else:
        return None

def download_video(url, platform):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s', 
        'format': 'best',
    }
    
    if platform == 'YouTube':
        print("Detected YouTube URL. Downloading video...")
    elif platform == 'Instagram':
        print("Detected Instagram URL. Downloading video...")
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error: {e}")
def main():
    url = input("Enter the video URL (Instagram or YouTube): ").strip()
    
    platform = detect_url_type(url)
    
    if platform:
        download_video(url, platform)
    else:
        print("Invalid URL. Please provide a valid Instagram or YouTube video URL.")

if __name__ == "__main__":
    main()
