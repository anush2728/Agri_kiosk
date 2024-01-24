import speech_recognition as sr
import pyttsx3
from google_trans_new import google_translator
import gtts as gt
from googletrans import Translator
from io import BytesIO
import pygame
from pygame import mixer
from noisereduce import reduce_noise
import numpy as np  # Import numpy for handling sampling rate

fl = 0
while fl == 0:
    def live_speech_to_text(language='ta-IN'):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Speak something in Tamil...")
            audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=15)  # Listen for up to 10 seconds

            try:
                # Get the sampling rate of the audio data
                sr_value = audio_data.sample_rate
                
                # Convert audio data to numpy array
                audio_array = np.frombuffer(audio_data.frame_data, dtype=np.int16)
                
                # Apply noise reduction to the audio data
                reduced_audio = reduce_noise(audio_array, sr_value)
                
                # Convert the numpy array back to audio data
                audio_data = sr.AudioData(reduced_audio.tobytes(), sr_value, audio_data.sample_width)
                
                text = recognizer.recognize_google(audio_data, language=language)
                return text
            except sr.UnknownValueError:
                return "Speech recognition could not understand audio"
            except sr.RequestError as e:
                return f"Could not request results from Google Speech Recognition service; {e}"

    # Example usage
    transcribed_text = live_speech_to_text()

    print("Transcribed text (Tamil):")
    print(transcribed_text)

    translator = Translator()
    translated_text = translator.translate(transcribed_text, src='ta', dest='en')
    print("Translated text (English):")
    print(translated_text.text)
    translated_text2 = translator.translate(translated_text.text, src='en', dest='ta')
    print(translated_text2.text)
    tts = gt.gTTS(text=translated_text2.text, lang='ta')

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
    c = input()
    if c.lower() == 'y':
        fl = 1
