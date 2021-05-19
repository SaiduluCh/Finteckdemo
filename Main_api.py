import cv2
import json
import os
import requests
import base64

from flask import Flask, request, jsonify, Response, render_template
from PIL import Image
from io import BytesIO

from google_cloud_demo import ocr

app = Flask(__name__)


UPLOAD_FOLDER = '/static/uploads/'
ALLOWED_EXTENSIONS = set(['png','jpg','jpeg'])
app = Flask(__name__)
app.config['uploadFolder'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):
            
            file = request.files['file'].read()
            decoded_data = base64.b64decode(file)
            image_result = open('deer_decode.jpg', 'wb')  
            image_result.write(file)
            file_path = 'deer_decode.jpg'
            extracted_text = ocr(file_path)
            return jsonify(extracted_text)
            
    elif request.method == 'GET':
        return render_template('upload.html')


if __name__ == '__main__':
    app.run()


if __name__ == "__main__":
    
    app.run(threaded=False)

