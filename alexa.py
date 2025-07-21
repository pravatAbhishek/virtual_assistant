import pyttsx3
import webbrowser
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait() 


speak("Initialising alexa")

def processCommand(c):
    c = c.lower()

    if "google" in c:
        webbrowser.open("https://google.com")
    elif "gold" in c:
        webbrowser.open("https://in.tradingview.com/chart/v1a0nCYb/?symbol=FOREXCOM%3AXAUUSD")
    elif "forex factory" in c:
        webbrowser.open("https://www.forexfactory.com/")
    elif "music" in c:
        webbrowser.open("https://www.youtube.com/watch?v=4etXyEu9jxA&list=RD4etXyEu9jxA&start_radio=1")
    elif "youtube" in c:
        webbrowser.open("https://youtube.com")
    else:
        speak("Searching that on Google")
        query = c.replace(" ", "+")
        webbrowser.open(f"https://www.google.com/search?q={query}")


while True:
    
    r = sr.Recognizer()
  
    print("recognizing...")

    try:
        with sr.Microphone() as source:
            print("listening")
            audio = r.listen(source, timeout=2,phrase_time_limit=1)

        word = r.recognize_google(audio)
        if word.lower() == "alexa":
            speak("alexa activated")

            with sr.Microphone() as source:
                print("alexa active")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                processCommand(command)

    except Exception as e:
        print("error")
