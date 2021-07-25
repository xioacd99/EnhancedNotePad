from ENotePadAlgorithm.strEncrypt.ECC import *

if __name__ == '__main__':
    pri, pub = getKeyPair()
    msg = pub.encryptMsg("test")
    print(msg)
    print(pri.decryptMsg(msg))

    print("\nECDH")
    a = ECDH()
    pa = a.sendPublic()
    b = ECDH()
    pb = b.sendPublic()

    print(a.getCommonKey(pb))
    print(b.getCommonKey(pa))