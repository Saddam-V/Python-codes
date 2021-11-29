import pyttsx3
engine = pyttsx3.init()
file = open('text.txt','r+')
engine.setProperty('rate', 110)

while(1):
    x = input("enter y for next line\nenter r to repeat the line\nenter e to exit")
    if (x == 'r'):
        engine.say(each)
        print(each)
        engine.runAndWait()
    elif (x == 'y'):
        each = file.readline()
        engine.say(each)
        print(each)
        engine.runAndWait()
    elif(x == 'e'):
        exit()

