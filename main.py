# von Kaya an Herr Gürth:

# Hallo Herr Grürth da ich leider spontan krank geworden bin kann ich leider heute nicht erscheinen und sollte es mir nicht besser gehen dann kann ich leider am Freitag auch nicht erscheinen.
# Da ich den Code großteils schon bevor ich Krank geworden bin fertig hatte musste ich nur noch die comments adden und ein paar kleine Äderungen vornehmen.
# Also es läuft alles wunderbar und wie geplant sogar mit einem mini feature undzwar der google Suche, Sie können sich gerne selber davon überzeugen :)
# Ich hoffe der Abdullha hat alle libarys mit dem pip requirements.txt installiert.
# Es gibr nur eine Sache sobald das Internet schlecht ist läuft alles langsamer da das ganze über eine google api rennt.
# Und da gäbe es nochwas undzwar hab ich schon eine tag damit verbracht eine libary namens pyaudio auf meinem mac zu installieren aber erfolgslos da diese libary unter mac nur Probleme bereitet daher musst ich dann auf meinem Windows PC arbeiten.Somit kann Alphi(So hab ich es mal getauft:) nur auf einem Windows PC laufen.
# Falls es noch Probleme geben sollte schreiben Sie dies bitte unter die comments von Herr Gürth an Kaya section!


# von Herr Gürth an Kaya:

#
#
#




import speech_recognition 
import pyttsx3
import subprocess
import pyttsx3
from playsound import playsound
import webbrowser as wb
from socket import *
import os
import time
global engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(f"Voice: {voice.name}")

print("please wait 5-10 seconds.....")
chrome_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome'




import win32com.client as wincl
global speak
speak = wincl.Dispatch("SAPI.SpVoice")
playsound('start2.mp3')
speak.Speak("Hallo ich bin ALPHI ein system das Alphabots über deine Stimme steuern kann. Um mehr zu erfahren sag einfach help.") 


engine.runAndWait()

recognizer = speech_recognition.Recognizer()

while True:

    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()
            
            
            print(f"Recognized {text}")
            
        engine = pyttsx3.init()
            

        if text == "forward":
            playsound('sound5.mp3')
            speak.Speak("Fahre Vorwärts") 
            print("driving forward")

        if text == "backwards":
            playsound('sound5.mp3')
            speak.Speak("Fahre Rückwärts") 
            print("driving backwards")

        if text == "right":
            playsound('sound5.mp3')
            speak.Speak("Fahre Rechts") 

        if text == "left":
            playsound('sound5.mp3')
            speak.Speak("Fahre Links") 

        if text == "exit":
            playsound('sound5.mp3')
            os._exit()

        if text == "help":
                playsound('sound5.mp3')
                speak.Speak("Hallo du kannst den Alphabot mit forward nach vorne fahren lassen, mit backwards nach hinten fahren lassen und mit right, und left, links oder rechts fahren lassen!") 
                speak.Speak("Um Sachen im internet zu suchen, sage einfach internet und dann das was du suchen willst!Bitte beachte das dies nur auf englisch funktioniert!") 
        if text == "internet":
            playsound('sound5.mp3')
            speak.Speak("Bitte sage jetzt was du im web suchen möchtest:") 
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()
                print(f"Recognized {text}")
                time.sleep(1)
                import googlesearch as gs   
                import webbrowser as wb      
                first_link=gs.search(text,num=1,tld="co.in",stop=1,pause=0)  
                for i in first_link:
                    wb.open_new_tab(i)       
    except speech_recognition.UnknownValueError:

        recognizer = speech_recognition.Recognizer()
        continue


       # Herr Gürth ich weiß nicht ob das so stimmt mit dem socket server verbinden und ob man so die variable rüber passen kann.
       # s = socket()
      #  s.connect(('ip', port))
       # s.send(text)

