import pyttsx3, os


class ReadInner(object):
    def __init__(self):
        pass

    def strReadInner(self, str):
        engine = pyttsx3.init()
        engine.say(str)
        engine.runAndWait()

    def fileReadInner(self, filename):
        engine = pyttsx3.init()

        # 设置发音速率，默认值为200
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 30)

        # 设置发音大小，范围为0.0-1.0
        volume = engine.getProperty('volume')
        engine.setProperty('volume', 0.6)

        # 需要自己下载语音包安装
        # 0：汉语女声；1：英语男声；2：英语女声；3：日语女声；4：韩语女声；5：英语女声；6：粤语女声；7：台语女声
        voices = engine.getProperty('voices')
        voices = engine.setProperty('voice', voices[0].id)

        if os.path.exists(filename):
            with open(filename, 'r',encoding='utf-8') as file:
                line = file.readline()
                while line:
                    engine.say(line)
                    line = file.readline()
        else:
            with open(filename, 'w') as file:
                print('Create a new file named %s' % filename)
        engine.runAndWait()

    # 检查已有的语音包
    def checkExistedVoicePack(self):
        engine = pyttsx3.init()  # 初始化
        voices = engine.getProperty('voices')
        for voice in voices:
            print('id = {} \nname = {} \n'.format(voice.id, voice.name))
