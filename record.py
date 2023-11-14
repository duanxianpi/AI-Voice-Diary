# This Python file uses the following encoding: utf-8
import pyaudio
import wave, os
from PySide6.QtCore import QObject, SignalInstance, Signal, Slot

class record:
    def __init__(self):
        self.CHUNK = 2048
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.signal = Communicate()
        self.stopped = False

    def initPyaduio(self):
        self.p = pyaudio.PyAudio()
        self.signal.finished.emit()

    def record_audio(self, wave_out_path):
        try:
            print(wave_out_path)
            os.makedirs(os.path.dirname(wave_out_path), exist_ok=True)

            self.stream = self.p.open(format=self.FORMAT,
                            channels=self.CHANNELS,
                            rate=self.RATE,
                            input=True,
                            frames_per_buffer=self.CHUNK)

            self.wf = wave.open(wave_out_path, 'wb')
            self.wf.setnchannels(self.CHANNELS)
            self.wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
            self.wf.setframerate(self.RATE)

            print("Start")
            while(not self.stopped):
                data = self.stream.read(self.CHUNK)
                self.wf.writeframes(data)
        except AttributeError:
            pass

    def stopRecording(self):
        self.stopped = True
        self.stream.stop_stream()
        self.stream.close()
        self.wf.close()
        print("End")

    def playRecording(self,wave_out_path):
        self.wf = wave.open(wave_out_path, 'rb')
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                        channels=self.wf.getnchannels(),
                        rate=self.wf.getframerate(),
                        output=True)

        data = self.wf.readframes(self.CHUNK)

        while data != '':
            self.stream.write(data)
            data = self.wf.readframes(self.CHUNK)

        self.stream.stop_stream()
        self.stream.close()

class Communicate(QObject):
    finished = Signal()
