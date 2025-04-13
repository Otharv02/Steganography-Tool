from PIL import Image, PngImagePlugin # PngImagePlugin -> used to embed hiffen data into png
from utils import file_to_base64, base64_to_file

# Embed file into image
def embed_file_in_image(file_path, image_path, output_image_path):
    base64_data = file_to_base64(file_path)
    image       = Image.open(image_path)
    meta        = PngImagePlugin.PngInfo()
    
    meta.add_text("hidden_data", base64_data)
    image.save(output_image_path,  pnginfo = meta) # pnginfo -> allow to add custom meta data

    print(f"File embeded and saved to {output_image_path}")

# Extract file from Image
def extract_file_from_image(image_path, output_file_path):
    image       = Image.open(image_path)
    # It retrieves the hidden metadata stored inside a PNG image
    #  specifically the value associated with the key "hidden_data".
    hidden_data = image.info.get("hidden_data") 
    
    if not hidden_data:
        raise Exception("No data was found in the image.")

    base64_to_file(hidden_data, output_file_path)
    print(f"File extracted and saved to {output_file_path}")



