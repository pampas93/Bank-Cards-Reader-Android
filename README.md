# Bank-Cards-Reader
A python program using tesseract and OpenCV to extract the vital information like Card Holder's Name, Expiry, Card Number from credit/debit card images, it uses OCR-A template matching for font recognition in openCV with thresholding (to preprocess image) and median blurring (to remove noise) to get the best results

## To run on Mac,
1. `pip install scikit-image pytesseract imutils opencv-python numpy`
2. `brew link tesseract` (requires for pytesseract)
3. `python readCarddetails.py`