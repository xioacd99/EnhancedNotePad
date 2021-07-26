import os

wordSplit = [',', '.', ':', '"', ",", '\n', ' ', '?', '!', '(', ')',
             '，', '。', '‘', '‘', '“', '”', '？', '！', '（', '）']


class BoyerMoore(object):
    def __init__(self):
        super(BoyerMoore, self).__init__()
        self.badCharTable = {}
        self.goodSuffixTable = {}

    def getBadCharTable(self, word):
        # find positions every char
        charLocations = {}
        matcherLen = len(word)
        for i in range(matcherLen):
            currentChar = word[i]
            locations = []
            if currentChar in charLocations:
                locations = charLocations[currentChar]
            locations.append(i)
            charLocations[currentChar] = locations

        # build badCharTable
        self.badCharTable = {}
        for i in range(matcherLen, 0, -1):
            for charTmp in charLocations.keys():
                innerResult = {}
                if charTmp in self.badCharTable:
                    innerResult = self.badCharTable[charTmp]
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
                self.badCharTable[charTmp] = innerResult

    def badCharOffset(self, char, pos):
        if char in self.badCharTable:
            innerLocationTable = self.badCharTable[char]
            return pos - innerLocationTable[str(pos)]
        else:
            return pos + 1

    def getGoodSuffixTable(self, matcher):
        self.goodSuffixTable = {}
        matcherLen = len(matcher)
        for i in range(matcherLen, 1, -1):
            tmpSuffix = matcher[i - 1: matcherLen]
            tmpSuffixLen = len(tmpSuffix)
            finded = False
            locationTmp = matcherLen - tmpSuffixLen - 1
            while True:
                if locationTmp <= 0 - tmpSuffixLen:
                    break
                matchedThisTime = True
                for j in range(0, tmpSuffixLen, 1):
                    if locationTmp + j < 0:
                        continue
                    if tmpSuffix[j] != matcher[locationTmp + j]:
                        matchedThisTime = False
                if matchedThisTime == True:
                    finded = True
                    break
                locationTmp = locationTmp - 1

            if finded == True:
                self.goodSuffixTable[tmpSuffix] = i - 1 - locationTmp
            else:
                self.goodSuffixTable[tmpSuffix] = matcherLen

    def goodSuffixOffset(self, matchedPart):
        if matchedPart == None or len(matchedPart) == 0:
            return 0
        return self.goodSuffixTable[matchedPart]

    def strSearch(self, source, target, pos=0):
        sLen = len(source)
        tLen = len(target)
        result = []

        self.getBadCharTable(target)
        self.getGoodSuffixTable(target)

        while pos + tLen <= sLen:
            isFind = True
            step = tLen
            matchedPart = ""
            for i in range(tLen, 0, -1):
                curChar = source[pos + i - 1]
                currentMatcherChar = target[i - 1]
                if curChar != currentMatcherChar:
                    offsetOfBadChar = self.badCharOffset(curChar, i - 1)
                    offsetOfGoodSuffix = self.goodSuffixOffset(matchedPart)
                    step = max(offsetOfBadChar, offsetOfGoodSuffix)
                    isFind = False
                    break
                else:
                    matchedPart = curChar + matchedPart
            if isFind == True:
                step = 1
                wordEnd = pos
                while True:
                    if source[wordEnd] in wordSplit:
                        break
                    else:
                        wordEnd += 1
                if wordEnd - pos == len(target):
                    result.append(pos)
            pos += step
        return result

    def fileBMFind(self, filename, target):
        results = []
        if os.path.exists(filename):
            lineNum = 1
            with open(filename, 'r') as file:
                line = file.readline()
                while line:
                    idx = self.strSearch(line, target)
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


