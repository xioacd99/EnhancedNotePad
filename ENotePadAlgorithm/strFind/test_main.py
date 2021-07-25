wordSplit = [',', '.', ':', '"', ",", '\n', ' ', '?', '!', '(', ')',
             '，', '。', '‘', '‘', '“', '”', '？', '！', '（', '）']

class BoyerMoore(object):
    def __init__(self):
        super(BoyerMoore, self).__init__()
        self.__matcher = None
        self.badCharTable = {}
        self.goodSuffixTable = {}

    def getBadCharTable(self, targer):
        # find positions every char
        charLocations = {}
        tLen = len(targer)
        for i in range(tLen):
            curChar = targer[i]
            locations = []
            if curChar in charLocations:
                locations = charLocations[curChar]
            locations.append(i)
            charLocations[curChar] = locations

        # build badCharTable
        self.badCharTable = {}
        for i in range(tLen, 0, -1):
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

    def getGoodSuffixTable(self, target):
        self.goodSuffixTable = {}
        tLen = len(target)
        for i in range(tLen, 1, -1):
            tmpSuffix = target[i - 1: tLen]
            tmpSuffixLen = len(tmpSuffix)
            isFind = False
            locationTmp = tLen - tmpSuffixLen - 1
            while True:
                if locationTmp <= 0 - tmpSuffixLen:
                    break
                matchedThisTime = True
                for j in range(0, tmpSuffixLen, 1):
                    if locationTmp + j < 0:
                        continue
                    if tmpSuffix[j] != target[locationTmp + j]:
                        matchedThisTime = False
                if matchedThisTime == True:
                    isFind = True
                    break
                locationTmp = locationTmp - 1

            if isFind == True:
                self.goodSuffixTable[tmpSuffix] = i - 1 - locationTmp
            else:
                self.goodSuffixTable[tmpSuffix] = tLen

    def goodSuffixOffset(self, word):
        if word == None or len(word) == 0:
            return 0
        return self.goodSuffixTable[word]

    def setMatcher(self, matcher):
        if matcher == None or len(matcher) == 0:
            return
        self.__matcher = matcher
        self.getBadCharTable(self.__matcher)
        self.getGoodSuffixTable(self.__matcher)

    def __searchLoop(self, content, matcher, start, result):
        if start + len(matcher) > len(content):
            return
        isFind = True
        step = len(matcher)
        matchedPart = ""
        for i in range(len(matcher), 0, -1):
            currentContentChar = content[start + i - 1]
            currentMatcherChar = matcher[i - 1]
            if currentContentChar != currentMatcherChar:
                offsetOfBadChar = self.badCharOffset(currentContentChar, i - 1)
                offsetOfGoodSuffix = self.goodSuffixOffset(matchedPart)
                step = max(offsetOfBadChar, offsetOfGoodSuffix)
                isFind = False
                break
            else:
                matchedPart = currentContentChar + matchedPart
        if isFind == True:
            step = 1
            wordEnd = start
            while True:
                if content[wordEnd] == ' ':
                    break
                else:
                    wordEnd += 1
            if wordEnd - start == len(matcher):
                result.append(start)
        self.__searchLoop(content, matcher, start + step, result)

    def strBMFind(self, source, target, pos=0, fullWord=True, caseSensitive=False):
        idx = []
        self.__searchLoop(source, False, target, 0, idx)
        return idx
        return self.search(source, False)

    def strFind(self, source, target, pos=0, fullWord=True, caseSensitive=True):
        # 如果有一方为空，则查询无效
        if len(source) == 0 or len(target) == 0:
            return []
        # 如果目串长度小于子串，则查询无效
        if len(source) < len(target):
            return []
        # 大小写敏感
        if not caseSensitive:
            source = source.lower()
            target = target.lower()

        idx = []
        sLen = len(source)
        tLen = len(target)

        while pos + tLen <= sLen:
            isFind = True
            step = tLen
            matchedPart = ""
            for i in range(tLen, 0, -1):
                if source[pos + i - 1] != target[i - 1]:
                    bcOffset = self.badCharOffset(source[pos + i - 1], i - 1)
                    gsOffset = self.goodSuffixOffset(target[i - 1])
                    step = max(bcOffset, gsOffset)
                    isFind = False
                    break
                else:
                    matchedPart = source[pos + i - 1] + matchedPart
            if isFind:
                step = 1
                # 是否全字匹配
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

if __name__ == '__main__':
    test = BoyerMoore()
    test.setMatcher('be')
    ans = test.strFind('being be be being ', 'be')
    print(ans)
