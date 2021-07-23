from stringFind import *

if __name__ == '__main__':
    # ans = strKMPFind('being be are be ','be')
    # print(ans)
    ans = fileKMPFind('ENTest.txt', 'be')
    for singleResult in ans:
        print(singleResult)
