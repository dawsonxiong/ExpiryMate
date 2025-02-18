import pytesseract
from PIL import Image

def read(path):
    # Load image
    img = Image.open(path)

    # OCR read
    text = pytesseract.image_to_string(img, config='--psm 6')  # Suitable for single-column text
    return

test_path = 'test/receipt_1.jpeg' # test image path
