import pytesseract as tess
from PIL import Image


# Set the Tesseract OCR path
tess.pytesseract.tesseract_cmd = r'C:\Users\UMAIR\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Open the image
img = Image.open('textHand2.png')

try:
    # Use the OCR to extract text from the image
    text = tess.image_to_string(img)

    # Print the extracted text
    print(text)
except Exception as e:
    print(f"An error occurred: {e}")
