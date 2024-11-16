import yt_dlp
import re

# Function to detect if URL is from YouTube or Instagram
def detect_url_type(url):
    # Regex pattern for YouTube (standard videos and YouTube Shorts)
    youtube_pattern = r"(https?://(?:www\.)?youtube\.com/(?:watch\?v=[\w-]+|shorts/[\w-]+))"
    
    # Regex pattern for Instagram (posts and Reels)
    instagram_pattern = r"(https?://(?:www\.)?instagram\.com/(?:p/[\w-]+|reel/[\w-]+))"
    
    if re.match(youtube_pattern, url):
        return 'YouTube'
    elif re.match(instagram_pattern, url):
        return 'Instagram'
    else:
        return None

# Function to download the video using yt-dlp
def download_video(url, platform):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',  # Save with the title as the filename
        'format': 'best',  # Download the best quality
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

# Main function to execute the program
def main():
    url = input("Enter the video URL (Instagram or YouTube): ").strip()
    
    platform = detect_url_type(url)
    
    if platform:
        download_video(url, platform)
    else:
        print("Invalid URL. Please provide a valid Instagram or YouTube video URL.")

if __name__ == "__main__":
    main()
