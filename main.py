# -*- coding: utf-8 -*-
from flask import Flask,send_from_directory,render_template,request
import os
from werkzeug.utils import secure_filename
from PIL import Image, ImageFilter

ALLOWED_EXTENSIONS = set(['jpg', 'png'])

app = Flask(__name__,static_folder='')
app.config['UPLOAD_FOLDER'] = os.getcwd()

def Trans(input):
    img=Image.open(input)
    img=img.rotate(90)
    input=input.replace("./prediction/","./prediction/new")
    img = img.save(input)
    return input

@app.route('/')
def index():
    return render_template('index.html',name="start")

@app.route('/upload',methods=['POST','GET'])
def upload():
    if request.method =='POST':
        file = request.files['input']
        if file:
            filename = os.path.join('./prediction/', secure_filename(file.filename))
            file.save(filename)
        filename=Trans(filename)
        return render_template('index.html',output=filename)

    return render_template('index.html',name="start")


if __name__ == '__main__':
    app.run(threaded=True,debug=False)