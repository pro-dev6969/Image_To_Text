
# Task 1 : image to text conversion

import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_path_1 = '1.jpg'
img1 = Image.open(image_path_1)

txt1 = pytesseract.image_to_string(img1)

print(txt1)