__author__ = 'liqian.ma'

from os import system

def speak_chinese(str):
    system(('say -v Mei-Jia ' + str).encode('utf-8'))

def speak_english(str):
    system(('say -v Alex ' + str).encode('utf-8'))

def tts_system(str, language='zh-CN'):
    if language == 'zh-CN':
        speak_chinese(str)
    elif language == 'en-US':
        speak_english(str)