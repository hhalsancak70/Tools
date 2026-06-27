import youtube_video_downloader
import qr_code_generator
import background_remover

while True:
    print("--- Toolkit Menu ---")
    print(" 1 - Youtube Video Downloader")
    print(" 2 - QR Code Generator")
    print(" 3 - Background Remover of an image")
    print(" 4 - Exit")

    tool_choice = input("Which tool would you like to use? (1-4): ")

    if tool_choice == "1":
        print("\n--- YouTube Options ---")
        print(" 1 - Download with HIGHEST resolution")
        print(" 2 - Download with LOWEST resolution")
        print(" 3 - Download with SPECIFIC resolution")
        print(" 4 - Download the AUDIO only")

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
            print("Invalid choice for download options.\n")

    elif tool_choice == "2":
        url = input("\nEnter a URL to generate a QR code for it: ")
        file_name = input("Enter a name for your QR code file (without .png): ")

        if file_name.strip() == "":
            qr_code_generator.qr_generator(url)
        else:
            qr_code_generator.qr_generator(url, file_name)

    elif tool_choice == "3":
        input_path = input("\nEnter the path of image you want to remove background: ")
        background_remover.remove_background_of_image(input_path)

    elif tool_choice == "4":
        print("Exiting toolkit. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option from the menu.\n")