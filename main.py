import tkinter as tk
from tkinter import filedialog, messagebox
from stegano_core import embed_file_in_image, extract_file_from_image

def select_file():
    file_path.set(filedialog.askopenfilename())

def select_image():
    image_path.set(filedialog.askopenfilename(filetypes=[("Image files", "*.png")])) # png only

def save_image():
    output_path.set(filedialog.asksaveasfilename(defaultextension=".png"))

def save_file():
    output_path.set(filedialog.asksaveasfilename(defaultextension=".png"))

def embed():
    try:
        embed_file_in_image(file_path.get(), image_path.get(), output_path.get())
        messagebox.showinfo("Success", "File embeded in image successfully.")
    except Exception as e:
        messagebox.showerror("Error ", str(e))

def extract():
    try:
        extract_file_from_image(image_path.get(), output_path.get())
        messagebox.showinfo("Success","File Extracted successfully.")        
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI 
root = tk.Tk()
root.title("Steganography - Embed & Extract Files")
root.geometry("500x300")

file_path = tk.StringVar()
image_path = tk.StringVar()
output_path = tk.StringVar()

tk.Label(root, text="Select File to Hide").pack()
tk.Entry(root, textvariable=file_path, width=60).pack()
tk.Button(root, text="Browse File", command=select_file).pack()

tk.Label(root, text="Select Carrier Image (PNG)").pack()
tk.Entry(root, textvariable=image_path, width=60).pack()
tk.Button(root, text="Browse Image", command=select_image).pack()

tk.Label(root, text="Output File / Image Path").pack()
tk.Entry(root, textvariable=output_path, width=60).pack()
tk.Button(root, text="Set Output Path", command=save_image).pack()

tk.Button(root, text="Embed File in Image", command=embed).pack(pady=10)
tk.Button(root, text="Extract File from Image", command=extract).pack()

root.mainloop()
