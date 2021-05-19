import os, io
from google.cloud import vision
import json
from oauth2client.client import GoogleCredentials
from google.cloud.vision import AnnotateImageResponse
import pandas as pd
from re import match
import re
import cv2

list = []

def google_ocr(path): 

	os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="Account_token_key.json"

	client = vision.ImageAnnotatorClient()

	
	root_path = os.path.dirname(os.path.abspath(path))
	
	image_path = os.path.join(root_path, path)

	# print(image_path)


	with io.open(image_path, 'rb') as image_file:
	    content = image_file.read()

	image = vision.Image(content=content)

	response = client.document_text_detection(image=image)

	# print(response)
	response_json = AnnotateImageResponse.to_json(response)
	response = json.loads(response_json)
	text = response['fullTextAnnotation']['text']
	data = json.dumps(text)
	return data


def ocr(image):
	list = []

	image = cv2.imread(image)

	img = cv2.resize(image, (800, 600))

	img2 = img[42:130, 10:430]
	# cv2.imshow('im',img2)
	# cv2.waitKey(0)

	cv2.imwrite('test.png', img2)

	img3 = img[165:273, 593:800]

	cv2.imwrite('test1.png', img3)

	img4 = img[320:500, 500:780]


	cv2.imwrite('test2.png', img4)


	data1 = google_ocr('test.png')
	new_data1 = data1.split("\\n")
	new_data1.remove('"')


	data2 = google_ocr('test1.png')
	new_data2 = data2.split("\\n")
	new_data2.remove('"')


	string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
	if(string_check.search(new_data1[0]) == None) and new_data1[0] != '"Bankof America':
		person_name = (new_data1[0]) 

	else:
		data3 = google_ocr('test2.png')
		new_data3 = data3.split("\\n")
		new_data3.remove('"')
		person_name = (new_data3[0])
		

	for j in new_data2:
		string_check= re.compile('[B-CE-KT-Zb-ce-kt-z@_!/\|}{~]') 
		if(string_check.search(j) == None): 
			amount = j
		

	return [amount,person_name]



