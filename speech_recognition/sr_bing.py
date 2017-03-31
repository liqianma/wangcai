import base as sr

class SR_BING:

    BING_KEY = "f2004b4375df4f4bab41e35b2ce1a493"

    def __init__(self, language='zh-CN'):
        self.lauguage = language
        self.r = sr.Recognizer()

    def initialize_system(self, audio_source):
        print("SR_BING: Initialize...")
        with audio_source as source:
            self.r.adjust_for_ambient_noise(source)
        self.r.energy_threshold = self.r.energy_threshold * 1.5
        self.r.dynamic_energy_threshold = False
        # print("Set minimum energy threshold to {}".format(self.r.energy_threshold))
        self.audio_source = audio_source
        print("SR_BING: Initialize done.")

    # return audio
    def listen(self):
        with self.audio_source as source:
            audio = self.r.listen(source)
        print("SR_BING Listener: Got command.")
        return audio

    # must be invoked every several minutes
    def get_token(self):
        self.access_token = self.r.connect_bing_reco_sevice(self.BING_KEY)

    def sr(self, audio):
        try:
            self.get_token()
            command = self.r.recognize_bing(audio,
                                            key=self.BING_KEY,
                                            access_token=self.access_token,
                                            language=self.lauguage)
        except sr.UnknownValueError:
            print("SR_BING Recognition: ERROR: Command not valid.")
            return None
        except sr.RequestError as e:
            print("SR_BING ERROR: Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
            return None
        print("SR_BING Recognition: " + command)
        return command