import cv2

image = cv2.imread('data/images/closing.png')
cv2.imshow('original', image)

closeSize = 3

element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*closeSize, 2*closeSize))
imageClosed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, element, iterations=4)

cv2.imshow('closed image', imageClosed)

cv2.waitKey(0)
cv2.destroyAllWindows()