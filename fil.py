from pydub import AudioSegment
from pydub.silence import split_on_silence

# Variables for the audio file
# You need to download this file from here: https://etc.usf.edu/lit2go/1/alices-adventures-in-wonderland/1/chapter-i-down-the-rabbit-hole/
file_path = "nu1.wav"
#file_name = file_path.split('/')[-1]
audio_format = "wav"

# Reading and splitting the audio file into chunks
sound = AudioSegment.from_file(file_path, format = audio_format)
audio_chunks = split_on_silence(sound
                            ,min_silence_len = 100
                            ,silence_thresh = -45
                            ,keep_silence = 50
                        )

# Putting the file back together
combined = AudioSegment.empty()
for chunk in audio_chunks:
    combined += chunk
combined.export(f'{file_path }', format = audio_format)