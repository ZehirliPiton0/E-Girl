import webbrowser
from winsound import PlaySound
from colorama import *
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
from random import choice
from pydub import AudioSegment
from selenium import webdriver
import time

print("")
print(Fore.YELLOW)

r = sr.Recognizer()


# def speeding():
#     in_path = 'answer.mp3'
#     ex_path = 'speed.mp3'
#     sound = AudioSegment.from_file(in_path)
#     slower_sound = speed_swifter(sound, 1.3)
#     slower_sound.export(ex_path, format="mp3")

# def speed_swifter(sound, speed=1.0):
#     sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
#     return sound_with_altered_frame_rate


def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("AŞKIM BALIM BİTANEM CANIM : Anlayamadım Aşko")
            time.sleep(30)
        except sr.RequestError:
            print("AŞKIM BALIM BİTANEM CANIM : Sistem Çalışmıyor Aşko")
        return voice


def response(voice):
    if "merhaba" in voice:
        speak("sanada merhaba")
    if "bye bye" in voice or "kapan" in voice or "baybay" in voice or "bay bay" in voice:
        playsound("tabi.mp3")
        print("")
        # print(Fore.GREEN + "Developed By 𝓩𝓮𝓱𝓲𝓻𝓵𝓲 𝓟𝓲𝓽𝓸𝓷 ")
        print(Style.RESET_ALL)
        print(Fore.RED + "𝒟𝑒𝓋𝑒𝓁𝑜𝓅𝑒𝒹 𝐵𝓎 𝐿𝒶𝓈𝓉 𝒞𝒾𝒽𝒶𝓃 𝒵𝑒𝒶𝓁 𝒫𝑒𝓃𝑔𝓊𝑒𝓃 𝒫𝒾𝓉𝑜𝓃 𝒵𝑒𝒽𝒾𝓇𝓁𝒾 𝒞𝑜𝓂𝓂𝓊𝓃𝓉𝓎")
        # print(Fore.RED + "𝓩𝓮𝓪𝓵 𝓒𝓸𝓶𝓾𝓷𝓽𝔂 ©")
        print(Style.RESET_ALL)
        print("")
        exit()

    if "teşekkür ederim" in voice or "sağ ol" in voice:
        speak("Rica Ederim Aşkım")
    if 'hangi gündeyiz' in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "Salı"

        elif today == "Tuesday":
            today = "Salı"

        elif today == "Wednesday":
            today = "Çarşamba"

        elif today == "Thursday":
            today = "Perşembe"

        elif today == "Friday":
            today = "Cuma"

        elif today == "Saturday":
            today = "Cumartesi"

        elif today == "Sunday":
            today = "Pazar"

        speak(today)

    if "saat kaç" in voice:
        selection = ["Saat şu an: ", "Saat kaçmazki şaka şaka saat: "]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selection)
        speak(selection + clock)

    if "arama yap" in voice:
        speak("ne aramamı istersin")
        search = record()
        url = "https://www.google.com/search?client=opera-gx&q={}".format(search)
        webbrowser.get().open(url)
        playsound("tabi.mp3")
        speak("{} için bulunanlar listeleniyor.".format(search))

    if "video ara" in voice:
        speak("ne aratmamı istersin")
        kelime = record()
        lnk = "https://www.youtube.com/results?search_query={}".format(kelime)
        webbrowser.get().open(lnk)
        playsound("tabi.mp3")

    if "insta" in voice:
        ins = "https://www.instagram.com/?hl=tr".format()
        webbrowser.get().open(ins)
        playsound("tabi.mp3")


def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    # speeding()
    tts.save(file)
    playsound(file)
    os.remove(file)


playsound("zor.mp3")

while True:
    voice = record()
    if voice != '':
        voice = voice.lower()
        print(voice.capitalize())
        response(voice)
