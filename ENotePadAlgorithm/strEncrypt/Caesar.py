class Caesar(object):
    def __init__(self):
        self.symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    def strEncrypt(self, msg, key=9):
        cipher = self.symbols[int(key):] + self.symbols[:int(key)]
        trans = str.maketrans(self.symbols, cipher)
        return msg.translate(trans)


if __name__ == '__main__':
    test = Caesar()
    result = test.strEncrypt('abcde')
    print(result)
