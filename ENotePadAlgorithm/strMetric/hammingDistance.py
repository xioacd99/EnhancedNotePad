
def getHammingDistance(a, b):
    aLen = len(a)
    bLen = len(b)

    if aLen == 0 or bLen == 0:
        return 0

    diff = 0
    if aLen != bLen:
        diff = abs(aLen - bLen)
    if aLen < bLen:
        a = a + ' ' * diff
    elif bLen < aLen:
        b = b + ' ' * diff

    result = 0
    length = max(aLen, bLen)
    for i in range(length):
        if a[i] != b[i]:
            result += 1
    return result

if __name__ == '__main__':
    ans = getHammingDistance('12345','abcde')
    print(ans)