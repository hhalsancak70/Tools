import youtube_video_downloader

print("The tools:")
print(" 1-Youtube Video Downloader")
tool_choice = input("Which tool would you like to use?: ")

if tool_choice == "1":
    print("\nThe options:")
    print(" 1-Download the video with HIGHEST resolution")
    print(" 2-Download the video with LOWEST resolution")
    print(" 3-Download the video with SPECIFIC resolution")
    print(" 4-Download the AUDIO of the video")

    # KULLANICIDAN CEVABI BURADA ALIYORUZ
    download_choice = input("How do you want to download the video?: ")

    # Kullanıcı geçerli bir seçim yaptıysa linki SADECE BİR KERE soruyoruz
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

else:
    print("Invalid choice for tools.")