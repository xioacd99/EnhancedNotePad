import os

# 单词结尾符号/单词分隔符
wordSplit = [',', '.', ':', '"', ",", '\n', ' ', '?', '!', '(', ')',
             '，', '。', '‘', '‘', '“', '”', '？', '！', '（', '）']

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