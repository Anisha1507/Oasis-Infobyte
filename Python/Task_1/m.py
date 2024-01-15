import speech_recognition as sr
import pyaudio
import pywhatkit
from gtts import gTTS
from playsound import playsound


def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)

    output.save("sounds/output.mp3")
    playsound("sounds/output.mp3")


def get_audio():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        playsound("sounds/activate.mp3")
        audio = recorder.listen(source)

    text = recorder.recognize_google(audio)
    print(f"You said:{text}")
    return text

text1 = get_audio()

if "youtube" in text1.lower(): 
     speech("Okay, I will open it on youtube for you. Please wait for few seconds.")
     pywhatkit.playonyt(text1)
elif "what" and "about" and "you" in text1.lower():
     speech("I am having a good day. What can I do for you?")
else:
    speech("showing results on google.")
    pywhatkit.search(text1)

     

