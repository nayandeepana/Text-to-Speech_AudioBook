import win32com.client as wincom
import speech_recognition as sr


speak = wincom.Dispatch("SAPI.SpVoice")
text = input('Enter Text : ')
speak.Speak(text)
r = sr.Recognizer()
with sr.Microphone() as source2:
    r.adjust_for_ambient_noise(source2, duration=0.2)
    r = sr.Recognizer()
    MyText = r.recognize_google(audio0)
    MyText = MyText.lower()
    print("Did you say ",MyText)
    speak.Speak(MyText)