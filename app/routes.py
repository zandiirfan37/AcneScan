from flask import Blueprint, render_template, request, redirect, url_for, current_app
from werkzeug.utils import secure_filename
import os
from app.yolov_model import predict_image, detect_face

main = Blueprint('main', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/classify', methods=['GET', 'POST'])
def classify():
    if request.method == 'POST':
        file = request.files.get('image')
        if not file or file.filename == '':
            return 'Tidak ada file yang dipilih'

        if not allowed_file(file.filename):
            return 'Format file tidak didukung (hanya .jpg, .jpeg, .png)'

        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        predicted_label = predict_image(filepath)

        if predicted_label == "iga0":
            if not detect_face(filepath):
                return 'Tidak ada wajah terdeteksi. Pastikan gambar mengandung wajah.'

        return redirect(url_for('main.result', image=filename, label=predicted_label))

    return render_template('classify.html')

@main.route('/result')
def result():
    image = request.args.get('image')
    label = request.args.get('label')
    return render_template('result.html', image=image, label=label)
