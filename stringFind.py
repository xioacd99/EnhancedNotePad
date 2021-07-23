import os

wordSplit = [',', '.', ':', '"', ",", '\n',' ',
             '，', '。', '‘', '‘', '“', '”']


# choice = True: 全字匹配
# choice = False: 非全字匹配
def strBruteForceFind(source, target, pos=0, fullWord=True):
    sLen = len(source)
    tLen = len(target)
    i = pos
    j = 0

    while i < sLen and j < tLen:
        ch = source[i]
        if source[i] == target[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if j == tLen:
        wordStart = i - j
        if fullWord:
            wordEnd = i
            while True:
                if source[wordEnd] in wordSplit:
                    break
                else:
                    wordEnd += 1
            if wordEnd - wordStart == tLen:
                return wordStart
            else:
                return -1
        return wordStart
    else:
        return -1


def strKMPFind(source, target, pos=0):
    pass


# 非全字匹配
def fileBurteForceFind(filename, target):
    results = []
    if os.path.exists(filename):
        lineNum = 1
        with open(filename, 'r') as file:
            line = file.readline()
            while line:
                pos = strBruteForceFind(line, target)
                if pos != -1:
                    pos += 1
                    singeResult = 'The ' + target + ' is in (line:' + str(lineNum) + ', pos:' + str(pos) + ')'
                    results.append(singeResult)
                line = file.readline()
                lineNum += 1
    else:
        with open(filename, 'w') as file:
            print('create a new file named %s' % filename)
    return results


def fileKMPFind(filename, target):
    pass
