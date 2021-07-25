from ENotePadAlgorithm.strEncrypt.HMAC import HMACSHA1

if __name__ == '__main__':
    hmacSHA1 = HMACSHA1('1','hello, world')
    ans = hmacSHA1.hexdigest()
    print(ans)