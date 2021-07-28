symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


def caesarEncrypt(msg, key=9):
    cipher = symbols[int(key):] + symbols[:int(key)]
    trans = str.maketrans(symbols, cipher)
    return msg.translate(trans)

if __name__ == '__main__':
    ans = caesarEncrypt('abcde','1')
    print(ans)