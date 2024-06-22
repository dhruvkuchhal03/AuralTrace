# Aural: Audio Fingerprinting and Recognition Algorithm

## Description

Aural is an audio fingerprinting and recognition algorithm implemented in Python. It can memorize audio by listening to it once and fingerprinting it. By playing a song and recording microphone input or reading from disk, Aural matches the audio against the fingerprints held in the database, returning the song being played.

## Features

- Memorizes and fingerprints audio by listening to it once.
- Matches live recordings or disk files against the stored fingerprints.
- Supports MySQL and Postgres databases.
- Robust against noise.
  Note: For voice recognition, Aural is not the right tool! Aural excels at recognition of exact signals with reasonable amounts of noise.

## Installation

### Requirements

- Python 3.x
- MySQL or Postgres

### Steps

1. Clone the repository:
   ```bash
   git clone xxx
   cd aural
   ```
2. Install Flask:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install Flask pydub==0.23.1 PyAudio==0.2.11 numpy==1.17.2 scipy==1.3.1 matplotlib==3.1.1 mysql-connector-python==8.0.17 psycopg2-binary
   ```
3. Set up the SQL database:
   ```bash
   mysql -u root -p
   Enter password: **********
   mysql> CREATE DATABASE IF NOT EXISTS aural;
   ```

### Running the Program

1. For SQL, run `./start_mysql.sh` and then enter the password.
2. For the main project, install Flask and then run:

```
python3 app.py
```

# Usage

## Fingerprinting

1. Create an Aural object with your configuration settings:

```python
from aural import Aural

config = {
    "database": {
        "host": "127.0.0.1",
        "user": "root",
        "password": "<password>",
        "database": "<database name>",
    }
}
atr = Aural(config)
```

2. Fingerprint all audio files in a directory:

```python
atr.fingerprint_directory("va_us_top_40/mp3", [".mp3"], 3)
```

## Recognizing

1. Recognize audio from a file:

```python
from aural.logic.recognizer.file_recognizer import FileRecognizer
song = atr.recognize(FileRecognizer, "va_us_top_40/wav/Mirrors - Justin Timberlake.wav")
```

2. Recognize audio through a microphone:

```python
from aural.logic.recognizer.microphone_recognizer import MicrophoneRecognizer
song = atr.recognize(MicrophoneRecognizer, seconds=10) # Defaults to 10 seconds.
```

# Project Status

Active - Development is ongoing. Contributions are welcome.

# Conclusion

Aural is a robust audio fingerprinting and recognition tool that allows you to identify songs by their audio fingerprints. It supports both file-based and microphone-based recognition, making it versatile for various applications.
