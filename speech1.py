import wave
import matplotlib.pyplot as plt
import numpy as np
obj=wave.open("he1.wav","rb")
samle_fre=obj.getframerate()
n_sample=obj.getnframes()
signalwave=obj.readframes(-1)
obj.close()
t_audio=n_sample/samle_fre
print(t_audio)
signal_array=np.frombuffer(signalwave, dtype=np.int16)
times=np.linspace(0,t_audio,num=n_sample)
plt.figure(figsize=(15,5))
plt.plot(times,signal_array)
plt.title("audio signal")
plt.ylabel("signal level")
plt.xlabel("times(s)")
plt.xlim(0,t_audio)
plt.show()