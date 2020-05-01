import time


class RandomGenerate:

    def __init__(self):
        self.timestamp = str(round(time.time_ns()))


    #随机生成手机号
    def random_phone(self):
        random_phone = "131" + self.timestamp[-8:]
        return random_phone