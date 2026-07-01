# Tools — Multi-Purpose Python Toolkit

A terminal-based, multi-purpose Python toolkit accessible from a single interactive menu.
From downloading YouTube videos and removing image backgrounds to converting between
PDF/JPG formats and adding watermarks, it handles common everyday tasks with one command.

All tools run through the interactive menu in `main.py`, and each tool has its own module,
so they can also be used independently if desired.

---

## Features

| # | Tool | Description |
|---|------|-------------|
| 1 | **YouTube Video Downloader** | Downloads a video in highest/lowest/specific resolution, or audio only. |
| 2 | **QR Code Generator** | Generates a `.png` QR code from a given URL. |
| 3 | **Background Remover** | Removes an image's background using AI (rembg), producing a transparent `.png`. |
| 4 | **PDF → Word Converter** | Converts a PDF file into an editable `.docx` document. |
| 5 | **Watermark Adder** | Adds a **text** or **image** watermark to a picture. |
| 6 | **JPG → PDF Converter** | Converts an image into a `.pdf` file. |
| 7 | **PDF → JPG Converter** | Converts each page of a PDF into separate `.jpg` images. |

---

## Project Structure

```
Tools/
├── main.py                       # Main menu / application entry point
├── youtube_video_downloader.py   # YouTube download functions
├── qr_code_generator.py          # QR code generation
├── background_remover.py         # Image background removal
├── pdf_to_docx.py                # PDF → Word conversion
├── adding_watermark.py           # Text/image watermark adding
├── jpg_to_pdf.py                 # JPG → PDF conversion
├── pdf_to_jpg.py                 # PDF → JPG conversion
├── requirements.txt              # Python dependencies
└── README.md
```

---

## Installation

### Requirements
- **Python 3.10+** (the project uses `match-case`; development environment: Python 3.13)
- `pip` and `venv`

### Steps

```bash
# 1. Clone the repository
git clone <repo-url>
cd Tools

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

> **Note:** On its first run, the background remover (rembg) downloads an AI model; this
> requires an internet connection and may take some time on first use.

---

## Usage

Start the application with the main menu:

```bash
python main.py
```

Then enter the number of the tool you want from the on-screen menu:

```
--- Toolkit Menu ---
 1 - Youtube Video Downloader
 2 - QR Code Generator
 3 - Background Remover of an image
 4 - Convert pdf to word file
 5 - Add watermark to your image
 6 - Convert a jpg to pdf file
 7 - Convert a pdf to jpg images
 8 - Exit
```

### Example Flows

**Downloading a YouTube video**
```
1  →  1 (highest resolution)  →  paste the video link
```

**Generating a QR code**
```
2  →  enter URL  →  enter file name (defaults to "QRcode.png" if left blank)
```

**Adding a text watermark**
```
5  →  image path  →  1  →  watermark text  →  color (black / white)
```

> You can exit the program safely with option `8` in the menu or with `Ctrl+C`.

---

## Output Files

Tools generally save their output to the **source file's directory** using the following naming:

| Tool | Example Output |
|------|----------------|
| Background Remover | `image_removed.png` |
| PDF → Word | `document.docx` |
| Text Watermark | `watermarked_text_image.png` |
| Image Watermark | `watermarked_img_image.png` |
| JPG → PDF | `image.pdf` |
| PDF → JPG | `document_page_1.jpg`, `document_page_2.jpg`, … |
| QR Code | `QRcode.png` (or the name you enter) |

---

## Main Libraries Used

| Library | Purpose |
|---------|---------|
| [pytubefix](https://pypi.org/project/pytubefix/) | YouTube video/audio downloading |
| [qrcode](https://pypi.org/project/qrcode/) | QR code generation |
| [rembg](https://pypi.org/project/rembg/) + onnxruntime | Image background removal |
| [pdf2docx](https://pypi.org/project/pdf2docx/) | PDF → Word conversion |
| [Pillow](https://pypi.org/project/pillow/) | Image processing / watermarking |
| [matplotlib](https://pypi.org/project/matplotlib/) | Previewing watermark results |
| [img2pdf](https://pypi.org/project/img2pdf/) | JPG → PDF conversion |
| [PyMuPDF](https://pypi.org/project/PyMuPDF/) | PDF → JPG conversion |

---

## Notes & Known Limitations

- The **YouTube downloader** can be affected by changes on YouTube's side; if you run into
  issues, update it with `pip install -U pytubefix`.
- The **text watermark** looks for the `arial.ttf` font; if it isn't found, it falls back to
  the system's default font.
- The **image watermark** currently places the overlay at a fixed position (`500, 200`) and
  size (`500x100`).
- Use only in a way that respects copyright and terms of service (e.g. YouTube content).

---

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-tool`)
3. Commit your changes
4. Open a pull request

When adding a new tool: write your module as a separate `.py` file and wire it into the
`main.py` menu as an option.
