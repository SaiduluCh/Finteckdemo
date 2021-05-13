import easyocr
import cv2

import pytesseract

# config = (' --oem 3 --psm 6')
def imgtodata(im):
	image = cv2.imread(im)
	img = cv2.resize(image, (800, 600))
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(img, (7, 7), 0)
	thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 15)


	img2 = img[500:570, 38:700]
	

	text1 = pytesseract.image_to_string(img2, lang='mcr')
	return text1

# imgtodata('Screenshot-2021-04-06-at-2.06.jpg')
