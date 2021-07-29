
def getL0NormDistance(a, b):
    aSpace = 0
    bSpace = 0
    for i in range(len(a)):
        if a[i] == ' ':
            aSpace += 1
    for i in range(len(b)):
        if b[i] == ' ':
            bSpace += 1
    return abs(aSpace - bSpace)


def getL1NormDistance(a, b):
    aSum = 0
    for i in range(len(a)):
        aSum += ord(a[i])
    bSum = 0
    for i in range(len(b)):
        bSum += ord(b[i])
    return abs(aSum - bSum)/256


def getL2NormDistance(a, b):
    aRMS = 0
    for i in range(len(a)):
        aRMS += (ord(a[i]) ** 2)
    aRMS = aRMS ** (0.5)
    bRMS = 0
    for i in range(len(b)):
        bRMS += (ord(b[i]) ** 2)
    bRMS = bRMS ** (0.5)
    return abs(aRMS - bRMS)/256


def getMinNormDistance(a, b):
    aLen = len(a)
    bLen = len(b)

    diff = abs(aLen - bLen)
    if aLen < bLen:
        a += ' ' * diff
    else:
        b += ' ' * diff

    minStr = ''
    length = max(aLen, bLen)
    for i in range(length):
        minStr += min(a[i], b[i])
    # 现在是四个都弄了，到时候选择一种范数就可以了
    aL1 = getL1NormDistance(a, minStr)
    # aL2=getL2NormDistance(a,minStr)
    bL1 = getL1NormDistance(b, minStr)
    # bL2=getL2NormDistance(b,minStr)
    return min(aL1, bL1)


def getMaxNormDistance(a, b):
    aLen = len(a)
    bLen = len(b)

    diff = abs(aLen - bLen)
    if aLen < bLen:
        a += ' ' * diff
    else:
        b += ' ' * diff

    minStr = ''
    length = max(aLen, bLen)
    for i in range(length):
        minStr += max(a[i], b[i])
    # 现在是四个都弄了，到时候选择一种范数就可以了
    aL1 = getL1NormDistance(a, minStr)
    # aL2=getL2NormDistance(a,minStr)
    bL1 = getL1NormDistance(b, minStr)
    # bL2=getL2NormDistance(b,minStr)
    return min(aL1, bL1)

if __name__ == '__main__':
    a = 'hello, world'
    b = 'HELLO, WORLD'
    print(getL0NormDistance(a, b))
    print(getL1NormDistance(a, b))
    print(getL2NormDistance(a, b))
    print(getMinNormDistance(a, b))
    print(getMaxNormDistance(a, b))
