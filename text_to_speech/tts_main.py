from tts_system import tts_system

class TTS:

    def __init__(self, language='zh-CN'):
        self.language = language

    def tts(self, str):
        print 'TTS speaking:', str
        tts_system(str, self.language)