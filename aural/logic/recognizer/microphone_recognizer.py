import numpy as np
import pyaudio

from aural.base_classes.base_recognizer import BaseRecognizer


class MicrophoneRecognizer(BaseRecognizer):
    default_chunksize = 8192
    default_format = pyaudio.paInt16
    default_channels = 2
    default_samplerate = 44100

    def __init__(self, aural):
        super().__init__(aural)
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.data = []
        self.channels = MicrophoneRecognizer.default_channels
        self.chunksize = MicrophoneRecognizer.default_chunksize
        self.samplerate = MicrophoneRecognizer.default_samplerate
        self.recorded = False

    def start_recording(self, channels=default_channels,
                        samplerate=default_samplerate,
                        chunksize=default_chunksize):
        print("* start recording")
        self.chunksize = chunksize
        self.channels = channels
        self.recorded = False
        self.samplerate = samplerate

        if self.stream:
            self.stream.stop_stream()
            self.stream.close()

        try:
            self.stream = self.audio.open(
                format=self.default_format,
                channels=channels,
                rate=samplerate,
                input=True,
                frames_per_buffer=chunksize,
            )
        except OSError as e:
            if e.errno == -9998:
                print("Invalid number of channels, trying with 1 channel")
                self.channels = 1
                self.stream = self.audio.open(
                    format=self.default_format,
                    channels=self.channels,
                    rate=samplerate,
                    input=True,
                    frames_per_buffer=chunksize,
                )
            else:
                raise

        self.data = [[] for _ in range(self.channels)]

    def process_recording(self):
        data = self.stream.read(self.chunksize)
        nums = np.fromstring(data, np.int16)
        for c in range(self.channels):
            self.data[c].extend(nums[c::self.channels])
        print(f"* recording chunk, data length: {len(nums)}")

    def stop_recording(self):
        print("* done recording")
        self.stream.stop_stream()
        self.stream.close()
        self.stream = None
        self.recorded = True

    def recognize_recording(self):
        if not self.recorded:
            raise NoRecordingError("Recording was not complete/begun")
        print("* recognizing recording")
        result = self._recognize(*self.data)
        print("* recognition complete")
        return result

    def get_recorded_time(self):
        return len(self.data[0]) / self.samplerate

    def recognize(self, seconds=10):
        self.start_recording()
        for _ in range(int(self.samplerate / self.chunksize * int(seconds))):
            self.process_recording()
        self.stop_recording()
        return self.recognize_recording()


class NoRecordingError(Exception):
    pass
