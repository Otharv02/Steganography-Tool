import base64

def file_to_base64(file_path):
    # rb -> read binary
    # This is to read file in binary mode
    with open(file_path,"rb") as f:  
        return base64.b64encode(f.read()).decode()

def base64_to_file(encoded_data, output_path):
    # wb -> write binary
    # This is to write file in binary mode
    decode = base64.b64decode(encoded_data.encode())
    with open(output_path, "wb") as f:
        f.write(decode)
