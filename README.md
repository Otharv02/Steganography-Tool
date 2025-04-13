# Steganography Tool

A simple Python-based tool for **hiding files inside images** (specifically PNG files) using **base64 encoding**. This tool allows you to hide sensitive files (such as documents or PDFs) inside an image file's metadata and retrieve them later.

## Features

- **Embed files into PNG images** using base64 encoding.
- **Extract hidden files** from PNG images.
- **Graphical User Interface (GUI)** built with Tkinter for ease of use.
- Supports both file selection and saving using Tkinter's file dialogs.

## Requirements

- Python 3.x
- Tkinter
- Pillow (`PIL`) for image handling

You can install the required dependencies by running:

```bash
pip install pillow
