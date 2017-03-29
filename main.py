# -*- coding: utf-8 -*-

import speech_recognition.base as sr
from os import system

r = sr.Recognizer()
m = sr.Microphone()

lauguage = 'zh-CN'
# lauguage = 'en-US'

def speak_chinese(str):
    system(('say -v Mei-Jia ' + str).encode('utf-8'))

BING_KEY = "f2004b4375df4f4bab41e35b2ce1a493"
access_token = r.connect_bing_reco_sevice(BING_KEY)

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    r.energy_threshold = r.energy_threshold * 1.5
    r.dynamic_energy_threshold = False
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")


        # recognize speech using Microsoft Bing Voice Recognition
        try:
            command = r.recognize_bing(audio, key=BING_KEY, access_token=access_token, language=lauguage)
            print(" -Microsoft Bing Voice Recognition: " + command)
        except sr.UnknownValueError:
            print(" -Microsoft Bing Voice Recognition could not understand audio")
            continue
        except sr.RequestError as e:
            print(" -Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
            continue

        if command == u'你好':
            speak_chinese(u'你好')
        elif command == u'时间':
            speak_chinese(u'我不知道')

        # # recognize speech using Google Speech Recognition
        # try:
        #     # for testing purposes, we're just using the default API key
        #     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        #     # instead of `r.recognize_google(audio)`
        #     print(" -Google Speech Recognition: " + r.recognize_google(audio, language=lauguage))
        # except sr.UnknownValueError:
        #     print(" -Google Speech Recognition could not understand audio")
        # except sr.RequestError as e:
        #     print(" -Could not request results from Google Speech Recognition service; {0}".format(e))

except KeyboardInterrupt:
    pass
