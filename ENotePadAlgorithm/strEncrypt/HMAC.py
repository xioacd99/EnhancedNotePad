from ENotePadAlgorithm.strEncrypt.SHA1 import SHA1


class HMACSHA1(object):
    msg = bytearray()
    key = bytearray()
    func = SHA1
    blockSize = 0
    outputSize = 0

    def __init__(self, msg, key='hello, world', func=SHA1, blockSize=64, outputSize=20):
        if type(msg) == str:
            msg = msg.encode()
        if type(key) == str:
            key = key.encode()
        self.msg = bytearray(msg)
        self.key = bytearray(key)
        self.func = func
        self.blockSize = blockSize
        self.outputSize = outputSize

    def __xor(self, a, b):
        t = type(a)
        r = []
        assert len(a) == len(b)
        for i in range(len(a)):
            r.append(a[i] ^ b[i])
        return t(r)

    def digest(self):
        if len(self.key) > self.blockSize:
            self.key = self.func(self.key).digest()
        if len(self.key) < self.blockSize:
            padding = self.blockSize - len(self.key)
            self.key.extend([0] * padding)

        opad = self.__xor(self.key, [0x5c] * self.blockSize)
        ipad = self.__xor(self.key, [0x36] * self.blockSize)
        result = self.func(ipad + self.msg).digest()
        result = self.func(opad + result).digest()
        return result

    def strEncrypt(self):
        digest = self.digest()
        return digest.hex()

if __name__ == '__main__':
    hmacSHA1 = HMACSHA1('12345')
    ans = hmacSHA1.strEncrypt()
    print(ans)