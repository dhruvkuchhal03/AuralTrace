import pyaudio
import wave
import time
import sys

def record_audio(output_filename):
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1  # Using 1 channel for mono
    fs = 48000  # Increase sample rate to 48000 samples per second
    seconds = 10

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    try:
        print('Recording')

        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=fs,
                        frames_per_buffer=chunk,
                        input=True)

        frames = []  # Initialize array to store frames

        # Store data in chunks for 10 seconds
        for _ in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        # Stop and close the stream
        stream.stop_stream()
        stream.close()

        print('Finished recording')

        # Save the recorded data as a WAV file
        wf = wave.open(output_filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()

        print(f'Saved recording as {output_filename}')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Terminate the PortAudio interface
        p.terminate()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python audio_recorder.py <output_filename>")
        sys.exit(1)
    output_filename = sys.argv[1]
    record_audio(output_filename)