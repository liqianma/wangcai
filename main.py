# -*- coding: utf-8 -*-

from speech_recognition.base import Microphone
from speech_recognition.sr_main import SR
from text_to_speech.tts_main import TTS

m = Microphone()
sr = SR(language='zh-CN')
tts = TTS(language='zh-CN')

try:
    sr.initialize_system(m)
    tts.tts(u'你好主人，我是旺财，汪汪')
    while True:

        audio = sr.listen()

        text = sr.sr(audio)

        if text == u'你好':
            tts.tts(u'你好，汪汪')
        elif text == u'再见':
            tts.tts(u'再见，汪汪')
        elif text is None:
            tts.tts(u'说人话主人，汪汪')
        else:
            tts.tts(u'对不起主人，我听不懂，汪汪')

except KeyboardInterrupt:
    pass
