import qrcode
from PIL import Image
from IPython.display import display
def generate_qr_code(data, filename):
    # Create a QR code object with the given data
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Controls the error correction used for the QR Code
        box_size=10,  # Controls how many pixels each box of the QR code is
        border=4,  # Controls how many boxes thick the border should be
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image object from the QR code
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image to a file
    img.save(filename)

# Example usage
data = 'https://www.example.com'
from datetime import datetime
filename = f'qrcode_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
generate_qr_code(data, filename)
print(f'QR code generated and saved as {filename}')
display(img)
