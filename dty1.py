import numpy as np
import matplotlib.pyplot as plot
from scipy import pi
from scipy.fftpack import fft
import librosa as lr
import librosa.display

audio1='had'
y, sr = lr.load('./{}.wav'.format(audio1))
signalAmplitude   = np.sin(y)
plot.subplot(211)
plot.plot(y, signalAmplitude,'bs')
plot.xlabel('time')
plot.ylabel('amplitude')
plot.subplot(212)
plot.magnitude_spectrum(signalAmplitude,Fs=4)
plot.show()

audio2='de'
y, sr = lr.load('./{}.wav'.format(audio2))
signalAmplitude   = np.sin(y)
plot.subplot(211)
plot.plot(y, signalAmplitude,'bs')
plot.xlabel('time')
plot.ylabel('amplitude')
plot.subplot(212)
plot.magnitude_spectrum(signalAmplitude,Fs=4)
plot.show()