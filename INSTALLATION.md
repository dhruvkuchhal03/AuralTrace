# Installation of Aural Trace

Aural Trace has been tested on Unix systems. The following dependencies are required for the installation and operation of Aural Trace:

* [`Flask`](https://flask.palletsprojects.com/) for creating the web interface.
* [`SQLAlchemy`](https://www.sqlalchemy.org/) for database ORM.
* [`pymysql`](https://pypi.org/project/PyMySQL/) for interfacing with MySQL databases.
* [`numpy`](https://numpy.org/) for numerical computations.
* [`scipy`](https://www.scipy.org/) for signal processing.
* [`librosa`](https://librosa.org/) for audio and music analysis.
* [`pydub`](https://pydub.com/) for manipulating audio.
* [`sounddevice`](https://python-sounddevice.readthedocs.io/) for recording audio.
* [`wavio`](https://pypi.org/project/wavio/) for handling WAV files.

## Mac OS X

Tested on OS X Mavericks. An option is to install [Homebrew](http://brew.sh) and follow these steps:

1. **Install Homebrew dependencies:**
   ```bash
   brew install portaudio
   brew install ffmpeg
   ```

2. **Install Python packages:**
   ```bash
   sudo easy_install pyaudio
   sudo easy_install pydub
   sudo easy_install numpy
   sudo easy_install scipy
   sudo easy_install pip
   sudo pip install Flask
   sudo pip install SQLAlchemy
   sudo pip install pymysql
   sudo pip install librosa
   sudo pip install sounddevice
   sudo pip install wavio
   ```

3. **Set up MySQL:**
   ```bash
   brew install mysql
   sudo ln -s /usr/local/mysql/lib/libmysqlclient.18.dylib /usr/lib/libmysqlclient.18.dylib
   ```

4. **Clone the Repository:**
   ```bash
   git clone https://github.com/dhruvkuchhal03/AuralTrace.git
   cd aural-trace
   ```

5. **Set Up Virtual Environment:**
   ```bash
   virtualenv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

6. **Create the `requirements.txt` file:**
   Save the following content into a file named `requirements.txt`:
   ```plaintext
   Flask==2.0.2
   SQLAlchemy==1.4.27
   pymysql==1.0.2
   numpy==1.21.4
   scipy==1.7.3
   librosa==0.8.1
   pydub==0.25.1
   sounddevice==0.4.3
   wavio==0.0.4
   ```

7. **Install Required Python Packages:**
   ```bash
   pip install -r requirements.txt
   ```

8. **Set Up MySQL Database:**
   Start the MySQL server and create the necessary database:
   ```bash
   sudo /usr/local/mysql/support-files/mysql.server start
   mysql -u root -p
   CREATE DATABASE aural;
   ```

9. **Configure the Application:**
   Update the `aural.cnf.SAMPLE` file with your database credentials and rename it to `aural.cnf`.

10. **Run MySQL database:**
    ```bash
    ./start_mysql.sh
    ```
    and then enter the password.

11. **Run the Application:**
    ```bash
    python app.py
    ```
    The application will be accessible at `http://127.0.0.1:5000`.

---