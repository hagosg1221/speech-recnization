#Importing library and thir function
from pydub import AudioSegment
from pydub.silence import split_on_silence

#reading from audio mp3 file
sound = AudioSegment.from_wav("two.wav")

# spliting audio files
audio_chunks = split_on_silence(sound, min_silence_len=200, silence_thresh=-40 )

#loop is used to iterate over the output list
for i, chunk in enumerate(audio_chunks):
   output_file = "wo{0}.wav".format(i)
   print("Exporting file", output_file)
   chunk.export(output_file, format="wav")

# chunk files saved as Output