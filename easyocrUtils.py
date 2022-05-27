import easyocr

def reader(img):
    r = easyocr.Reader(['ru'])
    result = r.readtext(img)
    return result