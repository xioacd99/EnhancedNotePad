# encode时会将非ANSII字符变为空格
# decode时会跳过非ANSII字符
class MorseCoder:
    __encode_alphabet = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..",  # 加密对照表
                         "E": ".", "F": "..-.", "G": "--.", "H": "....",
                         "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
                         "M": "--", "N": "-.", "O": "---", "P": ".--.",
                         "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
                         "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
                         "Y": "-.--", "Z": "--..",
                         "1": ".---", "2": "..---", "3": "...--", "4": "....-",
                         "5": ".....", "6": "-....", "7": "--...", "8": "---..",
                         "9": "----.", "0": "-----",
                         "(": ".--.-", "-": "-....-", "?": "..--..", "/": "-..-.",
                         ".": ".-.-.-", "@": ".--.-."
                         }
    __decode_alphabet = dict([val, key] for key, val in __encode_alphabet.items())  # 解密对照表

    def encode(self, plaintext):
        """Encode AscII chars in plaintext to morse code"""
        charList = list(plaintext.upper())
        morsecodeList = \
            [self.__encode_alphabet[char] if char in self.__encode_alphabet.keys() else " " for char in charList]
        return " ".join(morsecodeList)

    def decode(self, morsecode):
        morsecodeList = morsecode.split(" ")
        charList = \
            [self.__decode_alphabet[char] if char in self.__decode_alphabet.keys() else char for char in morsecodeList]
        return "".join(charList)

    def get_encode_alphabet(self):
        return self.__encode_alphabet

    def get_decode_alphabet(self):
        return self.__decode_alphabet

# 摩斯电码加密的字符只有字符，数字，标点，不区分大小写

if __name__ == '__main__':
    mc = MorseCoder()
    plaintext = "ABCD12345678"
    # plaintext = "helloworld"
    morsecode = mc.encode(plaintext)
    print("encode result:", morsecode)
    morsecode = ".... . .-.. .-.. ---     .-- --- .-. .-.. -.."
    plaintext = mc.decode(morsecode)
    print("decode result:", plaintext)
    mc.get_encode_alphabet()
    mc.get_decode_alphabet()