import wave
import numpy as np
import sys
import matplotlib.pyplot as plt

wav=wave.open("KLTENEW.wav","r")
raw=wav.readframes(-1)
raw=np.frombuffer(raw, "int16")
samplerate=wav.getframerate()
if wav.getnchannels()==1:
    print("the file not supported")
    sys.exit(0)
time=np.linspace(0, len(raw)/samplerate, num=len(raw) )    
plt.title("the wave form of KLTENEW")    
plt.plot(time, raw, color="blue")
plt.ylabel("Amplitude")
plt.show()