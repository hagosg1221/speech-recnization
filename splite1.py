from pydub import AudioSegment

# start at 0 milliseconds
# end at 1500 65milliseconds
start = 850
end = 1050

sound = AudioSegment.from_wav("la.wav")
extract = sound[start:end]

extract.export("la1.wav", format="wav")