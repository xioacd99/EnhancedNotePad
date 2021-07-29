import base64


class Base64(object):
    def strEncrypt(self, msg):
        return base64.b64encode(bytes(msg, encoding='utf-8'))


if __name__ == '__main__':
    test = Base64()
    result = test.encrypt('1')
    print(result)
