from ENotePadAlgorithm.strFind.KMP import *

if __name__ == '__main__':
    bf = KMP()
    ans = bf.strKMPFind('be being bebe ', 'be')
    print(ans)