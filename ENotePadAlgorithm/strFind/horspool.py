import os

# import time only for performance test
import time

wordSplit = [',', '.', ':', '"', ",", '\n', ' ', '?', '!', '(', ')',
             '，', '。', '‘', '‘', '“', '”', '？', '！', '（', '）']


class Horspool(object):
    def __init__(self):
        super(Horspool, self).__init__()
        self.charLocationTable = {}

    def buildCharLocationTable(self, matcher):
        # find positions every char
        charLocations = {}
        matcherLen = len(matcher)
        for i in range(matcherLen):
            currentChar = matcher[i]
            locations = []
            if currentChar in charLocations:
                locations = charLocations[currentChar]
            locations.append(i)
            charLocations[currentChar] = locations

        # build charLocationTable
        self.charLocationTable = {}
        for i in range(matcherLen, 0, -1):
            for charTmp in charLocations.keys():
                innerResult = {}
                if charTmp in self.charLocationTable:
                    innerResult = self.charLocationTable[charTmp]
                locationsTmp = charLocations[charTmp]
                isFind = False
                for j in range(len(locationsTmp), 0, -1):
                    locationTmp = locationsTmp[j - 1]
                    if locationTmp <= i - 1:
                        innerResult[str(i - 1)] = locationTmp
                        isFind = True
                        break
                if not isFind:
                    innerResult[str(i - 1)] = -1
                self.charLocationTable[charTmp] = innerResult

    def getOffset(self, flagChar, stopLocation, matcherLen):
        if flagChar in self.charLocationTable:
            innerLocationTable = self.charLocationTable[flagChar]
            return matcherLen - 1 - innerLocationTable[str(stopLocation)]
        else:
            return matcherLen

    def strFind(self, source, target, pos=0, fullWord=True, caseSensitive=True):
        sLen = len(source)
        tLen = len(target)

        # 如果主串和子串有一方为空或子串长度小于主串则返回空
        if (sLen == 0 or tLen == 0) or tLen < sLen:
            return []

        # 如果不区分大小写
        if not caseSensitive:
            source = source.lower()
            target = target.lower()

        idx = []
        self.buildCharLocationTable(target)

        while pos + tLen <= sLen:
            flag = source[pos + tLen - 1]
            isFind = True
            step = tLen
            for i in range(tLen - 1, 0, -1):
                curSChar = source[pos + i]
                curTChar = target[i]
                if curSChar != curTChar:
                    step = self.getOffset(flag, i, tLen)
                    isFind = False
                    break
            if isFind:
                step = 1
                wordStart = pos
                # 是否全字匹配
                if fullWord:
                    wordEnd = wordStart
                    while True:
                        if source[wordEnd] in wordSplit:
                            break
                        else:
                            wordEnd += 1
                    if wordEnd - wordStart == tLen:
                        idx.append(wordStart)
                else:
                    idx.append(wordStart)
            pos += step
        return idx

    def fileFind(self, filename, target):
        results = []
        if os.path.exists(filename):
            lineNum = 1
            with open(filename, 'r', encoding='utf-8') as file:
                line = file.readline()
                while line:
                    idx = self.strFind(line, target)
                    if idx:
                        for pos in idx:
                            results.append([lineNum, pos])

                        # 算法测试输入语句
                        '''
                        singleResult = 'The ' + target + ' occurs ' + str(len(idx)) + ' times in line ' + str(
                            lineNum) + ', which positions are '
                        for pos in idx:
                            singleResult += '(' + str(lineNum) + ', ' + str(pos) + ') '
                        results.append(singleResult)
                        '''

                    line = file.readline()
                    lineNum += 1
        else:
            with open(filename, 'w', encoding='uft-8') as file:
                print('Create a new file named %s' % filename)
        return results


if __name__ == '__main__':
    start = time.time()

    # write your test code
    test = Horspool()
    ans = test.fileFind(
        'F:\\.vscode\\Github\\EnhancedNotePad\\ENotePadAlgorithm\\algorithmTestData\\BigTest.txt', 'be')
    # end

    end = time.time()
    print('using time: %s seconds' % (end - start))
