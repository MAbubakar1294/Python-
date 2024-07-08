import speech_recognition as sr
import webbrowser
import pyttsx3
import naatLibr


recognizer =sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkdin" in c.lower():
        webbrowser.open("https://linkdin.com")
    elif c.lower().startswith("play"):
        naat = c.lower().split(" ")[1]
        link = naatLibr.naats[naat]
        webbrowser.open(link)

    else:
        pass

if __name__ == "__main__":
    speak("Initializing Jarvis")
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        


        print("recognizing...")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)

            if(word.lower() == "jarvis"):
                speak("ya")
                #listen for command
                with sr.Microphone() as source:
                    print("jarvis active ...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        
        except Exception as e:
            print("Error; {0}".format(e))
    