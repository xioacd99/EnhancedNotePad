
from ENotePadAlgorithm.strEncrypt.Morse import *

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