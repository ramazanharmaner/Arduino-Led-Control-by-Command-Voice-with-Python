import pyttsx3
import speech_recognition as sr
import controller as cnt


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        audio = r.listen(source)
        try:
            print("Recognize...........")
            query = r.recognize_google(audio, language='en-US')
        except Exception as e:
            print("Make sure you have internet connection...")
            return "None"
        return query
    

if __name__=="__main__":
    while True:
        query = takeCommand().lower()
        if 'light on' in query:
            print("Light On.........")
            speak("Light On.........")
            cnt.led(1)
        elif 'light off' in query:
            print("Light Off...........")
            speak("Light Off...........")
            cnt.led(0)
        elif 'information' in query:
            print("Developed by Ramazan Harmaner.....")
            speak("Developed by Ramazan Harmaner.....")
        elif 'exit' in query:
            print("Have a good one...")
            speak("Have a good one...")
            break


