import pytesseract
from PIL import Image

# Load image
img = Image.open('test/receipt_1.jpeg') # test image

# OCR read
text = pytesseract.image_to_string(img, config='--psm 6')  # Suitable for single-column text
print(text)
