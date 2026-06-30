import img2pdf
import os

def convert_jpg_to_pdf(input_path):
    try:
        if not os.path.exists(input_path):
            print(f"\nError: The file '{input_path}' does not exist.\n")
            return

        base_name, _ = os.path.splitext(input_path)
        output_path = f"{base_name}.pdf"

        # img2pdf can take the file path directly
        pdf_bytes = img2pdf.convert(input_path)

        # The 'with' statement automatically closes the file when done
        with open(output_path, "wb") as file:
            file.write(pdf_bytes)

        print(f"Successfully created: {output_path}")

    except Exception as e:
        print(f"\nAn error has occurred during conversion: {e}\n")