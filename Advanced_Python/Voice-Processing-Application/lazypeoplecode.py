import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning Man !")

    elif hour>=12 and hour<15:
        speak("Good Afternoon Man!")

    elif hour>=15 and hour<20:
        speak("Good Evening Man !")

    elif hour>=20 and hour<24:
        speak("Good Night Man !")

    else:
        speak("Good evening Sir !")

    speak("Hey lazy guy please tell me how may I help you ?")


def takeCommand():
    # it takes microphone input form user and return the string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning Your Voice ......")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    
    try:
        print("Recognizing .....")
   
        query = r.recognize_google(audio, language='en-in')
        print("You Said: ", query)

    except Exception as e:
        print(e)
        print("Sorry man I did not get you. could you please speak again ")
        return "none"
    return query


if __name__ == "__main__":
    
    wishMe()
    
    while True:
        query=takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query= query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences=2)
            print("according to wikipedia")
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'hello' in query:
            speak("Hello Man !")

        elif 'hi' in query:
            speak("Hi Man !")

        elif 'hey' in query:
            speak("Hey Man !")

        elif 'what is your name' is query:
            speak("My name is LazyGuy")

        elif 'how are you' in query:
            speak("I am fine thank you  How do you do ?")

        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'gmail' in query:
            webbrowser.open("gmail.com")

        elif 'facebook' in query:
            webbrowser.open("facebook.com")

        elif 'twitter' in query:
            webbrowser.open("twitter.com")

        elif 'instagram' in query:
            webbrowser.open("instagram.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'github' in query:
            webbrowser.open("github.com")

        elif 'gitlab' in query:
            webbrowser.open("gitlab.com")

        elif 'office' in query:
            webbrowser.open("eclipsia.ets-demo.com")

        elif 'webmail' in query:
            webbrowser.open("webmail.theetsindia.com/Mondo/lang/sys/login.aspx")
        
        elif 'ganna' in query:
            webbrowser.open("gaana.com")

        #elif '' in query:
        #    webbrowser.open()

        elif 'play music' in query:
            music_dir= 'C:\\Users\\ets_designer 2\\Desktop\\jarvis\\Code\\Music'
            songs=os.listdir(music_dir)
            no = random.randrange(1, 8)
            os.startfile(os.path.join(music_dir, songs[no]))
        
        elif 'tell me time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
            
        elif 'open data' in query:
            codePath = "D:\\Kuntal Samanta_ETS-TR0057\\NodeJs\\VS Studio Aftel instal File\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'skype' in query:
            codePath = "C:\\Program Files (x86)\\Microsoft\\Skype for Desktop\\Skype.exe"
            os.startfile(codePath)

        elif 'pycharm' in query:
            codePath = "D:\\Kuntal Samanta_ETS-TR0057\\PyCharm\\PyCharm Community Edition 2017.3.2\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'tata' in query:
            speak('Bye Bye Man Take care !')
            exit(0)

        else:
            print("Sorry man i did not hear any voice, please try again")



