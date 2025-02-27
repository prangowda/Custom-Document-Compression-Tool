import tkinter as tk
from tkinter import filedialog, messagebox
import os
from compressor import compress_pdf

def select_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        file_label.config(text=f"Selected: {os.path.basename(file_path)}")

def compress_file():
    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return

    target_size = target_size_entry.get()
    if not target_size.isdigit():
        messagebox.showerror("Error", "Enter a valid file size in KB!")
        return

    output_path = os.path.join("output", "compressed.pdf")
    compress_pdf(file_path, output_path, int(target_size))
    messagebox.showinfo("Success", f"Compressed file saved to {output_path}")

# GUI
root = tk.Tk()
root.title("PDF Compressor")
root.geometry("400x250")

file_label = tk.Label(root, text="No file selected")
file_label.pack(pady=10)

select_button = tk.Button(root, text="Select PDF", command=select_file)
select_button.pack()

tk.Label(root, text="Enter Target Size (KB):").pack()
target_size_entry = tk.Entry(root)
target_size_entry.pack()

compress_button = tk.Button(root, text="Compress PDF", command=compress_file)
compress_button.pack(pady=10)

root.mainloop()
