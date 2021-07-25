import base64


def base64Encode(msg):
    return base64.b64encode(bytes(msg,encoding='utf-8'))