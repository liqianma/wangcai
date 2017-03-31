from sr_bing import SR_BING


class SR:

    def __init__(self, language='zh-CN'):
        self.bing_model = SR_BING(language=language)

    def initialize_system(self, audio_source):
        return self.bing_model.initialize_system(audio_source)

    # return audio
    def listen(self):
        return self.bing_model.listen()

    def sr(self, audio):
        bing_sr_res = self.bing_model.sr(audio)
        return bing_sr_res