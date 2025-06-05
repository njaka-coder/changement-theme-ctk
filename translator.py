import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import pygame
import os
import time

# Initialisation des objets
r = sr.Recognizer()
translator = Translator()

# Initialisation de pygame pour la lecture audio
pygame.mixer.init()

try:
    with sr.Microphone() as source:
        print("Parlez maintenant en anglais...")
        # Ajustement du bruit ambiant
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=10)

        try:
            # Reconnaissance vocale
            speech_text = r.recognize_google(audio, language='en-US')
            print(f"Texte reconnu: {speech_text}")

            # Traduction
            translated = translator.translate(speech_text, src='en', dest='fr')
            translated_text = translated.text
            print(f"Traduction: {translated_text}")

            # Synthèse vocale
            voice = gTTS(text=translated_text, lang='fr')
            voice.save("voice.mp3")

            #Lecture du fichier audio avec pygame
            pygame.mixer.music.load("voice.mp3")
            pygame.mixer.music.play()

            # Attendre que la lecture soit terminée
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)

                # Suppression du fichier temporaire (optionnel)
                time.sleep(0.5)  # Petit délai pour s'assurer que le fichier est libéré
            try:
                os.remove("voice.mp3")
            except:
                pass

        except sr.UnknownValueError:
            print("Impossible de comprendre l'audio")
        except sr.RequestError as e:
            print(f"Erreur lors de la requête au service Google: {e}")
        except Exception as e:
            print(f"Erreur lors de la traduction: {e}")

except sr.WaitTimeoutError:
    print("Timeout: Aucun audio détecté")
except Exception as e:
    print(f"Erreur avec le microphone: {e}")