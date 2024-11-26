from yt_dlp import YoutubeDL
import os

def download_content(url, format_choice, is_playlist, is_channel):
    # Create download directories if they don't exist
    if not os.path.exists("download_video"):
        os.makedirs("download_video")
    if not os.path.exists("download_mp3"):
        os.makedirs("download_mp3")

    # Define output directory based on format, playlist, or channel
    if is_channel:
        output_dir = "download_mp3/%(uploader)s/%(title)s.%(ext)s" if format_choice == '2' else "download_video/%(uploader)s/%(title)s.%(ext)s"
    elif is_playlist:
        output_dir = "download_mp3/%(playlist)s/%(title)s.%(ext)s" if format_choice == '2' else "download_video/%(playlist)s/%(title)s.%(ext)s"
    else:
        output_dir = "download_mp3/%(title)s.%(ext)s" if format_choice == '2' else "download_video/%(title)s.%(ext)s"

    # Define options for audio or video download
    ydl_opts = {
        'format': 'bestaudio/best' if format_choice == '2' else 'best',
        'outtmpl': output_dir,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }] if format_choice == '2' else [],
        'noplaylist': not (is_playlist or is_channel),  # Only download playlists or channels if selected
        'ignoreerrors': True,  # Skip videos with errors and continue the download process
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"Error: {e}")
        print("The link may be incorrect or the content is unavailable. Skipping this video.")

def main():
    while True:
        url = input("Enter the YouTube video, playlist, or channel URL: ").strip()
        # Simple URL validation
        if not url.startswith("http"):
            print("Invalid URL. Please enter a valid YouTube URL.")
            continue

        format_choice = input("Enter '1' for video or '2' for MP3 audio: ").strip()
        if format_choice not in ['1', '2']:
            print("Invalid choice. Please enter '1' for video or '2' for MP3 audio.")
            continue

        # Ask if it's a playlist, channel, or single video
        content_type = input("Is this a (1) single video, (2) playlist, or (3) channel? Enter '1', '2', or '3': ").strip()
        if content_type not in ['1', '2', '3']:
            print("Invalid choice. Please enter '1' for single video, '2' for playlist, or '3' for channel.")
            continue

        is_playlist = content_type == '2'
        is_channel = content_type == '3'

        # For playlists or channels, extract all videos and handle errors individually
        with YoutubeDL({'quiet': True, 'extract_flat': True}) as ydl:
            try:
                info_dict = ydl.extract_info(url, download=False)
                if 'entries' in info_dict:
                    # Playlist or Channel
                    for entry in info_dict['entries']:
                        video_url = entry['url']
                        print(f"Downloading: {video_url}")
                        download_content(video_url, format_choice, is_playlist, is_channel)
                else:
                    # Single video
                    download_content(url, format_choice, is_playlist, is_channel)
                    break  # Exit loop after downloading a single video
            except Exception as e:
                print(f"Error extracting information from {url}: {e}")
                continue  # Skip if there's an issue extracting playlist/channel info

try:
    main()
except KeyboardInterrupt:
    print("\nProcess interrupted by user. Exiting the script.")
