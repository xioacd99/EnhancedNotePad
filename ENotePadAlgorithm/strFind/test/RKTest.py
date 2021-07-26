from ENotePadAlgorithm.strFind.RK import *

if __name__ == '__main__':
    bf = RK()
    ans = bf.fileFind('ENTest.txt', 'be')
    for i in ans:
        print(i)