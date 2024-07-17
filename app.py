from flask import Flask, request, render_template, redirect, url_for, flash, send_file, jsonify
from werkzeug.utils import secure_filename
import os
import shutil
import time
import subprocess
from aural import Aural
from aural.logic.recognizer.file_recognizer import FileRecognizer

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
LOG_FILE = 'recognition_log.txt'

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

        directory_path = os.path.join(app.config['UPLOAD_FOLDER'], 'fingerprint')
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
        if 'recorded_file' in request.form:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], request.form['recorded_file'])
        elif 'test_file' in request.files and request.files['test_file'].filename != '':
            file = request.files['test_file']
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
        else:
            flash('No file selected or recorded', 'danger')
            return redirect(request.url)

        song = atr.recognize(FileRecognizer, file_path)
        log_recognition_details(file_path, song)
        return render_template('results.html', song=song)
    return render_template('recognize.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/record_audio', methods=['POST'])
def record_audio_route():
    filename = f"output_{int(time.time())}.wav"
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    try:
        subprocess.run(['python', 'audio_recorder.py', file_path], check=True)
        return jsonify(file_name=filename, file_path=url_for('uploaded_file', filename=filename))
    except subprocess.CalledProcessError as e:
        return jsonify(error=str(e)), 500

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))

def log_recognition_details(file_path, song):
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(f"---\nTimestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        log_file.write(f"Input File: {file_path}\n")
        log_file.write(f"File Size: {os.path.getsize(file_path)} bytes\n")
        log_file.write(f"Recognition Results: {song}\n\n")

if __name__ == '__main__':
    app.run(debug=True)