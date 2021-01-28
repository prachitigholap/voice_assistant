import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


engine.say('I am your assistant')
engine.say('What can I do for you')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():

    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)

            print(command)
    except:
        pass
    return command


def run_assistant():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        talk('current time is' + time)

    elif 'search' in command:
        find = command.replace('search', '')
        talk('searching' + find)
        info = wikipedia.summary(find, 1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('sorry I cant')

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(talk)

    elif 'whatsapp' in command:
        pywhatkit.sendwhatmsg('enter your number here ', 'hi,this msg is sent using python', 22, 9)

    else:
        talk('please say the command again')




while True:
    run_assistant()
