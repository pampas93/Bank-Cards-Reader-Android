import cv2
import pytesseract

# Load image
image = cv2.imread('./image.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform OCR using Tesseract
text = pytesseract.image_to_string(gray)

print(text)
