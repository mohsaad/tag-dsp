import pyaudio
import config
import wave


def start_stream(callback):
    p = pyaudio.PyAudio()


    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=config.MIC_RATE,
                    input=True,
                    frames_per_buffer=int(config.MIC_RATE / config.FPS))
    while True:
        callback(stream)
    stream.stop_stream()
    stream.close()
    p.terminate()


def start_file_stream(callback):
    wf = wave.open('test.wav', 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                input=True)
    while True:
        callback(stream)
    stream.stop_stream()
    stream.close()
    p.terminate()