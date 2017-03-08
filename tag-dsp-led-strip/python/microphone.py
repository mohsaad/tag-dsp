import pyaudio
import config
import time
import scipy.io.wavfile as wavfile
import scipy.signal as signal
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np


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
    filename = 'test30.wav'

    # get single channel
    rate, data = wavfile.read(filename)
    print(rate)
    sd.default.samplerate = rate
    data0 = data[:,0]
    np.savetxt('testspect.csv', data0)

    # loop to get rid
    count = 0
    end = 0
    overlap = int(rate / config.FPS * 0.45)

    # f, t, Sxx = signal.spectrogram(data0, 44100)

    #f = np.log(f)

    # plt.pcolormesh(t, f, Sxx)
    # plt.ylabel('Frequency [Hz]')
    # plt.xlabel('Time [sec]')
    # plt.show()

    sd.play(data0, blocking=False)
    t0 = time.time()
    total_end = 0
    try:
        while end < data0.shape[0]:
            start = count
            end = count + int(config.MIC_RATE / config.FPS)
            if(end > data0.shape[0]):
                break
            callback(data0[start:end])


            count += overlap

    finally:
        t1 = time.time()
        print(t1 - t0)



def oneChannel(fname, chanIdx):
    """ list with specified channel's data from multichannel wave with 16-bit data """
    f = wave.open(fname, 'rb')
    chans = f.getnchannels()
    samps = f.getnframes()
    sampwidth = f.getsampwidth()
    assert sampwidth == 2
    s = f.readframes(samps) #read the all the samples from the file into a byte string
    f.close()
    unpstr = '<{0}h'.format(samps*chans) #little-endian 16-bit samples
    x = list(struct.unpack(unpstr, s)) #convert the byte string into a list of ints
    return x[chanIdx::chans] #return the desired channel
