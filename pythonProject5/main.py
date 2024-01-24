import speech_recognition as sr
import pyttsx3
from  google_trans_new import google_translator 
import gtts as gt
import os
from googletrans import Translator
from playsound import playsound
from io import BytesIO
import pygame
from pygame import mixer

fl=0
while(fl==0):
    #k = Translator()
    translator = google_translator() 
    #k = Translator(service_urls=['translate.googleapis.com'])
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('silence please. Caliberating background noise')
        r.adjust_for_ambient_noise(source, duration=1)
        print('caliberated, now speak')

        audio = r.listen(source,5,15)
        text = r.recognize_google(audio)
    # text = text.lower()
        print('did you say', text)

    translator = Translator()
    out=translator.translate(text,src='ta',dest='en')
    print(out.text)
    final = translator.translate(out.text,src='en',dest='ta')
    print(final.text)
    tts=gt.gTTS(text=final.text,lang='ta')

    buffer = BytesIO()
    tts.write_to_fp(buffer)
    buffer.seek(0)

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the speech from the in-memory file
    mixer.music.load(buffer)

    # Play the speech
    mixer.music.play()

    # Wait for the speech to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    print("Do you want to exit?")
    c=input()
    if(c=='y' or c=='Y') : fl=1
        
