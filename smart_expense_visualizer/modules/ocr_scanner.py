# OCR extraction using pytesseract

def scan_bill(image_path):
    import pytesseract
    return pytesseract.image_to_string(image_path)
