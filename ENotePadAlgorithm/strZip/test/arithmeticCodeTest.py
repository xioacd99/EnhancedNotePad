from ENotePadAlgorithm.strZip.arithmeticCode import *

if __name__ == '__main__':
    count = 10
    encode_str = "heloworldheloworld"
    strlen = len(encode_str)
    every = 3
    encoded = encode(encode_str, every)
    print(encoded)
    decoded = decode(encoded, strlen, every)