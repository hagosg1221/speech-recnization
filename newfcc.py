import numpy as np 
import matplotlib.pyplot as plt 
from glob import glob
import librosa as lr
import librosa.display
wav_path = "lu.wav"
data, fs = librosa.load(wav_path)
# fs is sampling frequency
# sampling frequency nothing but how may samples present for second.
t = np.linspace(0, 0.5, 500)
s = np.sin(40 * 2 * np.pi * t) + 0.5 * np.sin(90 * 2 * np.pi * t)

pfft = np.fft.fft(s)
T = t[1] - t[0]  # sampling interval 
N = s.size

# 1/T = frequency
f = np.linspace(0, 1 / T, N)

plt.ylabel("Amplitude")
plt.xlabel("Frequency [Hz]")
plt.bar(f[:N // 2], np.abs(pfft)[:N // 2] * 1 / N, width=1.5)  # 1 / N is a normalization factor
plt.show()