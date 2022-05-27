import cv2


def searchNumber(img):
    carplate_img = cv2.imread("./img/"+img)

    carplate_haar_cascade = cv2.CascadeClassifier("./haarcascade_russian_plate_number.xml")

    carplate_overlay = carplate_img.copy()
    carplate_rects = carplate_haar_cascade.detectMultiScale(carplate_overlay, scaleFactor=1.1, minNeighbors=3)

    if len(carplate_rects) == 0:
        return None

    max = 0
    rec = []
    for x, y, w, h in carplate_rects:
        if max < w * h:
            max = w * h
            rec = [x, y, w, h]

    x, y, w, h = rec
    cv2.rectangle(carplate_overlay, (x, y), (x + w, y + h), (0, 0, 255), 5)
    hsv = cv2.cvtColor(carplate_overlay, cv2.COLOR_RGB2HSV)

    carplate_img_gray = cv2.cvtColor(carplate_img, cv2.COLOR_RGB2GRAY)
    sliceNumber = carplate_img_gray[y:y + h, x:x + w]

    sliceNumberBlur = cv2.medianBlur(sliceNumber, 3)
    

    cv2.imwrite("./num_images/number_" + img, sliceNumberBlur)

    return True
