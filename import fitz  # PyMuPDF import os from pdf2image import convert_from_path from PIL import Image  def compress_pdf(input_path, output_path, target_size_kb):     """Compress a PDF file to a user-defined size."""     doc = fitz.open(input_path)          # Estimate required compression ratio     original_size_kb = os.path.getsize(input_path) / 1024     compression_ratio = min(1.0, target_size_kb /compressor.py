import fitz  # PyMuPDF
import os
from pdf2image import convert_from_path
from PIL import Image

def compress_pdf(input_path, output_path, target_size_kb):
    """Compress a PDF file to a user-defined size."""
    doc = fitz.open(input_path)
    
    # Estimate required compression ratio
    original_size_kb = os.path.getsize(input_path) / 1024
    compression_ratio = min(1.0, target_size_kb / original_size_kb)

    for page in doc:
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Save image with adjusted quality
        img.save("temp.jpg", "JPEG", quality=int(compression_ratio * 100))

        # Convert back to PDF
        new_page = fitz.open()
        new_page.new_page(pix.width, pix.height)
        new_page.insert_image(new_page.rect, filename="temp.jpg")
        new_page.save(output_path)

    os.remove("temp.jpg")
    print(f"✅ PDF compressed successfully! Saved as {output_path}")

if __name__ == "__main__":
    input_pdf = "sample.pdf"
    output_pdf = "output/compressed.pdf"
    target_size = int(input("Enter target size in KB: "))
    compress_pdf(input_pdf, output_pdf, target_size)
