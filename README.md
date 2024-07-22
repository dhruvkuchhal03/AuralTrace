# Aural Trace

## Project Description

Aural Trace is a sophisticated audio fingerprinting and recognition system designed to identify music tracks from audio inputs. This project leverages advanced algorithms to analyze and recognize songs from recorded or uploaded audio files. It serves as a useful tool for music enthusiasts, researchers, and developers by providing an easy-to-use interface for audio fingerprinting and song recognition.

Aural Trace solves the problem of identifying unknown music tracks by comparing the audio fingerprints of input files against a pre-existing database of music fingerprints. The project includes functionalities for recording audio, uploading music files, fingerprinting directories of music, and recognizing songs from recorded or uploaded audio clips. It is built using Python and Flask for the web interface, with additional libraries and tools for audio processing and database management.

## Installation Instructions

To install and run Aural Trace, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/dhruvkuchhal03/AuralTrace.git
   cd aural-trace
   ```

2. **Install Dependencies**

   Ensure you have Python 3.x installed. It's recommended to use a virtual environment to manage dependencies. Install `virtualenv` if you don't have it:
   ```bash
   pip install virtualenv
   ```

3. **Set Up Virtual Environment**
   ```bash
   virtualenv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

4. **Install Required Python Packages**
   ```bash
   pip install -r requirements.txt
   ```

5. **Install MySQL**

   If MySQL is not already installed, follow the instructions for your operating system from the [MySQL Installation Guide](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/).

6. **Set Up MySQL Database**
   Start the MySQL server and create the necessary database:
   ```bash
   sudo /usr/local/mysql/support-files/mysql.server start
   mysql -u root -p
   CREATE DATABASE aural;
   ```

7. **Configure the Application**

   Update the `aural.cnf.SAMPLE` file with your database credentials and rename it to `aural.cnf`.

8. **Run MySQL database**
   ```bash
   ./start_mysql.sh
   ```
   and then enter the password.

9. **Run the Application**
    ```bash
    python app.py
    ```
    The application will be accessible at `http://127.0.0.1:5000`.

## Usage

### Command-Line Interface (CLI)

1. **Recording Audio**

   To record a 10-second audio clip:
   ```bash
   python audio_recorder.py output_filename.wav
   ```
   This will save the recording as `output_filename.wav`.

2. **Fingerprinting Music Directory**

   To fingerprint all `.mp3` files in a directory:
   ```bash
   python aural.py --fingerprint /path/to/music_directory .mp3
   ```

3. **Recognizing Audio from File**

   To recognize a song from an audio file:
   ```bash
   python aural.py --recognize file /path/to/audio_file.wav
   ```

### Web Interface

1. **Upload and Fingerprint Music**

   Navigate to `http://127.0.0.1:5000/fingerprint`, select a directory of music files, and click "Fingerprint".

2. **Recognize Uploaded or Recorded Audio**

   Navigate to `http://127.0.0.1:5000/recognize`, upload an audio file, or record a new audio clip for recognition.

### Use Case Flows

#### CLI Use Case Flow

**Scenario:** You have a directory of `.mp3` files you want to fingerprint and later recognize a recorded audio clip.

1. **Fingerprinting Music Directory**
   ```bash
   python aural.py --fingerprint /path/to/music_directory .mp3
   ```

2. **Recording Audio**
   ```bash
   python audio_recorder.py test_clip.wav
   ```

3. **Recognizing Recorded Audio**
   ```bash
   python aural.py --recognize file test_clip.wav
   ```

#### Web Interface Use Case Flow

**Scenario:** You want to upload a music directory for fingerprinting and then recognize a song from an uploaded audio file.

1. **Upload and Fingerprint Music**

   Navigate to `http://127.0.0.1:5000/fingerprint`, select a directory of music files, and click "Fingerprint".

2. **Recognize Uploaded Audio**

   Navigate to `http://127.0.0.1:5000/recognize`, upload an audio file, and click "Recognize".

## Features

- **Audio Fingerprinting:** Generates unique fingerprints for audio files, allowing efficient and accurate music recognition.
- **Song Recognition:** Identifies music tracks from recorded or uploaded audio files.
- **Web Interface:** User-friendly web interface for uploading music files, fingerprinting, and recognizing songs.
- **Audio Recording:** Allows users to record audio directly from the web interface or command line.
- **Detailed Logging:** Logs recognition details for audit and analysis.

### Version 1.0.0

- Initial release with core features for audio fingerprinting and recognition.
- Web interface for uploading, fingerprinting, and recognizing songs.
- Command-line tools for recording, fingerprinting, and recognizing audio.
