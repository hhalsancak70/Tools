from PIL import Image, ImageFont, ImageDraw
import matplotlib.pyplot as plt
import os


def adding_watermark_as_a_text(input_path, watermark_text, color):
    try:
        if not os.path.exists(input_path):
            print(f"\nError: The file '{input_path}' does not exist.\n")
            return

        image = Image.open(input_path)
        watermark_image = image.copy()
        draw = ImageDraw.Draw(watermark_image)

        w, h = image.size
        x, y = int(w / 2), int(h / 2)
        font_size = min(x, y)

        try:
            font = ImageFont.truetype("arial.ttf", int(font_size / 6))
        except IOError:
            font = ImageFont.load_default()

        if color == "black":
            draw.text((x, y), watermark_text, fill=(0, 0, 0), font=font, anchor='ms')
        elif color == "white":
            draw.text((x, y), watermark_text, fill=(255, 255, 255), font=font, anchor='ms')
        else:
            print("We don't have that color.")
            return

        # --- YENİ: Otomatik Kaydetme ---
        output_name = "watermarked_text_" + os.path.basename(input_path)
        watermark_image.save(output_name)
        print(f"\nSuccess: Image saved automatically as '{output_name}'")

        # Görseli ekranda düzgün, ortalanmış olarak gösterme (Subplot kaldırıldı)
        plt.imshow(watermark_image)
        plt.title(f"{color.capitalize()} Text Watermark")
        plt.axis('off')  # Kenardaki sayı eksenlerini gizler, daha şık görünür
        plt.show()

    except Exception as e:
        print(f"\nAn error has occurred during text watermark: {e}\n")


def adding_watermark_as_a_image(input_path, watermark_image_path):
    try:
        if not os.path.exists(input_path):
            print(f"\nError: The base image '{input_path}' does not exist.\n")
            return
        if not os.path.exists(watermark_image_path):
            print(f"\nError: The watermark image '{watermark_image_path}' does not exist.\n")
            return

        base_image = Image.open(input_path)
        watermark = Image.open(watermark_image_path)

        size = (500, 100)
        watermark.thumbnail(size)

        copied_image = base_image.copy()
        copied_image.paste(watermark, (500, 200))

        # --- YENİ: Otomatik Kaydetme ---
        output_name = "watermarked_img_" + os.path.basename(input_path)
        copied_image.save(output_name)
        print(f"\nSuccess: Image saved automatically as '{output_name}'")

        # Resmi göster
        plt.imshow(copied_image)
        plt.title("Image Watermark")
        plt.axis('off')
        plt.show()

    except Exception as e:
        print(f"\nAn error has occurred during image watermark: {e}\n")