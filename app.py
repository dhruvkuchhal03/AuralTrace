from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
import shutil
from aural import Aural
from aural.logic.recognizer.file_recognizer import FileRecognizer

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

config = {
    "database": {
        "host": "127.0.0.1",
        "user": "root",
        "password": "Dhruv@2003",
        "database": "aural",
    }
}

# Initialize Aural
atr = Aural(config)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fingerprint', methods=['GET', 'POST'])
def fingerprint():
    if request.method == 'POST':
        if 'music_directory' not in request.files:
            flash('No directory selected', 'danger')
            return redirect(request.url)
        files = request.files.getlist('music_directory')
        if not files:
            flash('No files selected', 'danger')
            return redirect(request.url)

        directory_path = os.path.join(
            app.config['UPLOAD_FOLDER'], 'fingerprint')
        if os.path.exists(directory_path):
            shutil.rmtree(directory_path)
        os.makedirs(directory_path)

        for file in files:
            filename = secure_filename(file.filename)
            file.save(os.path.join(directory_path, filename))

        atr.fingerprint_directory(directory_path, [".mp3"], 3)
        flash("Fingerprinting Done!", "success")
        return redirect(url_for('recognize'))
    return render_template('fingerprint.html')


@app.route('/recognize', methods=['GET', 'POST'])
def recognize():
    if request.method == 'POST':
        if 'test_file' not in request.files or request.files['test_file'].filename == '':
            flash('No file selected', 'danger')
            return redirect(request.url)

        file = request.files['test_file']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        song = atr.recognize(FileRecognizer, file_path)
        return render_template('results.html', song=song)
    return render_template('recognize.html')


@app.route('/results')
def results():
    return render_template('results.html')


if __name__ == '__main__':
    app.run(debug=True)
