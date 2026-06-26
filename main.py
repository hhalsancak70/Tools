import youtube_video_downloader
import qr_code_generator

print("The tools:")
print(" 1-Youtube Video Downloader")
print(" 2-QR Code Generator")
tool_choice = input("Which tool would you like to use?: ")

if tool_choice == "1":
    print("\nThe options:")
    print(" 1-Download the video with HIGHEST resolution")
    print(" 2-Download the video with LOWEST resolution")
    print(" 3-Download the video with SPECIFIC resolution")
    print(" 4-Download the AUDIO of the video")

    download_choice = input("How do you want to download the video?: ")

    if download_choice in ["1", "2", "3", "4"]:
        link = input("\nEnter the link of the video: ")

        if download_choice == "1":
            youtube_video_downloader.download_video_highest_resolution(link)
        elif download_choice == "2":
            youtube_video_downloader.download_video_lowest_resolution(link)
        elif download_choice == "3":
            print("Video resolution i.e. '720p', '480p', '360p', '240p', '144p'")
            quality = input("Enter the quality of the video: ")
            youtube_video_downloader.download_video_according_to_quality(link, quality)
        elif download_choice == "4":
            youtube_video_downloader.download_sound_of_video(link)
    else:
        print("Invalid choice for download options.")
elif tool_choice == "2":
    url = input("Enter a URL to generate a QR code for it: ")
    file_name = input("Enter a name for your QR code file (without .png): ")

    if file_name.strip() == "":
        qr_code_generator.qr_generator(url)
    else:
        qr_code_generator.qr_generator(url, file_name)
else:
    print("Invalid choice for tools.")