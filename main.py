import os
import youtube_video_downloader
import qr_code_generator
import background_remover
import pdf_to_docx
import adding_watermark
import jpg_to_pdf


def main():
    while True:
        print("\n--- Toolkit Menu ---")
        print(" 1 - Youtube Video Downloader")
        print(" 2 - QR Code Generator")
        print(" 3 - Background Remover of an image")
        print(" 4 - Convert pdf to word file")
        print(" 5 - Add watermark to your image")
        print(" 6 - Convert a jpg to pdf file")
        print(" 7 - Exit")

        try:
            tool_choice = input("Which tool would you like to use? (1-7): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting toolkit. Goodbye!")
            break

        match tool_choice:
            case "1":
                print("\n--- YouTube Options ---")
                print(" 1 - Download with HIGHEST resolution")
                print(" 2 - Download with LOWEST resolution")
                print(" 3 - Download with SPECIFIC resolution")
                print(" 4 - Download the AUDIO only")

                download_choice = input("How do you want to download the video?: ").strip()

                if download_choice in ["1", "2", "3", "4"]:
                    link = input("\nEnter the link of the video: ").strip()

                    match download_choice:
                        case "1":
                            youtube_video_downloader.download_video_highest_resolution(link)
                        case "2":
                            youtube_video_downloader.download_video_lowest_resolution(link)
                        case "3":
                            print("Video resolution i.e. '720p', '480p', '360p', '240p', '144p'")
                            quality = input("Enter the quality of the video: ").strip()
                            youtube_video_downloader.download_video_according_to_quality(link, quality)
                        case "4":
                            youtube_video_downloader.download_sound_of_video(link)
                else:
                    print("Invalid choice for download options.\n")

            case "2":
                url = input("\nEnter a URL to generate a QR code for it: ").strip()
                file_name = input("Enter a name for your QR code file (without .png): ").strip()

                if file_name == "":
                    qr_code_generator.qr_generator(url)
                else:
                    qr_code_generator.qr_generator(url, file_name)

            case "3":
                input_path = input("\nEnter the path of image you want to remove background: ").strip()
                if os.path.exists(input_path):
                    background_remover.remove_background_of_image(input_path)
                else:
                    print(f"Error: File does not exist at '{input_path}'\n")

            case "4":
                input_path = input("\nEnter the path of pdf you want to convert: ").strip()
                if os.path.exists(input_path):
                    pdf_to_docx.convert_to_word(input_path)
                else:
                    print(f"Error: File does not exist at '{input_path}'\n")

            case "5":
                input_path = input("\nEnter the path of the base image: ").strip()

                # Added safety check for the base image
                if os.path.exists(input_path):
                    print(" 1 - Adding Watermark as a text")
                    print(" 2 - Adding Watermark as an image")
                    selection = input("Which option do you want to use: ").strip()

                    match selection:
                        case "1":
                            watermark_text = input("Enter your text to add as a watermark: ").strip()
                            color = input(
                                "Enter the color of your watermark text (Only black or white): ").strip().lower()
                            adding_watermark.adding_watermark_as_a_text(input_path, watermark_text, color)
                        case "2":
                            watermark_image = input("Enter the image path you want to use as a watermark: ").strip()
                            # Added safety check for the watermark image
                            if os.path.exists(watermark_image):
                                adding_watermark.adding_watermark_as_a_image(input_path, watermark_image)
                            else:
                                print(f"Error: Watermark image does not exist at '{watermark_image}'\n")
                        case _:
                            print("Invalid choice.\n")
                else:
                    print(f"Error: Base image file does not exist at '{input_path}'\n")

            case "6":
                input_path = input("\nEnter the path of the base image: ").strip()
                if os.path.exists(input_path):
                    jpg_to_pdf.convert_jpg_to_pdf(input_path)
                else:
                    print(f"Error: File does not exist at '{input_path}'\n")

            case "7":
                print("Exiting toolkit. Goodbye!")
                break

            case _:
                print("Invalid choice. Please select a valid option from the menu.\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting toolkit. Goodbye!")