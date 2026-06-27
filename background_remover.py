from rembg import remove
from PIL import Image
import os


def remove_background_of_image(input_path):
    try:
        base_name, _ = os.path.splitext(input_path)
        output_path = f"{base_name}_removed.png"

        input_img = Image.open(input_path)
        output_img = remove(input_img)

        output_img.save(output_path)
        print(f"\nThe background was removed successfully!")
        print(f"File saved as: {output_path}\n")

    except Exception as e:
        print(f"\nAn error has occurred: {e}\n")