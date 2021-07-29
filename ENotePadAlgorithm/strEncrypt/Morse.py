# encode时会将非ANSII字符变为空格
# decode时会跳过非ANSII字符

# 摩斯电码加密的字符只有字符，数字，标点，不区分大小写
class MorseCoder:
    def __init__(self):
        self.encode_alphabet = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..",  # 加密对照表
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

    def encode(self, plaintext):
        """Encode AscII chars in plaintext to morse code"""
        charList = list(plaintext.upper())
        morsecodeList = \
            [self.encode_alphabet[char] if char in self.encode_alphabet.keys() else " " for char in charList]
        return " ".join(morsecodeList)

    def decode(self, morsecode):
        morsecodeList = morsecode.split(" ")
        charList = \
            [self.decode_alphabet[char] if char in self.decode_alphabet.keys() else char for char in morsecodeList]
        return "".join(charList)

    def get_encode_alphabet(self):
        return self.encode_alphabet

    def get_decode_alphabet(self):
        return self.decode_alphabet

    def strEncrypt(self, msg):
        return self.encode(msg)


if __name__ == '__main__':
    test = MorseCoder()
    result = test.strEncrypt('ABCD12345678')
    print(result)
