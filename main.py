# video demonstration: https://youtu.be/bVW2WWnhHJo

import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr

api_key = "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"

lang = 'en'

openai.api_key = api_key

while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            print("Listening...")
            try:
                audio = r.listen(source, timeout=5)
                print("Processing...")
                said = r.recognize_google(audio)
                print("Recognized:", said)

                if "Sarah" in said:
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                              messages=[{"role": "user", "content": said}])
                    print("OpenAI Response:", completion)

                    text = completion.choices[0].message.content
                    speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
                    speech.save("welcome1.mp3")
                    playsound.playsound(r"C:\Users\OMEN\PycharmProjects\HelpyBot\welcome1.mp3")
                    print("Action performed!")

            except sr.UnknownValueError:
                print("Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"Exception: {str(e)}")

            return said


    get_audio()