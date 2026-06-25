from pytubefix import YouTube

def download_sound_of_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_audio_only()
        file_path = stream.download()
        print("The audio has been downloaded successfully.")
        return file_path
    except Exception as e:
        print(f"An error occurred while downloading the audio: {e}")
        return None


def download_video_highest_resolution(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        file_path = stream.download()
        print("The video has been downloaded successfully in highest resolution.")
        return file_path
    except Exception as e:
        print(f"An error occurred while downloading the video: {e}")
        return None


def download_video_lowest_resolution(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_lowest_resolution()
        file_path = stream.download()
        print("The video has been downloaded successfully in lowest resolution.")
        return file_path
    except Exception as e:
        print(f"An error occurred while downloading the video: {e}")
        return None


def download_video_according_to_quality(url, quality):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_by_resolution(quality)

        # Eğer istenen çözünürlükte video yoksa
        if stream is None:
            print(f"Error: The quality '{quality}' is not available for this video.")
            return None

        file_path = stream.download()
        print(f"The video has been downloaded successfully in {quality}.")
        return file_path
    except Exception as e:
        print(f"An error occurred while downloading the video: {e}")
        return None