import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import json
import datetime
import wikipedia
import pyjokes

name = "nati"
key = "AIzaSyBCcg-ARS5ULSTRoK3idtKai49N6qXyBGc"
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, "")
                print(rec)
    except:
        pass
    return rec

def run():
    rec = listen()
    if "reproduce" in rec:
        music = rec.replace("reproduce", "")
        talk("Reproduciendo " + music)
        pywhatkit.playonyt(music)
    elif "cuantos subcriptores tiene" in rec:
        susb = rec.replace("cuantos subcriptores tiene", "").strip()
        data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + name + "&key=" + key)
        susb = json.loads(data)["items"][0]["statistics"]["subscribeCount"]
        talk(susb + " tiene {:,d}".format(int(susb)) + " suscriptores")
    elif "hora" in rec:
        hora = datetime.datetime.now().strftime("%H:%M")
        talk("Son las " + hora)
    elif "busca" in rec:
        order = rec.replace("busca", "")
        info = wikipedia.summary(order, 1)
        talk(info)
    elif "broma" in rec:
        broma = (pyjokes.get_joke())
        talk("Vale corazon " + broma)
    else :
        talk("Repitemelo chulaco")

while True:
        run()
