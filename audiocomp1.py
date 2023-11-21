import speech_recognition as sr
import pyttsx3


r=sr.Recognizer()
def speechtotext(command):
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
#speechtotext("hagos gebremicheal gebremariam")
with sr.Microphone() as source2:
    r.adjust_for_ambient_noise(source2, duration=2)
    audio2=r.listen(source2)
    mytext=r.recognize_google(audio2)
    
print(f"did you say {mytext}")