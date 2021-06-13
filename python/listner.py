import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random



engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishme():
    hours=int(datetime.datetime.now().hour)
    if hours>=0 and hours<=12:
        engine.say('Good morning')
    elif hours>=12 and hours<18:
        engine.say('Good afternoon') 
    else:
        engine.say('Good evening')   

        
    speak("hey human I am your helper how may i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source) 
        audio = r.listen(source)

    try:  
        print('Recognizing.....')  
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print(e) 

        print("Couldn't get you...Can you please say it again")
        return "None"
    return query    

    


if __name__ == "__main__":
    
    wishme()
    #while True:
    if 1:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            speak(results)

        elif 'open google' in query:
            webbrowser.open('google.com')    

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')    

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com') 

        elif 'play music' in query:
            path = 'D:\\music_dir'
            file = os.path.join(path, random.choice(os.listdir(path)))
            os.startfile(file)
            
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')  
            print(strtime)
            speak(f"buddy the time is : {strtime}")


