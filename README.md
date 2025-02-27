### **📂 PDF/Document Size Compressor (Custom Compression Level)**
A Python-based tool that allows users to **custom compress PDF and document files** to a specified file size while maintaining readability.  

---

## **📌 Features**  
✔ **Custom Compression** – User specifies desired file size.  
✔ **PDF & Document Support** – Compresses PDFs and images in documents.  
✔ **Quality Retention** – Optimized to maintain readability.  
✔ **Multiple Compression Levels** – High, Medium, Low, Custom.  
✔ **Batch Processing** – Compress multiple files at once.  

---

## **🛠️ Technologies Used**  
| **Technology**  | **Purpose**  |  
|-----------------|-------------|  
| **Python**  | Core logic for compression |  
| **PyMuPDF (fitz)**  | PDF compression |  
| **pdf2image**  | PDF to image conversion |  
| **Pillow (PIL)**  | Image compression |  
| **Tkinter**  | User interface |  

---

## **📂 Project Structure**  

```
/PDFCompressor
│── compressor.py        # Main script for compression
│── gui.py               # GUI for user input
│── requirements.txt     # Dependencies
│── README.md            # Documentation
│── sample.pdf           # Sample PDF for testing
│── output/              # Compressed files saved here
```

## **🛠️ How to Run the Project**  
1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/prangowda/PDFCompressor.git
cd PDFCompressor
```

2️⃣ **Install Dependencies**  
```sh
pip install -r requirements.txt
```

3️⃣ **Run the GUI**  
```sh
python gui.py
```

---

## **🚀 How It Works?**  
✅ **Select a PDF file** using the UI  
✅ **Enter the target size** (e.g., 500 KB)  
✅ **Click Compress** – The file is optimized and saved in `/output/`  

---

## **🔮 Future Enhancements**  
✔ Support for **DOCX, PNG, JPG**  
✔ **Cloud Upload** for compressed files  
✔ **OCR Support** to retain text in images  
