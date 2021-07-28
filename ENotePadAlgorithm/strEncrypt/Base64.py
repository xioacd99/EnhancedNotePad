import base64


def base64Encode(msg):
    return base64.b64encode(bytes(msg,encoding='utf-8'))

if __name__=='__main__':
    ans = base64Encode('1')
    print(ans)