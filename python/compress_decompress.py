import base64
import zlib

def compress_string(text):

    if text:
        compressed_data = zlib.compress(text.encode('utf-8'))
        return base64.b64encode(compressed_data).decode('utf-8')  # Encode to Base64 and return as a string
    return ''

def decompress_string(binary_data):
    if binary_data:
        # Decode from Base64 and then decompress using zlib
        compressed_data = base64.b64decode(binary_data)
        return zlib.decompress(compressed_data).decode('utf-8')
    return ''