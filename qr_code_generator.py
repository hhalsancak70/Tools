import qrcode

def qr_generator(url, file_name="QRcode"):
    try:
        img = qrcode.make(url)
        save_path = f"{file_name}.png"
        img.save(save_path)
        print(f"The QR code has been generated successfully and saved as '{save_path}'")
    except Exception as e:
        print(f"An error has occurred: {e}. Please check your URL.")