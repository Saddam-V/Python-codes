import speech_recognition as sr
from gtts import gTTS
from time import sleep
import os
import pyglet
import wikipedia
import webbrowser
import wolframalpha
import temp as tmp
import pyttsx3
import random
import winsound
import pywhatkit as kt


r = sr.Recognizer()

app_id = '5R5YX2-U9JQ68K8A7'

client = wolframalpha.Client(app_id)

file = open('happy.txt')

# read the content of the file opened
content = file.readlines()
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def SpeakText(text):
    if (text == "hello" or text == "hi"):
        mytext = "Greetings sir!"
        # y = random.choice(list1)
        # x = tmp.emotion()
        # print(x)
        # if(x == "happy"):

        #     mytext = "Good to see you happy!" + \
        #         content[y] + "How can I help you?"
        # elif(x == "sad"):
        #     mytext = "You look sad,"+content[y] + " Can I help you in any way?"
        # elif(x == "neutral"):
        #     mytext = "Too neutral."+content[y] + " How can I help?"
        # elif(x == "excited"):
        #     mytext = "Wow! you are so excited!"+content[y]
    elif 'open youtube' in text:
        webbrowser.open_new_tab("https://www.youtube.com")
        mytext = "Here it is!"

    elif 'open google' in text:
        webbrowser.open_new_tab("https://www.google.com")
        mytext = "There you go! Google is here"

    elif 'open gmail' in text:
        webbrowser.open_new_tab("gmail.com")
        mytext = "Google Mail open now"

    elif 'search for' in text:
        text = text.replace("search for", " ", 10)
        kt.search(text)
        mytext = "Here is your search results"

    elif 'play' in text:
        text = text.replace("play", " ", 4)
        kt.playonyt(text)
        mytext = "Your" + text + " here sir"

    elif ('open notepad' in text) or ('open writingpad' in text) or ('open note' in text):
        os.system("Notepad")
        mytext = "Yes sir!"
    elif ("open vlc" in text) or ("player" in text) or ("video player" in text) or ("vlc" in text):
        os.system("VLC Media Player")
        mytext = "VLC here"
    elif 'shutdown now' in text:
        return os.system("shutdown /s /t 1")
    else:
        try:
            try:
                res = client.query(text)
                mytext = next(res.results).text
            except:
                print("kindly wait while i search wikipedia")
                mytext = wikipedia.summary(text, sentences=2)
        except:
            mytext = "Sorry! Result not found"

    # engine = pyttsx3.init()
    # engine.say(mytext)
    # engine.runAndWait()

    # init function to get an engine instance for the speech synthesis
    engine = pyttsx3.init()

    # change the speech rate
    engine.setProperty('rate', 200)

    # get the available voices
    voices = engine.getProperty('voices')

    # choose a voice based on the voice id
    engine.setProperty('voice', voices[0].id)  # Selected Brian Voice

    # say method on the engine that passing input text to be spoken
    engine.say(mytext)

    # run and wait method, it processes the voice commands.
    engine.runAndWait()

    # language = 'en'

    # myobj = gTTS(text=mytext, lang=language, slow=False)
    # filename = "temp.mp3"
    # myobj.save(filename)

    # music = pyglet.media.load(filename, streaming=False)
    # music.play()

    # sleep(music.duration)
    # os.remove(filename)


while (1):

    try:

        with sr.Microphone() as source2:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source2)
            print("Listening...")
            duration = 70  # milliseconds
            freq = 360  # Hz
            winsound.Beep(freq, duration)
            # audio2 = r.listen(source2)
            audio2 = r.record(source2, duration=4)
            print("Recognizing...")
            MyText = r.recognize_google(audio2, language='en')
            MyText = MyText.lower()

        print("Did you say " + MyText)
        SpeakText(MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print(". . .")
