from ENotePadAlgorithm.strFind.boyerMoore import *

if __name__ == '__main__':
    bm = BoyerMoore()
    ans = bm.fileBMFind('ENTest.txt', 'be')
    for singleResult in ans:
        print(singleResult)
