# -*- coding: utf-8 -*-
import time
import gtts
import os 
import speech_recognition as sr
from playsound import playsound
from checklist import (
    PREFLIGHT,
    BEFORE_START,
    BEFORE_TAKEOFF,
    BEFORE_TAXI, AFTER_TAKEOFF,
    DESCENT,
    APPROACH,
    LANDING,
    SECURING_AIRCRAFT,
    SHUTDOWN,
    FALLBACK_MESSAGE)

microfone = sr.Recognizer()

def checklist(itens: list, default_delay=1):
    for index, item in enumerate(itens):
        list_lenght = len(itens)
        tss = gtts.gTTS(item["item"], lang='en')
        tss.save("speech.mp3")
        playsound("speech.mp3")
        if index == 0 or index == (list_lenght - 2):
            time.sleep(default_delay+1)
        else: 
            time.sleep(default_delay)


def run(audio):
    try:
        os.system("clear")
        
        frase = str(microfone.recognize_google(audio, language='en'))
        frase = frase.lower()

        if "preflight" in frase:
            checklist(itens=PREFLIGHT)
        elif "before" in frase and "start" in frase:
            checklist(itens=BEFORE_START)
        elif "before" in frase and "taxi" in frase:
            checklist(itens=BEFORE_TAXI)
        elif "before" in frase and "takeoff" in frase:
            checklist(itens=BEFORE_TAKEOFF)
        elif "after" in frase and "takeoff" in frase:
            checklist(itens=AFTER_TAKEOFF)
        elif "descent" in frase:
            checklist(itens=DESCENT)
        elif "approach" in frase:
            checklist(itens=APPROACH)
        elif "landing" in frase:
            checklist(itens=LANDING)
        elif "shutdown" in frase:
            checklist(itens=SHUTDOWN)
        elif "securing" in frase and "aircraft" in frase:
            checklist(itens=SECURING_AIRCRAFT)
        else:
            checklist(itens=FALLBACK_MESSAGE)
        main()
    except Exception as exc:
        main()


def ouvir_microfone():
    try:
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            print("Estou te ouvindo...")
            audio = microfone.listen(source)
            return audio
    except Exception as exc:
        print(f"Erro ao tentar escutar o usuário {exc}")


def main():
    text = ouvir_microfone()
    run(audio=text)


if __name__ == "__main__":
    main()
