from  ENotePadAlgorithm.strEncrypt.AES import *

if __name__ == '__main__':
    aes = AES()
    ans=aes.encrypt('1','1111111111111111')
    print(ans)
    out=aes.decrypt(ans,'1111111111111111')
    print(out)
    pass