import wave
obj=wave.open("hea1.wav","rb")
print("number of chanelles",obj.getnchannels())
print("sample width",obj.getsampwidth())
print("frame rate",obj.getframerate())
print("Number of frames",obj.getnframes())
print("prametres",obj.getparams())
t_audio=obj.getnframes()/obj.getframerate()
print(t_audio)
frames=obj.readframes(-1)
print(type(frames),type(frames[0]))
print(len(frames)/2)
obj.close()
new_obj=wave.open("hea1.wav","wb")
new_obj.setnchannels(2)
new_obj.setsampwidth(2)
new_obj.setframerate(48000)
new_obj.writeframes(frames)
new_obj.close()