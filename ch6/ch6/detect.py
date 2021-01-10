"""
Facial recognition specific methods

"""
import cv2


def _boxes(filename, faces):
    print(filename)
    img = cv2.imread(filename)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (100, 100, 255), 2)
    filename = filename.split('/')[-1]
    parts = filename.split('.')
    new_name = '/tmp/%s-detected.%s' % (parts[0], parts[1])
    if img is not None:
        cv2.imwrite(new_name, img)
    return new_name


def faces(filename, ratio=1.2, neighbors=4, min_size=(10, 10)):
    img = cv2.imread(filename, 0)
    hc = cv2.CascadeClassifier(
        '/Users/yxiong/Repository/rabbit-in-depth/ch6/ch6/haarcascade_frontalface_alt.xml')
    return _boxes(filename, hc.detectMultiScale(img, ratio, neighbors,
                                                cv2.CASCADE_SCALE_IMAGE,
                                                min_size))
