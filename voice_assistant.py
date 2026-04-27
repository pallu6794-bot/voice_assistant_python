import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command=input("Type your command:")
    return command.lower()
    try:
        with sr.Microphone as source:
          print("Listening...")
        listener.adjust_for_ambient_noise(source)
        audio= listener.listen(source)
    
        command = listener.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
    except Exception as e:
        print("Error:",e)
        command = ""
    return command

def run_assistant():
    command = take_command()

    if 'hello' in command:
        speak("Hello! How can I help you?")

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("Current time is " + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        speak(info)

    elif 'play' in command:
        song = command.replace('play', '')
        speak("Playing " + song)
        pywhatkit.playonyt(song)

    elif 'open google' in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif 'stop' in command or 'exit' in command:
        speak("Goodbye")
        exit()

    else:
        speak("Sorry, I didn't understand.")

while True:
    run_assistant()