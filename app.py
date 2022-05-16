import os
from flask import Flask, abort, request, jsonify, make_response, send_file
from flask import Flask, render_template
import evaluate_test
from flask_cors import CORS
# r'/*' 是通配符，让本服务器所有的URL 都允许跨域请求
app = Flask(__name__)

CORS(app, resources=r'/*')



@app.route('/')
def index():
    return render_template("index.html")

basedir = os.path.abspath(os.path.dirname(__file__))
@app.route('/up_photo', methods=['post'])
def up_photo():
    img = request.files.get('txt_photo')
    print(img)
    img.filename='53.jpg'
    path = basedir + "/image/"
    file_path = path + img.filename
    img.save(file_path)
    evaluate_test.main()
    image_data = open(os.path.join(basedir + "/test_output_yyyy", '%s' % '53.png'), "rb").read()
    response = make_response(image_data)
    response.headers['Content-Type'] = 'image/png'
    return response
    # result_text = {"statusCode": 200, "message": "文件上传成功"}
    return render_template('index.html')


import base64
@app.route('/upload', methods=['post'])
def upload():
    print(request.files.get('file'))
    print(request.form.get('name'))
    img = request.files.get('file')
    img.filename='53.jpg'
    path = basedir + "/image/"
    file_path = path + img.filename
    img.save(file_path)
    evaluate_test.main()
    # image_data = open(os.path.join(basedir + "/test_output_yyyy", '%s' % '53.png'), "rb").read()
    # image_data=Image.open(basedir + "/test_output_yyyy/53.png")
    # print(image_data)
    # response = make_response(image_data)

    img_stream = ''
    with open(basedir + "/test_output_yyyy/53.png", 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream).decode()
    return img_stream

    # response.headers['Content-Type'] = 'image/png;charset=utf-8'
    return response
    # return send_file(basedir + "/test_output_yyyy", '%s' % '53.png', mimetype='image/gif')
    result_text = {"statusCode": 200, "message": "文件上传成功"}
    return render_template('index.html')


@app.route('/show/<string:filename>', methods=['GET'])
def show_photo(filename):
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if request.method == 'GET':
        if filename is None:
            pass
        else:
            image_data = open(os.path.join(file_dir, '%s' % filename), "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response
    else:
        pass

if __name__ == '__main__':
    app.run()
