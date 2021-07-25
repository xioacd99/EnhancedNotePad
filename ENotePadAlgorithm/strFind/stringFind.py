'''
Author: xioacd99
Date: 2021-07-23 16:31:23
LastEditTime: 2021-07-23 22:18:03
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \.vscode\Github\EnhancedNotePad\stringFind.py
'''

import os

# 单词结尾符号/单词分隔符
wordSplit = [',', '.', ':', '"', ",", '\n', ' ', '?', '!', '(', ')',
             '，', '。', '‘', '‘', '“', '”', '？', '！', '（', '）']


# TODO: 将字符串匹配的公用部分抽象出来
# TODO: 每一个strfind添加slen < tlen的判定
# TODO: 将file查找的几个算法利用菜单选项这种合并（代码重构）
# TODO: 每个类的函数名字去掉
# TODO: caseSensitive参数好像设置错误了

class BruteForce(object):
    def __init__(self):
        pass

    def strBruteForceFind(self, source, target, pos=0, fullWord=True, caseSensitive=False):
        '''
        @description: 朴素字符串查找
        @param {*} source: 源字符串, target: 目标字符串, pos: 查询开始的位置, fullWord: 是否选择全字查询(True-全字匹配, False-非全字匹配), 是否区分大小写(True-是, False-否)
        @return {*} 返回下标列表
        '''
        # 如果有一方为空，则查询无效
        if len(source) == 0 or len(target) == 0:
            return []
        # 是否区分大小写
        if caseSensitive:
            source = source.lower()
            target = target.lower()

        sLen = len(source)
        tLen = len(target)
        i = pos
        j = 0
        idx = []

        while i < sLen:
            if source[i] == target[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1
                j = 0

            if j == tLen:
                wordStart = i - j
                # 是否全字匹配
                if fullWord:
                    wordEnd = i
                    while True:
                        if source[wordEnd] in wordSplit:
                            break
                        else:
                            wordEnd += 1
                    if wordEnd - wordStart == tLen:
                        idx.append(wordStart)
                else:
                    idx.append(wordStart)
                j = 0
        return idx

    def fileBurteForceFind(self, filename, target):
        '''
        @description: 朴素字符串查找
        @param {*} filename: 文件名
        @param {*} target: 目标字符串
        @return {*} results: 查询结果字符串
        '''
        results = []
        if os.path.exists(filename):
            lineNum = 1
            with open(filename, 'r') as file:
                line = file.readline()
                while line:
                    idx = self.strBruteForceFind(line, target)
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


class KMP(object):
    def __init__(self):
        pass

    def getKMPTable(self, word):
        '''
        @description: KMP next数组预处理
        @param {*} word: 预处理字符串
        @return {*} next: 返回处理好的next数组
        '''
        # word为空直接返回空列表
        if len(word) == 0:
            return []

        i = 0
        j = -1
        lenth = len(word)
        next = [0] * lenth
        next[0] = -1

        # 因为比较的是t[i+1]
        while i < lenth - 1:
            if j == -1 or word[i] == word[j]:
                i += 1
                j += 1
                if word[i] != word[j]:
                    next[i] = j
                else:
                    next[i] = next[j]
            else:
                j = next[j]
        return next

    def strKMPFind(self, source, target, pos=0, fullWord=True, caseSensitive=False):
        '''
        @description: KMP字符串查找
        @param {*} source: 源字符串, target: 目标字符串, pos: 查询开始的位置, fullWord: 是否选择全字查询(True-全字匹配, False-非全字匹配), 是否区分大小写(True-是, False-否)
        @return {*} idx: 返回下标列表
        '''
        # 如果有一方为空，则查询无效
        if len(source) == 0 or len(target) == 0:
            return []
        # 是否区分大小写
        if caseSensitive:
            source = source.lower()
            target = target.lower()

        next = self.getKMPTable(target)
        sLen = len(source)
        tLen = len(target)
        i = pos
        j = 0
        idx = []

        while i < sLen:
            if j == -1 or source[i] == target[j]:
                i += 1
                j += 1
            else:
                j = next[j]

            if j == tLen:
                wordStart = i - j
                # 是否全字匹配
                if fullWord:
                    wordEnd = i
                    while True:
                        if source[wordEnd] in wordSplit:
                            break
                        else:
                            wordEnd += 1
                    if wordEnd - wordStart == tLen:
                        idx.append(wordStart)
                else:
                    idx.append(wordStart)
                j = 0
        return idx

        return table

    def fileKMPFind(self, filename, target):
        '''
        @description: KMP字符串查找
        @param {*} filename: 文件名
        @param {*} target: 目标字符串
        @return {*} results: 查询结果字符串
        '''
        results = []
        if os.path.exists(filename):
            lineNum = 1
            with open(filename, 'r') as file:
                line = file.readline()
                while line:
                    idx = self.strKMPFind(line, target)
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


class Sunday(object):
    def __init__(self):
        pass

    def strSundayFind(self, source, target, pos=0, fullWord=True, caseSensitive=False):
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

        i = 0
        while i <= sLen - tLen:
            if source[i:i + tLen] == target:
                # 是否全字匹配
                if fullWord:
                    wordEnd = i
                    while True:
                        if source[wordEnd] in wordSplit:
                            break
                        else:
                            wordEnd += 1
                    if wordEnd - i == tLen:
                        idx.append(i)
                else:
                    idx.append(i)
                i += tLen
            else:
                rpos = target.rfind(source[i + tLen])
                if rpos == -1:
                    i += (tLen + 1)
                else:
                    i += (tLen - rpos)
        return idx

    def fileSundayFind(self, filename, target):
        results = []
        if os.path.exists(filename):
            lineNum = 1
            with open(filename, 'r') as file:
                line = file.readline()
                while line:
                    idx = self.strSundayFind(line, target)
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



