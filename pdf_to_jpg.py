import os
import fitz


def convert_pdf_to_jpg(input_path):
    try:
        if not os.path.exists(input_path):
            print(f"\nError: The file '{input_path}' does not exist.\n")
            return

        base_name, _ = os.path.splitext(input_path)

        # PDF dosyasını açıyoruz
        doc = fitz.open(input_path)

        print("Converting PDF to images, please wait...")
        # PDF'in her bir sayfasını döngüye alıp resme dönüştürüyoruz
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            output_path = f"{base_name}_page_{page_num + 1}.jpg"
            pix.save(output_path)
            print(f"Saved: {output_path}")

        doc.close()
        print("\nSuccessfully converted PDF to JPG images!\n")

    except Exception as e:
        print(f"\nAn error has occurred during conversion: {e}\n")
        print("Note: Make sure you have PyMuPDF installed via: pip install pymupdf")