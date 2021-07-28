import os

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
                finded = False
                for j in range(len(locationsTmp), 0, -1):
                    locationTmp = locationsTmp[j - 1]
                    if locationTmp <= i - 1:
                        innerResult[str(i - 1)] = locationTmp
                        finded = True
                        break
                if finded == False:
                    innerResult[str(i - 1)] = -1
                self.charLocationTable[charTmp] = innerResult

    def getOffset(self, flagChar, stopLocation, matcherLen):
        if flagChar in self.charLocationTable:
            innerLocationTable = self.charLocationTable[flagChar]
            return matcherLen - 1 - innerLocationTable[str(stopLocation)]
        else:
            return matcherLen

    def strFind(self, source, target, pos=0, fullWord=True, caseSensitive=False):
        # 如果有一方为空，则查询无效
        if len(source) == 0 or len(target) == 0:
            return []
        # 是否区分大小写
        if caseSensitive:
            source = source.lower()
            target = target.lower()

        sLen = len(source)
        tLen = len(target)
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
                if fullWord:
                    wordEnd = pos
                    while True:
                        if source[wordEnd] in wordSplit:
                            break
                        else:
                            wordEnd += 1
                    if wordEnd - pos == tLen:
                        idx.append(pos)
                else:
                    idx.append(pos)
            pos += step
        return idx

    def fileFind(self, filename, target):
        results = []
        if os.path.exists(filename):
            lineNum = 1
            with open(filename, 'r') as file:
                line = file.readline()
                while line:
                    idx = self.strFind(line, target)
                    if idx:
                        # 生成查询字符串前半部分
                        singleResult = 'The ' + target + ' occurs ' + str(len(idx)) + ' times in line ' + str(
                            lineNum) + ', which positions are '
                        # 添加每行的具体位置
                        for pos in idx:
                            singleResult += '(' + str(lineNum) + ', ' + str(pos) + ') '
                        results.append(singleResult)
                    line = file.readline()
                    lineNum += 1
        else:
            with open(filename, 'w') as file:
                print('Create a new file named %s' % filename)
        return results

if __name__ == '__main__':
    hp = Horspool()
    ans = hp.strFind('be being be being ', 'be')
    print(ans)