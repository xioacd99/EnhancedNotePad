from stringFind import *


def test(filename):
    with open(filename) as fin:
        line = fin.readline()
        while line:
            print(line)
            line = fin.readline()


# FIXME: 实际查到的be有8个，但是只找到了6个，27、28两行不知道为什么查不到
if __name__ == '__main__':
    """
    ans = fileBurteForceFind('ENTest.txt', 'be')
    for singleResult in ans:
        print(singleResult)
    """
    lines=[]
    with open('ENTest.txt') as f:
       lines=f.readlines()
    target='be'
    for i,line in enumerate(lines):
        idx=line.find(target)
        if idx>=0:
            print(f'{target} is in line:{i+1},pos:{idx+1}')
