from ENotePadAlgorithm.strEncrypt.SHA1 import SHA1

if __name__ == '__main__':
    sha1 = SHA1('1')
    ans = sha1.hexdigest()
    print(ans)