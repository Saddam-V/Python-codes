import random
import alphabets as alp
import pyttsx3 as snd
from pynput import keyboard


def callme():
    with keyboard.Events() as events:
        ls=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        random.shuffle(ls)
        x=ls.pop(3)
        print(x)
        y="yes"

        spk = snd.init()
        newvoicerate = 90
        spk.setProperty('rate', newvoicerate)

        event = events.get(1e6)
        if event.key == keyboard.KeyCode.from_char(x):
            alp.draw(x)
            print(end="\n\n")
            #*********************************************************************************
            spk.say(x.upper()+"  ")
            spk.runAndWait()
            #*********************************************************************************
            callme()
        else:
            alp.G()
            alp.A()
            alp.M()
            alp.E()
            print(end="\n\n")
            alp.O()
            alp.V()
            alp.E()
            alp.R()
            print("GAME OVER")
            # *********************************************************************************
            spk.say("GAME OVER   ")
            spk.runAndWait()
            # *********************************************************************************

callme()


