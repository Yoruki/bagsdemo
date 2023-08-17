from PIL import Image
import cv2

a = 90
img = cv2.imread('code.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, a, 255, cv2.THRESH_BINARY)

cv2.imwrite('valuecode.jpg',thresh)