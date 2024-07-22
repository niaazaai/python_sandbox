from pytube import YouTube

def download_youtube_video(url, resolution):
    try:
        # Create YouTube object
        yt = YouTube(url)

        # Filter streams by resolution
        streams = yt.streams.filter(res=resolution, file_extension='mp4')

        # Check if any stream is available for the specified resolution
        if streams:
            # Get the first stream found
            video_stream = streams.first()
            print(f"Downloading: {yt.title} at {resolution}")
            # Download the video
            video_stream.download()
            print("Download completed!")
        else:
            print(f"No streams found for the specified resolution: {resolution}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input the YouTube video URL and desired resolution
    video_url = input("Enter the YouTube video URL: ")
    desired_resolution = input("Enter the desired resolution (e.g., '720p', '1080p'): ")

    download_youtube_video(video_url, desired_resolution)
