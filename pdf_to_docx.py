from pdf2docx import Converter
import os

def convert_to_word(input_path):
    try:
        if not os.path.exists(input_path):
            print(f"\nError: The file '{input_path}' does not exist.\n")
            return

        base_name, _ = os.path.splitext(input_path)
        output_path = f"{base_name}.docx"

        print(f"\nStarting conversion: {input_path} -> {output_path}")
        cv = Converter(input_path)
        cv.convert(output_path)
        cv.close()
        print("Conversion completed successfully!\n")

    except Exception as e:
        print(f"\nAn error has occurred during conversion: {e}\n")